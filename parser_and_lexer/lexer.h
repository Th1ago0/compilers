#include <unordered_map>
#include <string>
#include <sstream>

using std::string;
using std::unordered_map;
using std::stringstream;

enum Tag {NUM=256, ID, TRUE, FALSE};

struct Token
{
    int tag;
    Token() : tag(0) {}
    Token(int t) : tag(t) {}
    virtual string ToString() { stringstream ss; ss << char(tag); return ss.str(); }
};

struct Num : public Token
{
    int value;
    Num() : Token(Tag::NUM), value(0) {}
    Num(int v) : Token(Tag::NUM), value(v) {}
    virtual string ToString() { stringstream ss; ss << value; return ss.str(); }
};

struct Id : public Token
{
    string name;
    Id() : Token(Tag::ID) {}
    Id(int t, string s) : Token(t), name(s) {}
    virtual string ToString() { return name; }
};

class Lexer
{
private:
    struct
    {
        Token t;
	Num n;
	Id i;
    }
    token;

    int line = 1;
    char peek;

    unordered_map<string, Id> id_table;

public:
    Lexer();
    int Line_num();
    Token * Scan();
};

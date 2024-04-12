#include <string>

using std::string;

class SyntaxError
{
private:
    int line_num;
    string desc;
public:
    SyntaxError(int line, string msg);
    void what();
};

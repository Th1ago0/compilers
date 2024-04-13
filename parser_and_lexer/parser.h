#include "lexer.h"

class Parser
{
private:
    Lexer scanner;
    Token * lookahead;

    void Term();
    void Expr();
    void Fact();
    bool Match(int tag);

public:
    Parser();
    void Start();
};

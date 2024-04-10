#include <iostream>
#include "parser.h"
#include <cctype>

using std::cout;
using std::cin;
using std::endl;

/*
    Gramatic

    Expr -> Term Oper
    Oper -> + Term { print("+") } Oper
          | - Term { print("-") } Oper
    Term -> 0 { print("0") }
          | ...
	  | 9 { print("9") }
*/

// Expr -> Term Oper
void Parser::Expr()
{
    // Term
    Term();
    
    // Oper
    while (true)
    {
        // Oper -> + Term { print("+") } Oper
        if (lookahead == '+')
        {
            Match('+');
	    Term();
            cout << '+';
	}
	// Oper -> - Term { print("-") } Oper
	else if (lookahead == '-')
	{
	    Match('-');
	    Term();
	    cout << '-';
	}
	// Empty production
	else return;
    };
};

// Term -> 0 ... 9
void Parser::Term()
{
    if (isdigit(lookahead))
    {
        cout << lookahead;
	Match(lookahead);
    }
    else
    {
        throw SyntaxError{};
    };
};

void Parser::Match(char t)
{
    if (t == lookahead)
    {
        lookahead = cin.get();
    }
    else
    {
        throw SyntaxError{};
    };
};

Parser::Parser()
{
    lookahead = 0;
};

void Parser::Start()
{
    lookahead = cin.get();
    Expr();
    if (lookahead != '\n')
    {
        throw SyntaxError{};
    };
};

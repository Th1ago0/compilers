#include "lexer.h"
#include <sstream>
#include <iostream>

using std::cin;
using std::cout;
using std::stringstream;

// Constructor
Lexer::Lexer()
{
    // Inserts reserved words into the id's table
    id_table["true"] = Id{Tag::TRUE, "true"};
    id_table["false"] = Id{Tag::FALSE, "false"};
    
    // Starts the input reading
    peek = cin.get();
}

int Lexer::Line_num()
{
    return line;
};

// Returns tokens to the parser
Token * Lexer::Scan()
{
    // Skips spaces, tabs and new lines
    while (isspace(peek))
    {
        if (peek == '\n')
	{
	    line += 1;
	};
	peek = cin.get();
    };

    // Returns the numbers
    if (isdigit(peek))
    {
        int v = 0;


	do
	{
	    // Converts char to int
	    int n = peek - '0';
	    v = 10 * v + n;
	    peek = cin.get();
        }
	while (isdigit(peek));

	// DEBUG: shows the recognized token
	cout << "<num, " << v << "> ";

	// Returns the NUM token
        token.n = Num{v};
	return &token.n;
    };

    // Returns the KW and id's
    if (isalpha(peek))
    {
        stringstream ss;

	do
	{
	    ss << peek;
	    peek = cin.get();
	}
	while (isalpha(peek));

	string s = ss.str();
	auto pos = id_table.find(s);

	// If the lexeme is already in the table
	if (pos != id_table.end())
	{
	    // Returns the ID token
	    token.i = pos->second;
            return &token.i;
	};

        // If the lexeme is not in the table
        Id new_id {Tag::ID, s};
	id_table[s] = new_id;

	// Returns the id token
        token.i = new_id;
	return &token.i;
    };

    // Operators and isolated alphanumeric characters
    Token op {peek};
    peek = ' ';

    // Returns the token
    token.t = op;
    return &token.t;
};

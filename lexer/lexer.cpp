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
}

// Returns tokens to the parser
Token Lexer::Scan()
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
	    v = 10 * n + v;
	    peek = cin.get();
        }
	while (isdigit(peek));

	// DEBUG: shows the recognized token
	cout << "<num, " << v << "> ";

	// Returns the NUM token
	return Num{v};
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
	    // DEBUG: shows the recognized token
	    switch (pos->second.tag)
	    {
	        case TRUE: cout << "<TRUE, " << pos->second.name << ">"; break;
		case FALSE: cout << "<FALSE, " << pos->second.name << ">"; break;
		default: cout << "<ID, " << pos->second.name << ">"; break;
	    };

	    // Returns the ID token
	    return pos->second;
	};

        // If the lexeme is not in the table
        Id new_id {Tag::ID, s};
	id_table[s] = new_id;

	// DEBUG
	cout << "<ID, " << new_id.name << ">";

	// Returns the id token
	return new_id;
    };

    // Operators and isolated alphanumeric characters
    Token t {peek};
    peek = ' ';
    
    // DEBUG
    cout << "<" << char(t.tag) << "> ";

    // Returns the token
    return t;
};

void Lexer::Start()
{
    // Simulates the parser
    while (peek != '\n')
    {
        Scan();
    };
};

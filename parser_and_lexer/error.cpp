#include "error.h"
#include <iostream>


using std::cout;
using std::endl;

SyntaxError::SyntaxError(int line, string msg) : line_num(line), desc(msg) 
{
};

void SyntaxError::what()
{
    cout << "\nError (line " << line_num << "): " << desc << endl;
};

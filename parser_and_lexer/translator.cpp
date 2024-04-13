#include "parser.h"
#include "error.h"
#include <iostream>

using namespace std;

int main()
{
    Parser translator;
    try
    {
        translator.Start();
    }
    catch (SyntaxError error)
    {
	error.what();
    }
    cout << endl;

}

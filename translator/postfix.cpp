#include "parser.h"
#include <iostream>
using namespace std;

int main(int argc, char *argv[])
{
    Parser tradutor;
    try
    {
        tradutor.Start();
    }
    catch (SyntaxError)
    {
        cout << "^\n";
	cout << "Erro de Sintaxe\n";
    };
    cout << endl;
};

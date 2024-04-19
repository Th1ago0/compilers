from parser import SyntaxErro, Parser


translator = Parser();
try:
    translator.start();
except SyntaxErro:
    print("\nErro de Sintaxe")
print()

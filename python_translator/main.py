from parser import *

parser = Parser()
try:
    parser.start()
except SyntaxErro as e:
    e.show()

print()

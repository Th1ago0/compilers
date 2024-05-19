from parser import *

parser = Parser()
try:
    parser.start()
except SyntaxError as e:
    e.show()
print()

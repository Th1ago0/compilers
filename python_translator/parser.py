from lexer import *
from error import *
import sys
import pdb

class Parser:

    def __init__(self):
        with open('file.llds', 'r') as file:
            file_content = file.read()
            
        self.scanner = Lexer(file_content)
        self.lookahead = self.scanner.scan()
        
    def is_end(self):
        if self.lookahead.tag == Tag().EOF:
            print()
            sys.exit()

    def expr(self):
        pdb.set_trace()
        self.term()
        self.is_end()

        while True:

            if self.lookahead.tag == "+":

                self.match("+")
                self.term()
                print("+", end="")

            elif self.lookahead.tag == "-":

                self.match("-")
                self.term()
                print("-", end="")

            else:
                return

    def term(self):
        self.fact()
        self.is_end()
        while True:
            if self.lookahead.tag == "*":
                self.match("*")
                self.fact()
                print("*", end="")
            elif self.lookahead.tag == "/":
                self.match("/")
                self.fact()
                print("/", end="")
            else:
                return

    def fact(self):
        self.is_end()
        if self.lookahead.tag == "(":
            self.match("(")
            self.expr()
            if not self.match(")"):
                raise SyntaxErro(self.scanner.lineno(), "\')\' expected.")
        elif self.lookahead.tag == Tag().NUM:
            print(f"[{self.lookahead.to_string()}]", end="")
            self.match(Tag().NUM)

        elif self.lookahead.tag == Tag().ID:
            print(f"[{self.lookahead.to_string()}]", end="")
            self.match(Tag().ID)

        else:
            raise SyntaxErro(self.scanner.lineno(), f"Symbol {self.lookahead.to_string()} is invalid.")

    def match(self, t):
        #pdb.set_trace()
        if self.lookahead.tag == Tag().EOF:
            return
        else:
            if self.lookahead.tag == t:
                self.lookahead = self.scanner.scan()
                #self.is_end()
                return True
    
            else:
                return False

    def start(self):
    
        self.expr()


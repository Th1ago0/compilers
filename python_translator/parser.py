from lexer import *
from error import *


class Parser:
    def __init__(self):
        self.scanner = Lexer("file.llds")
        self.lookahead = self.scanner.scan()
            
    def expr(self):
        self.term()
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
        if self.lookahead.tag == "(":
            self.match("(")
            self.expr()
            if not self.match(")"):
                raise SyntaxErro(self.scanner.lineno(), "\')\' expected.")
        elif self.lookahead.tag == Tag().NUM:
            self.match(Tag().NUM)
            print(f"[{self.lookahead.str()}]", end="")
        elif self.lookahead.tag == Tag().ID:
            self.match(Tag().ID)
            print(f"[{self.lookahead.str()}]", end="")
        else:
            raise SyntaxErro(self.scanner.lineno(), f"Symbol {self.lookahead.str()} is invalid.")
            
    def match(self, t):
        if self.lookahead.tag == t:
            self.lookahead = self.scanner.scan()
            return True
        else:
            return False
                
    def start(self):
        self.expr()

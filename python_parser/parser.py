class SyntaxErro(Exception):

    pass

"""
    Gramatic

    Expr -> Term Oper
    Oper -> + Term { print("+") } Oper
          | - Term { print("-") } Oper
    Term -> 0 { print("0") }
          | ...
          | 9 { print("9") }
"""

class Parser:

    def __init__(self):

        self.tokens = [];
        self.index = 0;

    def expr(self):

        self.term();

        while self.index < len(self.tokens):

            if self.tokens[self.index] == "+":

                self.match("+");
                self.term();
                print("+", end="");

            elif self.tokens[self.index] == "-":

                self.match("-");
                self.term();
                print("-", end="")

            else:
                break

    def term(self):

        if self.tokens[self.index].isdigit():

            print(self.tokens[self.index], end="");
            self.match(self.tokens[self.index]);

        else:
            raise SyntaxErro


    def match(self, t):

        if t == self.tokens[self.index]:

            self.index += 1;

        else:
            raise SyntaxErro

    def start(self):
        self.tokens = input()
        self.expr();


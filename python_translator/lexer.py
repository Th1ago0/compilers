import pdb

class Tag:
    def __init__(self):
        self.ID = "ID"
        self.NUM = "NUM"
        self.TRUE = "TRUE"
        self.FALSE = "FALSE"
        self.EOF = "EOF"

class Token:
    def __init__(self, tag):
        self.tag = tag

    def to_string(self):
        return self.tag

class Id(Token):
    def __init__(self, tag, name):
        self.tag = tag
        self.name = name
        super().__init__(self.tag)

    def to_string(self):
        return self.name

class Num(Token):
    def __init__(self, value):
        self.value = value
        self.tag = Tag().NUM
        super().__init__(self.tag)

    def to_string(self):
        return str(self.value)

class TokenHandler:
    def __init__(self):
        self.t = None
        self.n = None
        self.i = None
        

class Lexer:
    def __init__(self, source):

        self.source_code = source
        self.index = 0

        self.line = 1
        self.peek = self.source_code[self.index]

        self.id_table = {}
        self.id_table["false"] = Id(Tag().FALSE, "false")
        self.id_table["true"] = Id(Tag().TRUE, "true")
        
        self.token = TokenHandler()

    def next_char(self):
        if len(self.source_code) > (self.index + 1):
            self.index += 1
            self.peek = self.source_code[self.index]
        else:
            self.peek = " "
    
    def is_space(self):
        if self.peek == "\n":
            self.line += 1
        self.next_char()

    def is_digit(self):
        v = 0
        n = int(self.peek)
        v = 10 * v + n
        self.next_char()

        while self.peek.isdigit():
            n = int(self.peek)
            v = 10 * v + n
            self.next_char()

        self.token.n = Num(v)
        return self.token.n

    def is_alpha(self):
        s = self.peek
        self.next_char()

        while self.peek.isalpha():
            s += self.peek
            self.next_char()

        value = self.id_table.get(s)

        if value is not None:
            self.token.i = value
            return self.token.i

        new_id = Id(Tag().ID, s)
        self.id_table[s] = new_id

        self.token.i = new_id
        return self.token.i
    
    def lineno(self):
        return self.line

    def scan(self):
        #pdb.set_trace()
        if self.index == len(self.source_code):
            eof = Token(Tag().EOF)
            return eof
        
        while self.peek.isspace():
            self.is_space()

        if self.peek.isdigit():
            return self.is_digit()
        
        if self.peek.isalpha():
            return self.is_alpha()

        if self.peek == "/":
            if self.source_code[self.index + 1] == "/":
                self.next_char()
                self.next_char()
                while self.peek != "\n":
                    self.next_char()
                self.next_char()
                
            elif self.source_code[self.index + 1] == "*":
                self.next_char()
                self.next_char()
                while self.peek != "*" and self.source_code[self.index + 1] != "/":
                    self.next_char()
                self.next_char()
                self.next_char()
        
        if not (self.peek.isalnum() or self.peek.isspace()):
            symbol = Token(self.peek)
            peek = ' '
            self.next_char()
            self.token.t = symbol
            return self.token.t
        else:
            self.scan()

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
        
    def str(self):
        return self.tag
        
class Id(Token):
    def __init__(self, tag, name):
        self.tag = tag
        self.name = name
        super().__init__(self.tag)
        
    def str(self):
        return self.name
        
class Num(Token):
    def __init__(self, value):
        self.value = value
        self.tag = Tag().NUM
        super().__init__(self.tag)
        
    def str(self):
        return str(self.value)
        
class TokenHandler:
    def __init__(self):
        self.t = None
        self.n = None
        self.i = None
        
class Lexer:
    def __init__(self, file_name):
        self.file = open(file_name, "r")
        self.line = 1
        self.peek = self.file.read(1)
        
        self.id_table = {}
        self.id_table["false"] = Id(Tag().FALSE, "false")
        self.id_table["true"] = Id(Tag().TRUE, "true")
        self.token = TokenHandler()
        
    def next_char(self):
        self.peek = self.file.read(1)
        
    def is_space(self):
        if self.peek == "\n":
            self.line += 1
        self.next_char()
        
    def is_digit(self):
        v = 0
        while self.peek.isdigit():
            v = 10 * v + int(self.peek)
            self.next_char()
            
        self.token.n = Num(v)
        return self.token.n
        
    def is_alpha(self):
        s = ''
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
        
    def skip_comments(self):
        self.next_char()
        if self.peek == "/":
            while self.peek != "\n" and self.peek != "":
                self.next_char()
            self.next_char()
            return self.scan()
        else:
            self.token.t = Token("/")
            return self.token.t
        
    def lineno(self):
        return self.line
        
    def scan(self):
        while self.peek.isspace():
            self.is_space()
            
        if self.peek.isdigit():
            return self.is_digit()
            
        elif self.peek.isalpha():
            return self.is_alpha()
            
        elif self.peek == "/":
            return self.skip_comments()
                
        elif self.peek == '':
            return Token(Tag().EOF)
        
        else:
            symbol = Token(self.peek)
            peek = ' '
            self.next_char()
            self.token.t = symbol
            return self.token.t

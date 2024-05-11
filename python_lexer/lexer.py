class Tag:
    def __init__(self):
        self.ID = "ID"
        self.NUM = "NUM"
        self.TRUE = "TRUE"
        self.FALSE = "FALSE"

class Token:
    def __init__(self, tag):
        self.tag = tag

class Id(Token):
    def __init__(self, tag, name):
        self.tag = tag
        self.name = name
        super().__init__(self.tag)

class Num(Token):
    def __init__(self, value):
        self.value = value
        self.tag = Tag().NUM
        super().__init__(self.tag)

class Lexer:
    def __init__(self, source):

        self.source_code = source
        self.index = 0

        self.line = 1
        self.peek = self.source_code[self.index]

        self.id_table = {}
        self.id_table["false"] = Id(Tag().FALSE, "false")
        self.id_table["true"] = Id(Tag().TRUE, "true")

    def next_char(self):
        if len(self.source_code) > (self.index + 1):
            self.index += 1
            self.peek = self.source_code[self.index]
        else:
            self.peek = " "

    def scan(self):
        while self.peek.isspace():
            if self.peek == "\n":
                self.line += 1
            self.next_char()

        if self.peek.isdigit():
            v = 0
            n = int(self.peek)
            v = 10 * v + n
            self.next_char()

            while self.peek.isdigit():
                n = int(self.peek)
                v = 10 * v + n
                self.next_char()

            # DEBUG
            print(f"<NUM, {v}>")

            return Num(v)
        
        if self.peek.isalpha():
            s = self.peek
            self.next_char()

            while self.peek.isalpha():
                s += self.peek
                self.next_char()

            value = self.id_table.get(s)

            if value is not None:

                # DEBUG
                if s == "false":
                    print(f"<FALSE, {value.name}>")
                elif s == "true":
                    print(f"<TRUE, {value.name}>")
                else:
                    print(f"<ID, {value.name}>")

                return value

            new_id = Id(Tag().ID, s)
            self.id_table[s] = new_id

            # DEBUG
            print(f"<ID, {new_id.name}>")

            return new_id
        

        t = Token(self.peek)
        peek = ' '

        # DEBUG
        print(f"<{t.tag}>")

        return t

    def start(self):
        while self.peek != "\n":
            self.scan()


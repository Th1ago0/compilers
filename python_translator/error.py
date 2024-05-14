class SyntaxErro(Exception):
    def __init__(self, line, msg):
        self.lineno = line
        self.desc = msg

    def show(self):
        print(f"Error (line {self.lineno}): {self.desc}")


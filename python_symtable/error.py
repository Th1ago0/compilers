class SyntaxError(Exception):
    def __init__(self, line, msg):
        self.lineno = line
        self.desc = msg
    def show(self):
        print(f"\nErro de Sintaxe (linha {self.lineno}): {self.desc}", end="")

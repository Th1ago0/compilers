from lexer import *
from error import *
from symtable import *
import pdb


class Parser:
    def __init__(self):
        self.scanner = Lexer("file.llds")
        self.symtable = Symtable()
        self.lookahead = self.scanner.scan()
            
    def program(self):
        # program -> block
        self.block()
        
    def block(self):
        # block -> { decls stmts }
        if not self.match("{"):
            raise SyntaxError(self.scanner.lineno(), "\'{\' Esperado.")
        else:
            print("{", end="")
        
        saved_st = self.symtable
        self.symtable = Symtable(saved_st)
        
        self.decls()
        self.stmts()
        
        if not self.match("}"):
            raise SyntaxError(self.scanner.lineno(), "\'}\' Esperado.")
        else:
            print("}", end="")
        
        self.symtable = saved_st
        del saved_st
        
    def decls(self):
        # decls -> decl decls
        #       | empty
        # decl -> type id;
        #pdb.set_trace()
        while self.lookahead.tag == Tag().TYPE:
            type = self.lookahead.str()
            self.match(Tag().TYPE)
            
            name = self.lookahead.str()
            self.match(Tag().ID)
            
            symb = Symbol(name, type)
            
            if not self.symtable.insert(name, symb):
                raise SyntaxError(self.scanner.lineno(), f"Variável \'{name}\' já definida.")
                
            if not self.match(";"):
                raise SyntaxError(self.scanner.lineno(), f"Encontrou \'{self.lookahead.str()}\' invés de \';\'.")
        
    def stmts(self):
        # stmts -> stmt stmts
        #       | empty
        # stmt -> block
        #       | fact;
        #pdb.set_trace()
        while True:
            if self.lookahead.tag == "{":
                self.block()
            elif self.lookahead.tag == Tag().ID:
                self.fact()
                if not self.match(";"):
                    raise SyntaxError(self.scanner.lineno(), f"Encontrou \'{self.lookahead.str()}\' invés de \';\'.")
            else:
                return
            
    def fact(self):
        # facf -> id
        if self.lookahead.tag == Tag().ID:
            s = self.symtable.find(self.lookahead.str())
            
            if not s:
                raise SyntaxError(self.scanner.lineno(), f"A variável \'{self.lookahead.str()}\' não foi declarada.")
            print(f" {s.var}:{s.type}; ", end="")
            self.match(Tag().ID)
        else:
            raise SyntaxError(self.scanner.lineno(), f"\'{self.lookahead.str()}\' não é válido.")
        
    def match(self, tag):
        if self.lookahead.tag == tag:
            self.lookahead = self.scanner.scan()
            return True
        return False
                
    def start(self):
        self.program()

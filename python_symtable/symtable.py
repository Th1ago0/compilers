class Symbol:
    def __init__(self, var, type):
        self.var = var
        self.type = type

class Symtable:
    def __init__(self, prev_table=None):
        self.table = {}
        self.prev = prev_table

    def insert(self, s, symb):
        if s in self.table:
            return False
        else:
            self.table[s] = symb
            return True

    def find(self, s):
        st = self
        while st is not None:
            value = st.table.get(s)
            if value is not None:
                return value
            st = st.prev
        return None

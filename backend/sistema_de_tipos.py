##################################
# Cristopher Barrios
# COMPILADORES 
##################################
# sistema_de_tipos.py
##################################
DEFAULT_TYPES = {
    'int': 4,
    'boolean': 4,
    'char': 4,
}
class Scope:
    """Clase para el manejo de scope general
    """
    def __init__(self, id = None,  name = None, parent = None, type = None):
        self.id = id
        self.type = type
        self.name = name
        self.instantiables = []
        self.symbols = []
        self.parent = parent
    
    def get_instance(self, name):
        for instance in self.instantiables:
            if instance.name == name:
                return instance
    
    def add_instantiable(self, id, name, type, ret = None, subs = [], size = 0):
        instan = Instantiable(id, name, type, ret, subs, size)
        self.instantiables.append(instan)
    
    def get_symbol(self, name):
        for symbol in self.symbols:
            if symbol.name == name:
                return symbol

    def add_symbol(self, type, name, reps, id = 0, offset = 0):
        symbol = Symbols(type, name, reps, id, offset)
        self.symbols.append(symbol)
    
    def get_subattribute(self, instance_name, sub_name):
        for instance in self.instantiables:
            if instance.name == instance_name:
                for sub in instance.sub_attributes:
                    if sub.name == sub_name:
                        return sub
        return None
    
    def get_instance_size(self, instance_name):
        for instance in self.instantiables:
            if instance.name == instance_name:
                return instance.size
        else:
            return self.parent.get_instance_size(instance_name)

    def get_subattribute_offset(self, instance_name):
        for instance in self.instantiables:
            if instance.name == instance_name:
                return 0

    def get_size(self):
        size = 0
        for instance in self.symbols:
            if instance.type  in DEFAULT_TYPES:
                size += DEFAULT_TYPES[instance.type] * int(instance.reps)
            else:
                if lsize:= self.get_instance(instance.type) != None:
                    size += lsize.size * int(instance.reps)
                else:
                    lsize = self.parent.get_instance(instance.type.replace("struct", ""))
                    size += lsize.size * int(instance.reps)
        return size

    def get_structs(self):
        str_arr = []
        for inst in self.instantiables:
            if 'struct' in inst.type:
                str_arr.append(inst)
        return str_arr


class Instantiable:
    """Clase para instancias como los structs
    """
    def __init__ (self, id = 0, name = None, type = None, ret = None, subs = [], size = 0 ):
        self.id = id
        self.name = name
        if type == "struct":
            self.type = type
            self.size = size
            self.sub_attributes = subs
        else:
            self.type = type
            self.ret = ret
            self.params = subs

    def get_sub_attributes(self):
        return self.sub_attributes
    

class Symbols:
    """Clase para los simbolos del programa
    """
    def __init__ (self, type, name, reps, id = 0, offset = 0):
        self.id = id
        self.name = name
        self.type = type
        self.offset = offset
        self.reps = reps

class Error:
    "Clase para errores"
    def __init__ (self, problem, line, columns, msg = ""):
        self.problem = problem
        self.line = line
        self.column = columns
        if msg != "":
            self.msg =  msg





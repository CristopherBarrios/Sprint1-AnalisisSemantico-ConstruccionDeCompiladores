from symbol import namedexpr_test


DEFAULT_TYPES = {
    'Int': 4,
    'boolean': 4,
    'String': 4,
}

class Clase:
    """Clase para el manejo de clases jaja
    """
    def __init__(self,name,parent,scope_ids,params):
        self.name = name
        self.parent = parent
        self.scope_ids = scope_ids
        self.params = params

    def get_symbol(self, name):
        for p in self.params:
            if "name" in dir(p):
                if p.name == name:
                    if p.expr != None:
                        if "id" in dir(p.expr):
                            return p.expr.id
                    else:
                        return p.type

    def get_instance(self,name):
        if self.name == name:
            return self.name

    def get_size(self):
        size = 0
        for instance in self.params:
            if instance.type in DEFAULT_TYPES:
                size += DEFAULT_TYPES[instance.type]
        return size


    def get_clase_values(self):
        print("Clase: " + self.name + "  Inherits: " + str(self.parent) + "  Scope_ids: " + str(self.scope_ids) + "  Params: " + str(self.params))



class Method:
    """Clase para el manejo de metodos
    """
    def __init__(self,name,id,type,formalParams,expr):
        self.name = name
        self.id = id
        self.type = type
        self.formalParams = formalParams
        self.expr = expr

    def get_symbol(self, name):
        for p in self.formalParams:
            if p.name == name:
                return p.type

        #for exp in dir(self.expr)[::-1]:
        if 'parenth' in dir(self.expr):
            if self.expr.parenth.name.name == name:
                return self.expr.parenth.name.type
        


    def get_size(self):
        size = 0
        for instance in self.formalParams:
            if instance.type in DEFAULT_TYPES:
                size += DEFAULT_TYPES[instance.type]
        return size
    

    def get_instance(self, name):
        if self.name == name:
            return self.name


    def get_method_values(self):
        print("Metodo: " + self.name + "  ID: " + str(self.id) + "  Type: " + str(self.type) + "  Params: " + str(self.formalParams) + "  Expr: " + str(self.expr))



class OwnMethod:
    """Clase para el manejo
    """
    def __init__(self,method,argumen):
        self.method = method
        self.argumen = argumen
    

    def get_omethod_values(self):
        print("Metodo: " + self.method + "  argumen: " + str(self.argumen))



class Property:
    """Clase para el manejo de propiedades
    """
    def __init__(self,name,type,expr):
        self.name = name
        self.type = type
        self.expr = expr

    def get_property_name(self, name):
        if name == self.name:
            return self.name
    def get_expression(self): return self.expr

    def get_property_values(self):
        print("Property: " + str(self.name) + "  tipo: " + str(self.type) + "  expr: " + str(self.expr))



class Formal:
    """Clase para el manejo de Formal
    """
    def __init__(self,name,type):
        self.name = name
        self.type = type


    def get_formal_values(self):
        print("Formal: " + str(self.name) + "  tipo: " + str(self.type))



class Assignment:
    def __init__(self,name,expr):
        self.name = name
        self.expr = expr


    def get_assignment_values(self):
        print("Assignment: " + str(self.name) + "  expr: " + str(self.expr))



class MethodCall:
    def __init__(self,name,type,expr,expr1,expr2):
        self.name = name
        self.type = type
        self.expr = expr
        self.expr1 = expr1
        self.expr2 = expr2


    def get_methodcall_values(self):
        print("MethodCall: " + str(self.name) + "  type: " + str(self.type) + "  expr: " + str(self.expr) + "  expr1: " + str(self.expr1) + "  expr2: " + str(self.expr2))


class IfCount:
    def __init__(self,exprIf,exprThen,exprElse):
        self.exprIf = exprIf
        self.exprThen = exprThen
        self.exprElse = exprElse

    def get_ifcount_values(self):
        print("If: " + str(self.exprIf) + "  Then: " + str(self.exprThen) + "  Else: " + str(self.exprElse))

class Case:
    def __init__(self,exprCase,name,type,exprCaseArrow):
        self.exprCase = exprCase
        self.name = name
        self.type = type
        self.exprCaseArrow = exprCaseArrow

    def get_case_values(self):
        print("Case: " + str(self.exprCase) + "  name: " + str(self.name) + "  type: " + str(self.type) + "  arrow: " + str(self.exprCaseArrow))

class Decla:
    def __init__(self,name,type,expr):
        self.name = name
        self.type = type
        self.expr = expr

    def get_decla_values(self):
        print("Declaration: " + str(self.name) + "  type: " + str(self.type) + " expr: " + str(self.expr))

class LetIn:
    def __init__(self,let,let1,expr):
        self.name = let
        self.type = let1
        self.expr = expr

    def get_letin_values(self):
        print("Name: " + str(self.name) + "  type: " + str(self.type) + "  expr: " + str(self.expr))

class WhileCount:
    def __init__(self,expWhile,expLoop):
        self.expWhile = expWhile
        self.expLoop = expLoop
    
    def get_whilecount_values(self):
        print("While:" + str(self.expWhile) + "  Loop: " + str(self.expLoop))

class Equal:
    def __init__(self,Le,Ri):
        self.left = Le
        self.right = Ri
    
    def get_equal_values(self):
        print("Left: " + str(self.left) + "  Right: " + str(self.right))

class LessEqual:
    def __init__(self,Le,Ri):
        self.left = Le
        self.right = Ri

    def get_lessequal_values(self):
        print("Left: " + str(self.left) + "  Right: " + str(self.right))

class LessThan:
    def __init__(self,Le,Ri):
        self.left = Le
        self.right = Ri

    def get_lessthan_values(self):
        print("Left: " + str(self.left) + "  Right: " + str(self.right))

class Minus:
    def __init__(self,Le,Ri):
        self.left = Le
        self.right = Ri

    def get_minus_values(self):
        print("Left: " + str(self.left) + "  Right: " + str(self.right))

class Add:
    def __init__(self,Le,Ri):
        self.left = Le
        self.right = Ri

    def get_add_values(self):
        print("Left: " + str(self.left) + "  Right: " + str(self.right))

class Division:
    def __init__(self,Le,Ri):
        self.left = Le
        self.right = Ri

    def get_division_values(self):
        print("Left: " + str(self.left) + "  Right: " + str(self.right))

class Multiply:
    def __init__(self,Le,Ri):
        self.left = Le
        self.right = Ri

    def get_multiply_values(self):
        print("Left: " + str(self.left) + "  Right: " + str(self.right))

class Isvoid:
    def __init__(self,vo):
        self.vo = vo

    def get_idvoid_values(self):
        print("Isvoid: " + str(self.vo))

class Negative:
    def __init__(self,ne):
        self.ne = ne
    
    def get_negative_values(self):
        print("Negative: " + str(self.ne))

class BoolNot:
    def __init__(self,bn):
        self.bn = bn

    def get_boolnot_values(self):
        print("Boolnot: " + str(self.bn))

class New:
    def __init__(self,type):
        self.type = type

    def get_new_values(self):
        print("New: " + str(self.type))

class String:
    def __init__(self,str, strval, valores):
        self.str = str
        self.strval = strval
        self.valores = valores
    
    def get_string_values(self):
        print("String: " + str(self.str) + "  striLoop: " + str(self.strval) + "  Valores: " + str(self.valores))

class Valus:
    def __init__(self,valor,indice):
        self.valor = valor
        self.indice = indice

    def get_valus_values(self):
        print("Value: " + str(self.valor) + "  Indice: " + str(self.indice))
        
class Block:
    def __init__(self,bloc):
        self.bloc = bloc

    def get_block_values(self):
        print("Block" + str(self.bloc))

class Id:
    def __init__(self,id):
        self.id = id

    def get_id_values(self):
        print("Id: " + str(self.id))

class Parentheses:
    def __init__(self,parenth):
        self.parenth = parenth

    def get_parentheses_values(self):
        print("Parentheses: " + str(self.parenth))

class FalseCount:
    def __init__(self,falsef):
        self.falsef = falsef

    def get_falsecount_values(self):
        print("False: " + str(self.falsef))

class Int:
    def __init__(self,id):
        self.id = id
    
    def get_int_values(self):
        print("Int: " + str(self.id))

class TrueCount:
    def __init__(self,id):
        self.id = id
    
    def get_truecoutn_values(self):
        print("TrueCount: " + str(self.id))

class In:
    def __init__(self,method):
        self.method = method

    def get_In_values(self):
        print("In: " + str(self.method))

class OutString:
    def __init__(self,outstring, expr1 = None, expr2 = None):
        self.outstring = outstring
        self.expr1 = expr1
        self.expr2 = expr2 

    def get_outstring_values(self):
        print("Outstring: " + str(self.outstring) + "  expr1: " + str(self.expr1) + "  expr2: "+ str(self.expr2))

class OutInt:
    def __init__(self,outint, expr1 = None, expr2 = None):
        self.outint = outint
        self.expr1 = expr1
        self.expr2 = expr2 

    def get_outint_values(self):
        print("Outstring: " + str(self.outint) + "  expr1: " + str(self.expr1) + "  expr2: "+ str(self.expr2))
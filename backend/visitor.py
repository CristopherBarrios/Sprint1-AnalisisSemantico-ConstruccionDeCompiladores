##################################
# Cristopher Barrios
# COMPILADORES 
##################################
# visitor.py
##################################
import backend.sistema_de_tipos as tables
import backend.classes as lista
from YAPL.YAPLVisitor import YAPLVisitor
from YAPL.YAPLParser import YAPLParser
from backend.functions import *


class MyYAPLVisitor(YAPLVisitor):
    def __init__(self, table):
        YAPLVisitor.__init__(self)
        self.ERRORS = []

        self.class_ids = -1
        self.method_ids = -1
        self.symbols_ids = 0
        self.offset = 0
        self.instantiable_ids = 0
        global_scope = tables.Scope()
        self.actual_scope = 'Global'
        self.method_scope = ''
        self.cont_lets = 0
        self.let_scope = []
        self.scopes = []
        self.variables = []
        self.table = table
        self.reservado = ['Object']
        self.palabras = ['self']
        self.valoresTipos = ['String','Bool','Int']

        self.clases = []
        self.metodos = []
        self.ownmethod = []
        self.property = []
        self.formal = []
        self.assignment = []
        self.methodcall = []
        self.ifCount = []
        self.equal = []
        self.lessequal = []
        self.lessthan = []
        self.minus = []
        self.add = []
        self.division = []
        self.multiply = []
        self.whileCount = []
        self.declaration = []
        self.letin = []
        self.void = []
        self.negative = []
        self.boolnot = []
        self.case = []
        self.new = []
        self.string = []
        self.valor = []
        self.block = []
        self.id = []
        self.parentheses = []
        self.fals = []
        self.integer = []
        self.truet = []
        self.instr = []
        self.outstring = []
        self.outint = []

        self.total_scopes = {}
        self.printidorClases = {}

    def visitStart(self, ctx):
        # self.ERRORS = []
        # self.visitChildren(ctx)

        contador = []
        for clas in self.clases:
            contador.append(clas.get_instance("Main"))
        if "Main" not in contador:
            new_error = tables.Error("Main class not defined", ctx.start.line, ctx.start.column)
            self.ERRORS.append(new_error)

        if len(self.clases) != 0:
            for x in self.clases:
                self.total_scopes[x.name] = x
            for y in self.metodos:
                self.total_scopes[y.name] = y

        if "Main" in contador:
            contador = []
            for meto in self.total_scopes["Main"].params:
                if "id" in dir(meto):
                    contador.append(meto.get_instance("main"))
            if "main" not in contador:
                new_error = tables.Error("main method not defined", ctx.start.line, ctx.start.column)
                self.ERRORS.append(new_error)

        if "main" in contador:
            contador = []
            if "bloc" in dir(self.total_scopes["main"].expr): 
                for corredor in self.total_scopes["main"].expr.bloc:
                    if "expr" in dir(corredor) and "expr1" in dir(corredor) and "expr2" in dir(corredor) and "name" in dir(corredor) and "type" in dir(corredor):
                        contador.append(corredor.name)
                if "main" not in contador:
                    new_error = tables.Error("No se encuentra (new Main).main(); en main", ctx.start.line, ctx.start.column)
                    self.ERRORS.append(new_error)
            else:
                new_error = tables.Error("No se encuentra { } en main", ctx.start.line, ctx.start.column)
                self.ERRORS.append(new_error)

        classsss = []
        for scopeClass in self.clases:
            classsss.append(scopeClass.name)
            n = buscar_n_elemento(self.total_scopes, scopeClass.name)
            if n > 1:
                new_error = tables.Error("Hay clases repetidas", ctx.start.line, ctx.start.column)
                self.ERRORS.append(new_error)

        for scopeMetodo in self.metodos:
            n = buscar_n_elemento(self.total_scopes, scopeMetodo.name)
            if n > 1:
                new_error = tables.Error("Hay metodos repetidos", ctx.start.line, ctx.start.column)
                self.ERRORS.append(new_error)

            #verifica si hereda bien los metodos
            if scopeMetodo.type not in classsss and scopeMetodo.type != "Int" and scopeMetodo.type != "SELF_TYPE" and scopeMetodo.type != "Bool" and scopeMetodo.type != "String" and scopeMetodo.type != "Object":
                if scopeMetodo.type not in classsss:
                    new_error = tables.Error("No hay ninguna clase llamada asi", ctx.start.line, ctx.start.column)
                    self.ERRORS.append(new_error)
                else:
                    new_error = tables.Error("No hay ninguna metodo exclusivo", ctx.start.line, ctx.start.column)
                    self.ERRORS.append(new_error)

        #verifica si hereda bien las clases
        for scopeClass in self.clases:
            if scopeClass.parent not in classsss and scopeClass.parent != "IO" and scopeClass.parent != None:
                    new_error = tables.Error("No hay ninguna clase que se pueda heredar", ctx.start.line, ctx.start.column)
                    self.ERRORS.append(new_error) 

        #imprime todos los datos
        #printidor(self.clases,self.metodos,self.ownmethod,self.property,self.formal,self.assignment,self.methodcall,self.ifCount,self.equal,self.lessequal,self.lessthan,self.minus,self.add,self.division,self.multiply,self.whileCount,self.declaration,self.letin,self.void,self.negative,self.boolnot,self.case,self.new,self.string,self.valor,self.block,self.id,self.parentheses,self.fals,self.integer,self.truet,self.instr,self.outstring,self.outint)

        return 0


    def visitClass_list(self, ctx):
        class_list = [self.visit(ctx.class_exp())]
        programB = self.visit(ctx.program())

 
    def visitEnd(self, ctx):
        self.visitStart(ctx)


    def visitClass_exp(self, ctx):
        class_name = ctx.TYPE(0).getText()
        self.class_ids += 1
        self.actual_scope = class_name

        parent = None
        if len(ctx.TYPE()) > 1:
            parent = ctx.TYPE(1).getText()

        features = []
        propertyCount = 0
        for f in ctx.feature():
            feature = self.visit(f)
            features.append(feature)
            if type(feature).__name__ == 'Property':
                propertyCount += 1
                self.variables.append(feature)

        for met in self.clases:
            if class_name == met.name:
                new_error = tables.Error("Ya se ha declarado esta clase " + str(class_name), ctx.start.line, ctx.start.column)
                self.ERRORS.append(new_error)

        clase = lista.Clase(class_name,parent,self.class_ids,features)
        self.clases.append(clase)
        self.actual_scope = 'Global'

        if propertyCount != 0:
            self.variables = eliminar_ultimos_elementos(self.variables, propertyCount)

        if ctx.INHERITS():
            if class_name == "Main":
                if parent != "IO":
                    new_error = tables.Error("La clase Main no puede heredar de ninguna otra clase ", ctx.start.line, ctx.start.column)
                    self.ERRORS.append(new_error)
            if class_name == parent:
                    new_error = tables.Error("La clase no puede heredar de la misma clase ", ctx.start.line, ctx.start.column)
                    self.ERRORS.append(new_error)
            if parent == "Int" or parent == "String" or parent == "Bool":
                    new_error = tables.Error("La clase no puede heredar un Int, String o Bool ", ctx.start.line, ctx.start.column)
                    self.ERRORS.append(new_error)
        return clase


    def visitMethod(self, ctx):
        name = ctx.ID().getText()
        tipo = None;expr=None

        self.method_scope = name
        if ctx.TYPE():
            tipo = ctx.TYPE().getText()
        self.method_ids += 1

        for meto in self.metodos:
            if name == meto.name:
                self.method_ids -= 1
                #return 0

        formalParams = []
        formalCont = 0
        for f in ctx.formal():
            formalCont += 1
            formalParam = self.visit(f)
            formalParams.append(formalParam)
            self.variables.append(formalParam)

        if ctx.expr():
            expr = self.visit(ctx.expr())

        if type(expr).__name__ == 'Id':
            if expr.id != "self":
                id  = verificaThor(expr.id,self.variables)
                if id is None:
                    new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,expr.id)
                    self.ERRORS.append(new_error)  

        elif type(expr).__name__ == 'Block':
            for obj in expr.bloc:
                if type(obj).__name__ == 'Id':
                    if obj.id != "self":
                        id  = verificaThor(obj.id,self.variables)
                        if id is None:
                            new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,obj.id)
                            self.ERRORS.append(new_error)  

        metodo = lista.Method(name,self.method_ids,tipo,formalParams,expr)
        self.metodos.append(metodo)
        self.method_scope = ''

        if formalCont != 0:
            self.variables = eliminar_ultimos_elementos(self.variables, formalCont)

        if name == "main":
            if ctx.formal():
                new_error = tables.Error("El metodo main no puede contener parametros formales ", ctx.start.line, ctx.start.column)
                self.ERRORS.append(new_error)              

        if name == tipo or tipo == None:
            new_error = tables.Error("No se puede encontrar type en metodo ", ctx.start.line, ctx.start.column)
            self.ERRORS.append(new_error)

        return metodo


    def visitAttribute(self, ctx):
        what = ctx.getChild(0)
        name = ctx.ID().getText()
        tipo = ctx.TYPE().getText()
        type2 = ctx.getText()

        if tipo not in self.valoresTipos:
            id = encontradorClases(tipo,self.table)
            if id is None:
                new_error = tables.Error("No se declaro el tipo o clase", ctx.start.line, ctx.start.column,ctx.TYPE().getText())
                self.ERRORS.append(new_error)  

        if ctx.ASSIGNMENT() is None:
            propiedad = lista.Property(name,tipo,None)
            self.property.append(propiedad)
            return propiedad

        expr = self.visit(ctx.expr())

        if tipo in self.valoresTipos:
            if type(expr).__name__ == 'Block':
                for obj in expr.bloc:
                    if type(obj).__name__ == 'Id':
                        if obj.id not in self.palabras:
                            id  = verificaThor(obj.id,self.variables)
                            if id is None:
                                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,obj.id)
                                self.ERRORS.append(new_error)

                    elif type(obj).__name__ == 'Int' or type(obj).__name__ == 'String':
                        if  tipo != type(obj).__name__:
                            new_error = tables.Error("No corresponden los tipos de la asignacion", ctx.start.line, ctx.start.column,tipo)
                            self.ERRORS.append(new_error)
                    elif type(obj).__name__ == 'TrueCount' or type(obj).__name__ == 'FalseCount':
                        if  tipo != 'Bool':
                            new_error = tables.Error("No corresponden los tipos de la asignacion", ctx.start.line, ctx.start.column,tipo)
                            self.ERRORS.append(new_error)  
            else:
                if type(expr).__name__ == 'Id':
                    if expr.id not in self.palabras:
                        id  = verificaThor(expr.id,self.variables)
                        if id is None:
                            new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,expr.id)
                            self.ERRORS.append(new_error)
                        else:
                            if  tipo != id.type:
                                new_error = tables.Error("No corresponden los tipos de la asignacion", ctx.start.line, ctx.start.column,tipo)
                                self.ERRORS.append(new_error)
                elif type(expr).__name__ == 'String' or type(expr).__name__ == 'Int':
                    if  tipo != type(expr).__name__:
                        new_error = tables.Error("No corresponden los tipos de la asignacion", ctx.start.line, ctx.start.column,tipo)
                        self.ERRORS.append(new_error)
                elif type(expr).__name__ == 'TrueCount' or type(expr).__name__ == 'FalseCount':
                    if  tipo != 'Bool':
                        new_error = tables.Error("No corresponden los tipos de la asignacion", ctx.start.line, ctx.start.column,tipo)
                        self.ERRORS.append(new_error)    

                elif type(expr).__name__ == "Add" or type(expr).__name__ == "Division" or type(expr).__name__ == "Multiply" or type(expr).__name__ == "Minus":
                    if tipo != 'Int':
                        new_error = tables.Error("No corresponden los tipos de la asignacion", ctx.start.line, ctx.start.column,tipo)
                        self.ERRORS.append(new_error)

        propiedad = lista.Property(name,tipo,expr)
        self.property.append(propiedad)
        return propiedad


    def visitFormal(self, ctx):
        name = ctx.ID().getText()
        type = ctx.TYPE().getText()

        formal = lista.Formal(name,type)
        self.formal.append(formal)

        return formal


    def visitDeclaration(self, ctx):
        name = ctx.ID().getText()
        type = ctx.TYPE().getText()

        if ctx.ASSIGNMENT() is None:
            declaration = lista.Decla(name,type,None)
            self.declaration.append(declaration)
            return declaration

        expr = self.visit(ctx.expr())

        declaration = lista.Decla(name,type,expr)
        self.declaration.append(declaration)
        return declaration


    def visitAssignment(self, ctx):
        name = ctx.ID().getText()
        expr = self.visit(ctx.expr())

        id  = verificaThor(ctx.ID().getText(),self.variables)
        if id is None:
            new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.ID().getText())
            self.ERRORS.append(new_error) 

        assignement = lista.Assignment(name,expr)
        self.assignment.append(assignement)

        return assignement


    def visitLetIn(self, ctx):
        declaCont = 0
        let = self.visit(ctx.declaration(0))
        declaCont += 1
        self.variables.append(let)
        self.cont_lets += 1
        self.let_scope.append('let' + str(self.cont_lets))
        let1 = None

        if ctx.declaration(1) is not None:
            declaCont += 1
            let1 = self.visit(ctx.declaration(1))
            self.variables.append(let1)
        expr = self.visit(ctx.expr())

        letin = lista.LetIn(let,let1,expr)
        self.letin.append(letin)
        self.let_scope.pop()
        if declaCont != 0:
            self.variables = eliminar_ultimos_elementos(self.variables, declaCont)

        return letin


    def visitWhile(self, ctx):
        expWhile = self.visit(ctx.expr(0))
        expLoop = self.visit(ctx.expr(1))

        if type(expWhile).__name__ == "Add" or type(expWhile).__name__ == "Division" or type(expWhile).__name__ == "Multiply" or type(expWhile).__name__ == "Minus":
            new_error = tables.Error("While tiene que ser booleano", ctx.start.line, ctx.start.column)
            self.ERRORS.append(new_error)

        whileCount = lista.WhileCount(expWhile,expLoop)
        self.whileCount.append(whileCount)

        return whileCount
    

    def visitIf(self, ctx):
        exprIf = self.visit(ctx.expr(0))
        exprThen = self.visit(ctx.expr(1))
        exprElse = self.visit(ctx.expr(2))

        if type(exprIf).__name__ == "Add" or type(exprIf).__name__ == "Division" or type(exprIf).__name__ == "Multiply" or type(exprIf).__name__ == "Minus":
            new_error = tables.Error("If tiene que ser booleano", ctx.start.line, ctx.start.column)
            self.ERRORS.append(new_error)
            
        ifcount = lista.IfCount(exprIf,exprThen,exprElse)
        self.ifCount.append(ifcount)

        return ifcount
    

    def visitCase(self, ctx):
        exprCase = self.visit(ctx.expr(0))

        Of = []
        for f in ctx.ID():
            name = f.getText()
            Of.append(name)
            
        type = []
        exprCaseArrow = []

        for t in ctx.TYPE():
            name = t.getText()
            type.append(name)

        for i in range(1, len(ctx.expr())):
            exprCaseArrow.append(self.visit(ctx.expr(i)))
        
        case = lista.Case(exprCase,Of,type,exprCaseArrow)
        self.case.append(case)

        return case

 
    def visitLessThan(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))

        if type(r).__name__ == 'Id':
            id  = verificaThor(ctx.expr(1).getText(),self.variables)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                self.ERRORS.append(new_error) 
            else:
                if id.type != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la comparacion", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                    self.ERRORS.append(new_error)   

        if type(l).__name__ == 'Id':
            id  = verificaThor(ctx.expr(0).getText(),self.variables)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                self.ERRORS.append(new_error)
            else:
                if id.type != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la comparacion", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                    self.ERRORS.append(new_error) 

        if type(l).__name__ != type(r).__name__ :
            if type(l).__name__ !=  "Id" and type(r).__name__ !=  "Id":
                new_error = tables.Error("No corresponden los tipos de la comparacion =", ctx.start.line, ctx.start.column,ctx.getText())
                self.ERRORS.append(new_error) 

        lessthan = lista.LessThan(l,r)
        self.lessthan.append(lessthan)

        return lessthan
    
    def visitEqual(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))

        if type(r).__name__ == 'Id':
            id  = verificaThor(ctx.expr(1).getText(),self.variables)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                self.ERRORS.append(new_error) 
            else:
                if id.type != 'Int' and id.type != 'String':
                    new_error = tables.Error("No corresponden los tipos de la comparacion", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                    self.ERRORS.append(new_error)   
                else:
                    if type(l).__name__ != id.type and type(l).__name__ !="Minus" and type(l).__name__ != 'Add' and type(l).__name__ != 'Division' and type(l).__name__ != 'Multiply': 
                        new_error = tables.Error("No corresponden los tipos de la comparacion", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                        self.ERRORS.append(new_error)  

        if type(l).__name__ == 'Id':
            id  = verificaThor(ctx.expr(0).getText(),self.variables)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                self.ERRORS.append(new_error)
            else:
                if id.type != 'Int' and id.type != 'String':
                    new_error = tables.Error("No corresponden los tipos de la comparacion", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                    self.ERRORS.append(new_error)
                else:
                    if type(r).__name__ != id.type and type(r).__name__ !="Minus" and type(r).__name__ != 'Add' and type(r).__name__ != 'Division' and type(r).__name__ != 'Multiply':
                        new_error = tables.Error("No corresponden los tipos de la comparacion", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                        self.ERRORS.append(new_error)  

        if type(r).__name__ == 'OwnMethod':
            id  = encontradorClases(r.method,self.table)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                self.ERRORS.append(new_error)
            else:
                if id['type'] != 'Int' and id['type'] != 'String':
                    new_error = tables.Error("No corresponden los tipos de la comparacion", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                    self.ERRORS.append(new_error) 

        if type(l).__name__ == 'OwnMethod':
            id  = encontradorClases(l.method,self.table)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                self.ERRORS.append(new_error)
            else:
                if id['type'] != 'Int' and id['type'] != 'String':
                    new_error = tables.Error("No corresponden los tipos de la comparacion", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                    self.ERRORS.append(new_error) 

        if type(r).__name__ == 'Add' or type(r).__name__ == 'Minus' or type(r).__name__ == 'Division' or type(r).__name__ == 'Multiply':
            if type(l).__name__ != 'Int':
                new_error = tables.Error("No corresponden los tipos de la comparacion", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                self.ERRORS.append(new_error) 

        if type(l).__name__ == 'Add' or type(l).__name__ == 'Minus' or type(l).__name__ == 'Division' or type(l).__name__ == 'Multiply':
            if type(r).__name__ != 'Int':
                new_error = tables.Error("No corresponden los tipos de la comparacion", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                self.ERRORS.append(new_error) 

        if type(l).__name__ != type(r).__name__ :
            if type(l).__name__ !=  "Id" and type(r).__name__ !=  "Id" and type(l).__name__ != 'OwnMethod'and type(r).__name__ != 'OwnMethod' and type(l).__name__ != 'Add' and type(r).__name__ != 'Add' and type(l).__name__ != 'Minus' and type(r).__name__ != 'Minus' and type(l).__name__ != 'Division' and type(r).__name__ != 'Division' and type(l).__name__ != 'Multiply' and type(r).__name__ != 'Multiply':
                new_error = tables.Error("No corresponden los tipos de la comparacion =", ctx.start.line, ctx.start.column,ctx.getText())
                self.ERRORS.append(new_error)

        equal = lista.Equal(l,r)
        self.equal.append(equal)

        return equal
    

    def visitLessEqual(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))

        if type(r).__name__ == 'Id':
            id  = verificaThor(ctx.expr(1).getText(),self.variables)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                self.ERRORS.append(new_error) 
            else:
                if id.type != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la comparacion", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                    self.ERRORS.append(new_error)   

        if type(l).__name__ == 'Id':
            id  = verificaThor(ctx.expr(0).getText(),self.variables)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                self.ERRORS.append(new_error)
            else:
                if id.type != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la comparacion", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                    self.ERRORS.append(new_error) 

        if type(l).__name__ != type(r).__name__ :
            if type(l).__name__ !=  "Id" and type(r).__name__ !=  "Id":
                new_error = tables.Error("No corresponden los tipos de la comparacion <=", ctx.start.line, ctx.start.column,ctx.getText())
                self.ERRORS.append(new_error) 

        lessequal = lista.LessEqual(l,r)
        self.lessequal.append(lessequal)

        return lessequal
    

    def visitAdd(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))

        if type(r).__name__ == 'Id':
            id  = verificaThor(ctx.expr(1).getText(),self.variables)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                self.ERRORS.append(new_error) 
            else:
                if id.type != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la suma", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                    self.ERRORS.append(new_error)   

        if type(l).__name__ == 'Id':
            id  = verificaThor(ctx.expr(0).getText(),self.variables)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                self.ERRORS.append(new_error)
            else:
                if id.type != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la suma", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                    self.ERRORS.append(new_error)   

        if type(r).__name__ == 'IfCount':
            if type(r.exprThen).__name__ != 'Block':
                if type(r.exprThen).__name__ != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la suma", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                    self.ERRORS.append(new_error)   
            if type(r.exprElse).__name__ != 'Block':
                if type(r.exprElse).__name__ != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la suma", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                    self.ERRORS.append(new_error)

        if type(l).__name__ == 'IfCount':
            if type(l.exprThen).__name__ != 'Block':
                if type(l.exprThen).__name__ != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la suma", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                    self.ERRORS.append(new_error)   
            if type(l.exprElse).__name__ != 'Block':
                if type(l.exprElse).__name__ != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la suma", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                    self.ERRORS.append(new_error)

        if type(r).__name__ == 'OwnMethod':
            id  = encontradorClases(r.method,self.table)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                self.ERRORS.append(new_error)
            else:
                if id['type'] != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la suma", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                    self.ERRORS.append(new_error) 

        if type(l).__name__ == 'OwnMethod':
            id  = encontradorClases(l.method,self.table)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                self.ERRORS.append(new_error)
            else:
                if id['type'] != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la suma", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                    self.ERRORS.append(new_error) 

        if type(l).__name__ !=  "Int" or type(r).__name__ !=  "Int":
            if type(l).__name__ !=  "Id" and type(r).__name__ !=  "Id" and type(l).__name__ != 'IfCount' and type(r).__name__ != 'IfCount' and type(l).__name__ != 'OwnMethod'and type(r).__name__ != 'OwnMethod':
                new_error = tables.Error("No corresponden los tipos de la suma", ctx.start.line, ctx.start.column,ctx.getText())
                self.ERRORS.append(new_error)

        add = lista.Add(l,r)
        self.add.append(add)

        return add


    def visitMinus(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))

        if type(r).__name__ == 'Id':
            id  = verificaThor(ctx.expr(1).getText(),self.variables)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                self.ERRORS.append(new_error) 
            else:
                if id.type != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la resta", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                    self.ERRORS.append(new_error)   

        if type(l).__name__ == 'Id':
            id  = verificaThor(ctx.expr(0).getText(),self.variables)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                self.ERRORS.append(new_error)
            else:
                if id.type != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la resta", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                    self.ERRORS.append(new_error) 

        if type(r).__name__ == 'IfCount':
            if type(r.exprThen).__name__ != 'Block':
                if type(r.exprThen).__name__ != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la resta", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                    self.ERRORS.append(new_error)   
            if type(r.exprElse).__name__ != 'Block':
                if type(r.exprElse).__name__ != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la resta", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                    self.ERRORS.append(new_error)

        if type(l).__name__ == 'IfCount':
            if type(l.exprThen).__name__ != 'Block':
                if type(l.exprThen).__name__ != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la resta", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                    self.ERRORS.append(new_error)   
            if type(l.exprElse).__name__ != 'Block':
                if type(l.exprElse).__name__ != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la resta", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                    self.ERRORS.append(new_error)

        if type(r).__name__ == 'OwnMethod':
            id  = encontradorClases(r.method,self.table)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                self.ERRORS.append(new_error)
            else:
                if id['type'] != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la resta", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                    self.ERRORS.append(new_error) 

        if type(l).__name__ == 'OwnMethod':
            id  = encontradorClases(l.method,self.table)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                self.ERRORS.append(new_error)
            else:
                if id['type'] != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la resta", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                    self.ERRORS.append(new_error) 

        if type(l).__name__ !=  "Int" or type(r).__name__ !=  "Int":
            if type(l).__name__ !=  "Id" and type(r).__name__ !=  "Id" and type(l).__name__ != 'IfCount' and type(r).__name__ != 'IfCount' and type(l).__name__ != 'OwnMethod'and type(r).__name__ != 'OwnMethod':
                new_error = tables.Error("No corresponden los tipos de la resta", ctx.start.line, ctx.start.column,ctx.getText())
                self.ERRORS.append(new_error)
        
        minus = lista.Minus(l,r)
        self.minus.append(minus)
        
        return minus
    

    def visitDivision(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))

        if type(r).__name__ == 'Id':
            id  = verificaThor(ctx.expr(1).getText(),self.variables)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                self.ERRORS.append(new_error) 
            else:
                if id.type != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la division", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                    self.ERRORS.append(new_error)   

        if type(l).__name__ == 'Id':
            id  = verificaThor(ctx.expr(0).getText(),self.variables)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                self.ERRORS.append(new_error)
            else:
                if id.type != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la division", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                    self.ERRORS.append(new_error) 

        if type(r).__name__ == 'IfCount':
            if type(r.exprThen).__name__ != 'Block':
                if type(r.exprThen).__name__ != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la division", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                    self.ERRORS.append(new_error)   
            if type(r.exprElse).__name__ != 'Block':
                if type(r.exprElse).__name__ != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la division", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                    self.ERRORS.append(new_error)

        if type(l).__name__ == 'IfCount':
            if type(l.exprThen).__name__ != 'Block':
                if type(l.exprThen).__name__ != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la division", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                    self.ERRORS.append(new_error)   
            if type(l.exprElse).__name__ != 'Block':
                if type(l.exprElse).__name__ != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la division", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                    self.ERRORS.append(new_error)

        if type(r).__name__ == 'OwnMethod':
            id  = encontradorClases(r.method,self.table)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                self.ERRORS.append(new_error)
            else:
                if id['type'] != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la division", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                    self.ERRORS.append(new_error) 

        if type(l).__name__ == 'OwnMethod':
            id  = encontradorClases(l.method,self.table)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                self.ERRORS.append(new_error)
            else:
                if id['type'] != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la division", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                    self.ERRORS.append(new_error) 

        if type(l).__name__ !=  "Int" or type(r).__name__ !=  "Int":
            if type(l).__name__ !=  "Id" and type(r).__name__ !=  "Id" and type(l).__name__ != 'IfCount' and type(r).__name__ != 'IfCount' and type(l).__name__ != 'OwnMethod'and type(r).__name__ != 'OwnMethod':
                new_error = tables.Error("No corresponden los tipos de la division", ctx.start.line, ctx.start.column,ctx.getText())
                self.ERRORS.append(new_error) 

        division = lista.Division(l,r)
        self.division.append(division)

        return division


    def visitStar(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))
     
        if type(r).__name__ == 'Id':
            id  = verificaThor(ctx.expr(1).getText(),self.variables)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                self.ERRORS.append(new_error) 
            else:
                if id.type != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la multiplicacion", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                    self.ERRORS.append(new_error)   

        if type(l).__name__ == 'Id':
            id  = verificaThor(ctx.expr(0).getText(),self.variables)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                self.ERRORS.append(new_error)
            else:
                if id.type != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la multiplicacion", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                    self.ERRORS.append(new_error)

        if type(r).__name__ == 'IfCount':
            if type(r.exprThen).__name__ != 'Block':
                if type(r.exprThen).__name__ != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la multiplicacion", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                    self.ERRORS.append(new_error)   
            if type(r.exprElse).__name__ != 'Block':
                if type(r.exprElse).__name__ != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la multiplicacion", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                    self.ERRORS.append(new_error)

        if type(l).__name__ == 'IfCount':
            if type(l.exprThen).__name__ != 'Block':
                if type(l.exprThen).__name__ != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la multiplicacion", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                    self.ERRORS.append(new_error)   
            if type(l.exprElse).__name__ != 'Block':
                if type(l.exprElse).__name__ != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la multiplicacion", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                    self.ERRORS.append(new_error)

        if type(r).__name__ == 'OwnMethod':
            id  = encontradorClases(r.method,self.table)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                self.ERRORS.append(new_error)
            else:
                if id['type'] != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la multiplicacion", ctx.start.line, ctx.start.column,ctx.expr(1).getText())
                    self.ERRORS.append(new_error) 

        if type(l).__name__ == 'OwnMethod':
            id  = encontradorClases(l.method,self.table)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                self.ERRORS.append(new_error)
            else:
                if id['type'] != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la multiplicacion", ctx.start.line, ctx.start.column,ctx.expr(0).getText())
                    self.ERRORS.append(new_error) 

        if type(l).__name__ !=  "Int" or type(r).__name__ !=  "Int":
            if type(l).__name__ !=  "Id" and type(r).__name__ !=  "Id" and type(l).__name__ != 'IfCount' and type(r).__name__ != 'IfCount' and type(l).__name__ != 'OwnMethod'and type(r).__name__ != 'OwnMethod':
                new_error = tables.Error("No corresponden los tipos de la multiplicacion", ctx.start.line, ctx.start.column,ctx.getText())
                self.ERRORS.append(new_error)   

        multiply = lista.Multiply(l,r)
        self.multiply.append(multiply)

        return multiply


    def visitNewObject(self, ctx):
        tipo = None
        if ctx.TYPE() is not None:
            tipo = ctx.TYPE().getText()
        
        if tipo is not None:
            id = encontradorClases(tipo,self.table)
            if tipo in self.reservado: id = {'kind': 1}
            if id is None:
                new_error = tables.Error("No ha encontrado la clase", ctx.start.line, ctx.start.column,tipo)
                self.ERRORS.append(new_error) 
            else:
                if id['kind'] != 1:
                    new_error = tables.Error("No corresponde la llamada", ctx.start.line, ctx.start.column,tipo)
                    self.ERRORS.append(new_error) 
        else:
            new_error = tables.Error("No corresponde la llamada", ctx.start.line, ctx.start.column,ctx.getText().replace('new', '', 1))
            self.ERRORS.append(new_error) 

        new = lista.New(tipo)
        self.new.append(new)

        return new
    

    def visitNegation(self, ctx):
        bn = self.visit(ctx.expr())

        if (type(bn).__name__ != 'TrueCount' and type(bn).__name__ != 'FalseCount' and type(bn).__name__ != 'Id' and type(bn).__name__ != 'MethodCall'):
                new_error = tables.Error("No corresponden los tipos del not", ctx.start.line, ctx.start.column,ctx.getText())
                self.ERRORS.append(new_error)

        boolnot = lista.BoolNot(bn)
        self.boolnot.append(boolnot)

        return boolnot
    

    def visitNegInteger(self, ctx):
        ne = self.visit(ctx.expr())

        if type(ne).__name__ == 'Id':
            id  = verificaThor(ctx.expr().getText(),self.variables)
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.getText())
                self.ERRORS.append(new_error) 
            else:
                if id.type != 'Int':
                    new_error = tables.Error("No corresponden los tipos de la negacion", ctx.start.line, ctx.start.column,ctx.getText())
                    self.ERRORS.append(new_error)  

        if (type(ne).__name__ != 'Int' and type(ne).__name__ != 'Id'):
                new_error = tables.Error("No corresponden los tipos de la negacion", ctx.start.line, ctx.start.column,ctx.getText())
                self.ERRORS.append(new_error) 
        negative = lista.Negative(ne)
        self.negative.append(negative)

        return negative
    
    def visitIsVoid(self, ctx):
        vo = self.visit(ctx.expr())

        if type(vo).__name__ == 'Id':
            id  = verificaThor(ctx.expr().getText(),self.variables)
            if vo.id in self.palabras: id = {'kind': 1}
            if id is None:
                new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,ctx.expr().getText())
                self.ERRORS.append(new_error) 
            # else:
            #     if id.type != 'Int':
            #         new_error = tables.Error("No corresponden los tipos de void", ctx.start.line, ctx.start.column,vo)
            #         self.ERRORS.append(new_error)  

        if (type(vo).__name__ != 'Id'):
                new_error = tables.Error("No corresponden los tipos de la void", ctx.start.line, ctx.start.column,vo)
                self.ERRORS.append(new_error) 

        void = lista.Isvoid(vo)
        self.void.append(void)

        return void


    def visitDispatch(self, ctx):
        name = ctx.ID().getText()
        tipo = None; expr1 = None; expr2 = None

        if ctx.TYPE() is not None:
            tipo = ctx.TYPE().getText()
            id = encontradorClases(tipo,self.table)
            if tipo in self.reservado: id = {'kind': 1}
            if id is None:
                new_error = tables.Error("No ha encontrado la clase", ctx.start.line, ctx.start.column,tipo)
                self.ERRORS.append(new_error)
            elif comprobador(name,tipo,self.table):
                    new_error = tables.Error("El metodo no se encuentra dentro de la clase", ctx.start.line, ctx.start.column,tipo)
                    self.ERRORS.append(new_error) 
            else:
                if id['kind'] != 1:
                    new_error = tables.Error("No corresponde la llamada", ctx.start.line, ctx.start.column,tipo)
                    self.ERRORS.append(new_error) 

        expr = self.visit(ctx.expr(0))

        if type(expr).__name__ == 'Id':
            if expr.id != "self":
                id  = verificaThor(expr.id,self.variables)
                if id is None:
                    new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,expr.id)
                    self.ERRORS.append(new_error)  

        if ctx.expr(1) is not None:
            expr1 = self.visit(ctx.expr(1))
            if type(expr1).__name__ == 'Id':
                if expr1.id != "self":
                    id  = verificaThor(expr1.id,self.variables)
                    if id is None:
                        new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,expr1.id)
                        self.ERRORS.append(new_error)  

        if ctx.expr(2) is not None:
            expr2 = self.visit(ctx.expr(2))

        if name != "in_string" and name != "in_int" and name != "out_string" and name != "out_int" and name != "concat" and name != "length" and name != "substr" and name != "type_name" and name != "abort":
            id = encontradorClases(name,self.table)
            numero = contadorDeParametros(name,id['line'],self.table)
            params = obtenerParametros(name,id['line'],self.table)
            if id is None:
                new_error = tables.Error("No se declaro el metodo", ctx.start.line, ctx.start.column,ctx.ID().getText())
                self.ERRORS.append(new_error) 
            elif numero != len(ctx.expr()) - 1:
                new_error = tables.Error("la cantidad de elementos no coincide con los del metodo", ctx.start.line, ctx.start.column,name)
                self.ERRORS.append(new_error) 

        if len(ctx.expr()) - 1 > 1:
            arguments = []
            for f in ctx.expr():
                argumen = self.visit(f)
                arguments.append(argumen)
            arguments.pop(0)
            for a in arguments:
                if type(a).__name__ == 'Id':
                    id  = verificaThor(a.id,self.variables)
                    if id is None:
                        new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,a.id)
                        self.ERRORS.append(new_error)
                    else:
                        for p in params:
                            if id.type != p['type']:
                                new_error = tables.Error("No corresponden los tipos con el metodo", ctx.start.line, ctx.start.column,a.id)
                                self.ERRORS.append(new_error)
                                params.pop(0)
                            else:
                                params.pop(0)
                if type(a).__name__ == 'MethodCall':
                    for p in params:
                        id = encontradorClases(a.name,self.table)
                        if id['type']!= p['type']:
                            new_error = tables.Error("No corresponden los tipos con el metodo", ctx.start.line, ctx.start.column,a.id)
                            self.ERRORS.append(new_error)
                            params.pop(0)
                            break
                        else:
                            params.pop(0)
                            break
        else:
            if type(expr1).__name__ == 'Id':
                id  = verificaThor(expr1.id,self.variables)
                if id is None:
                    new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,expr1.id)
                    self.ERRORS.append(new_error)
                else:
                    for p in params:
                        if id.type != p['type']:
                            new_error = tables.Error("No corresponden los tipos con el metodo", ctx.start.line, ctx.start.column,expr1.id)
                            self.ERRORS.append(new_error)


        if name == "in_string" or name == "in_int":
            instr = lista.In(name)
            self.instr.append(instr)
            return instr
        
        if name == "out_string":
            outstring = lista.OutString(expr,expr1,expr2)
            self.outstring.append(outstring)
            return outstring

        if name == "out_int":
            outint = lista.OutInt(expr,expr1,expr2)
            self.outint.append(outint)
            return outint
        methodcall = lista.MethodCall(name,tipo,expr,expr1,expr2)
        self.methodcall.append(methodcall)

        return methodcall


    def visitCall(self, ctx):
        instance = "self"
        method = ctx.ID().getText()

        arguments = []
        for f in ctx.expr():
            argumen = self.visit(f)
            arguments.append(argumen)

        idC = encontradorClases(method,self.table)
        if idC is not None:
            numero = contadorDeParametros(method,idC['line'],self.table)
            params = obtenerParametros(method,idC['line'],self.table)

        if method != "in_string" and method != "in_int" and method != "out_string" and method != "out_int" and method != "concat" and method != "length" and method != "substr" and method != "type_name" and method != "abort":
            if idC is None:
                new_error = tables.Error("No se declaro el metodo", ctx.start.line, ctx.start.column,ctx.getText())
                self.ERRORS.append(new_error)  
            elif numero != len(arguments):
                new_error = tables.Error("la cantidad de elementos no coincide con los del metodo", ctx.start.line, ctx.start.column,method)
                self.ERRORS.append(new_error)


        
        for a in arguments:
            if type(a).__name__ == 'Id':
                id  = verificaThor(a.id,self.variables)
                if id is None:
                    new_error = tables.Error("No se declaro la variable", ctx.start.line, ctx.start.column,a.id)
                    self.ERRORS.append(new_error)
                else:
                    if idC is not None:
                        for p in params:
                            if id.type != p['type']:
                                new_error = tables.Error("No corresponden los tipos con el metodo", ctx.start.line, ctx.start.column,a.id)
                                self.ERRORS.append(new_error)

        if method == "in_string" or method == "in_int":
            instr = lista.In(method)
            self.instr.append(instr)
            return instr
        
        if method == "out_string":
            outstring = lista.OutString(arguments)
            self.outstring.append(outstring)
            return outstring

        if method == "out_int":
            outint = lista.OutInt(arguments)
            self.outint.append(outint)
            return outint

        OwnMeth = lista.OwnMethod(method,arguments)
        self.ownmethod.append(OwnMeth)
        return OwnMeth


    def visitParenthesis(self, ctx):
        expr = self.visit(ctx.expr())

        parentheses = lista.Parentheses(expr)
        self.parentheses.append(parentheses)

        return parentheses


    def visitBlock(self, ctx):
        expr = []
        for e in ctx.expr():
            expre = self.visit(e)
            expr.append(expre)

        block = lista.Block(expr)
        self.block.append(block)

        return block
    

    def visitStr(self, ctx):
        stri = ctx.STR().getText()
        striLoop = stri
        list_valus = []

        if (len(ctx.getText()) > 25):
            new_error = tables.Error("Longitud de string excedida", ctx.start.line, ctx.start.column,ctx.getText())
            self.ERRORS.append(new_error)

        if "\\n" in stri:
            id = "\\n"
            striLoop = idTexto(id,stri,striLoop,self.valor,list_valus)

        if "\\t" in stri:
            id = "\\t"
            striLoop = idTexto(id,stri,striLoop,self.valor,list_valus)

        string = lista.String(striLoop,stri,list_valus)
        self.string.append(string)

        return string





    def visitTrue(self, ctx):
        true = ctx.TRUE().getText()

        truet = lista.TrueCount(true)
        self.truet.append(truet)

        return truet


    def visitFalse(self, ctx):
        false = ctx.FALSE().getText()

        fals = lista.FalseCount(false)
        self.fals.append(fals)

        return fals
    

    def visitInt(self, ctx):
        int = ctx.INT().getText()

        integer = lista.Int(int)
        self.integer.append(integer)

        return integer
    
    
    def visitId(self, ctx):
        name = ctx.ID().getText()

        id = lista.Id(name)
        self.id.append(id)

        return id
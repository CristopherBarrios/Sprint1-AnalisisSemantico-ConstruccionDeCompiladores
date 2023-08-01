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
    def __init__(self):
        YAPLVisitor.__init__(self)
        self.ERRORS = []

        self.class_ids = -1
        self.method_ids = -1
        self.symbols_ids = 0
        self.offset = 0
        self.instantiable_ids = 0
        global_scope = tables.Scope()
        self.scopes = []

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
        
        #return self.visitChildren(ctx)

 
    def visitEnd(self, ctx):
        self.visitStart(ctx)
        #return self.visitChildren(ctx)


    def visitClass_exp(self, ctx):
        class_name = ctx.TYPE(0).getText()
        self.class_ids += 1

        parent = None
        if len(ctx.TYPE()) > 1:
            parent = ctx.TYPE(1).getText()

        features = []
        for f in ctx.feature():
            feature = self.visit(f)
            features.append(feature)

        for met in self.clases:
            if class_name == met.name:
                new_error = tables.Error("Ya se ha declarado esta clase " + str(class_name), ctx.start.line, ctx.start.column)
                self.ERRORS.append(new_error)

        clase = lista.Clase(class_name,parent,self.class_ids,features)
        self.clases.append(clase)

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
        type = None;expr=None
        if ctx.TYPE():
            type = ctx.TYPE().getText()
        self.method_ids += 1

        for meto in self.metodos:
            if name == meto.name:
                self.method_ids -= 1
                return 0

        formalParams = []
        for f in ctx.formal():
            formalParam = self.visit(f)
            formalParams.append(formalParam)

        if ctx.expr():
            expr = self.visit(ctx.expr())

        metodo = lista.Method(name,self.method_ids,type,formalParams,expr)
        self.metodos.append(metodo)

        if name == "main":
            if ctx.formal():
                new_error = tables.Error("El metodo main no puede contener parametros formales ", ctx.start.line, ctx.start.column)
                self.ERRORS.append(new_error)              

        if name == type or type == None:
            new_error = tables.Error("No se puede encontrar type en metodo ", ctx.start.line, ctx.start.column)
            self.ERRORS.append(new_error)

        return metodo



    def visitAttribute(self, ctx):
        what = ctx.getChild(0)
        name = ctx.ID().getText()
        type = ctx.TYPE().getText()
        type2 = ctx.getText()

        if ctx.ASSIGNMENT() is None:
            propiedad = lista.Property(name,type,None)
            self.property.append(propiedad)
            return propiedad

        expr = self.visit(ctx.expr())

        propiedad = lista.Property(name,type,expr)
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



    def visitLetIn(self, ctx):
        let = self.visit(ctx.declaration(0))
        let1 = None
        if ctx.declaration(1) is not None:
            let1 = self.visit(ctx.declaration(1))
        expr = self.visit(ctx.expr())

        letin = lista.LetIn(let,let1,expr)
        self.letin.append(letin)

        return letin


    def visitMinus(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))

        if type(l).__name__ !=  "Int" or type(r).__name__ !=  "Int":
            if type(l).__name__ !=  "Id" and type(r).__name__ !=  "Id":
        # if (l != "INT" or r != "INT"):
        #     if l != "ID" and r != "ID":
                new_error = tables.Error("No corresponden los tipos de la resta", ctx.start.line, ctx.start.column,ctx.getText())
                self.ERRORS.append(new_error)
        

        minus = lista.Minus(l,r)
        self.minus.append(minus)
        return minus
        #return self.visitChildren(ctx)



    def visitNegation(self, ctx):
        bn = self.visit(ctx.expr())

        boolnot = lista.BoolNot(bn)
        self.boolnot.append(boolnot)

        return boolnot




    def visitDispatch(self, ctx):
        name = ctx.ID().getText()
        type = None; expr1 = None; expr2 = None
        
        if ctx.TYPE() is not None:
            type = ctx.TYPE().getText()

        expr = self.visit(ctx.expr(0))

        if ctx.expr(1) is not None:
            expr1 = self.visit(ctx.expr(1))

        if ctx.expr(2) is not None:
            expr2 = self.visit(ctx.expr(2))

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
        methodcall = lista.MethodCall(name,type,expr,expr1,expr2)
        self.methodcall.append(methodcall)

        return methodcall



    def visitWhile(self, ctx):
        expWhile = self.visit(ctx.expr(0))
        expLoop = self.visit(ctx.expr(1))

        if type(expWhile).__name__ == "Add" or type(expWhile).__name__ == "Division" or type(expWhile).__name__ == "Multiply" or type(expWhile).__name__ == "Minus":
            new_error = tables.Error("While tiene que ser booleano", ctx.start.line, ctx.start.column)
            self.ERRORS.append(new_error)

        whileCount = lista.WhileCount(expWhile,expLoop)
        self.whileCount.append(whileCount)

        return whileCount
        #return self.visitChildren(ctx)



    def visitvDivision(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))

        if type(l).__name__ !=  "Int" or type(r).__name__ !=  "Int":
            if type(l).__name__ !=  "Id" and type(r).__name__ !=  "Id":
        # if (l != "INT" or r != "INT"):
        #     if l != "ID" and r != "ID":
                new_error = tables.Error("No corresponden los tipos de la division", ctx.start.line, ctx.start.column,ctx.getText())
                self.ERRORS.append(new_error) 

        division = lista.Division(l,r)
        self.division.append(division)

        return division


    def visitNewObject(self, ctx):
        type = ctx.TYPE().getText()

        new = lista.New(type)
        self.new.append(new)

        return new


 
    def visitLessThan(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))

        if type(l).__name__ != type(r).__name__ :
            if type(l).__name__ !=  "Id" and type(r).__name__ !=  "Id":
        # if (l != r):
        #     if l != "ID" and r != "ID":

                new_error = tables.Error("No corresponden los tipos de la comparacion =", ctx.start.line, ctx.start.column,ctx.getText())
                self.ERRORS.append(new_error) 

        lessthan = lista.LessThan(l,r)
        self.lessthan.append(lessthan)

        return lessthan




    def visitBlock(self, ctx):
        expr = []
        for e in ctx.expr():
            expre = self.visit(e)
            expr.append(expre)

        block = lista.Block(expr)
        self.block.append(block)

        return block


    def visitNegInteger(self, ctx):
        ne = self.visit(ctx.expr())

        negative = lista.Negative(ne)
        self.negative.append(negative)

        return negative
        #return self.visitChildren(ctx)



    def visitId(self, ctx):
        name = ctx.ID().getText()

        id = lista.Id(name)
        self.id.append(id)

        return id
        #return "ID"



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



    def visitAdd(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))


        if type(l).__name__ !=  "Int" or type(r).__name__ !=  "Int":
            if type(l).__name__ !=  "Id" and type(r).__name__ !=  "Id":
                new_error = tables.Error("No corresponden los tipos de la suma", ctx.start.line, ctx.start.column,ctx.getText())
                self.ERRORS.append(new_error)
        # if (l != "INT" or r != "INT"):
        #     if l != "ID" and r != "ID":
        #         new_error = tables.Error("No corresponden los tipos de la suma", ctx.start.line, ctx.start.column,ctx.getText())
        #         self.ERRORS.append(new_error)

        add = lista.Add(l,r)
        self.add.append(add)

        #return self.visitChildren(ctx)



    def visitStar(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))

        if type(l).__name__ !=  "Int" or type(r).__name__ !=  "Int":
            if type(l).__name__ !=  "Id" and type(r).__name__ !=  "Id":

        # if (l != "INT" or r != "INT"):
        #     if l != "ID" and r != "ID":
                new_error = tables.Error("No corresponden los tipos de la multiplicacion", ctx.start.line, ctx.start.column,ctx.getText())
                self.ERRORS.append(new_error)   

        multiply = lista.Multiply(l,r)
        self.multiply.append(multiply)

        return multiply

        #return self.visitChildren(ctx)



    def visitAssignment(self, ctx):
        name = ctx.ID().getText()
        expr = self.visit(ctx.expr())

        assignement = lista.Assignment(name,expr)
        self.assignment.append(assignement)

        return assignement
        #return self.visitChildren(ctx)



    def visitFalse(self, ctx):
        false = ctx.FALSE().getText()

        fals = lista.FalseCount(false)
        self.fals.append(fals)

        return fals
        #return "FALSE"


    def visitParenthesis(self, ctx):
        expr = self.visit(ctx.expr())

        parentheses = lista.Parentheses(expr)
        self.parentheses.append(parentheses)

        return parentheses


    def visitInt(self, ctx):
        int = ctx.INT().getText()

        integer = lista.Int(int)
        self.integer.append(integer)

        return integer
        #return "INT"



    def visitCall(self, ctx):
        instance = "self"
        method = ctx.ID().getText()

        arguments = []
        for f in ctx.expr():
            argumen = self.visit(f)
            arguments.append(argumen)
        
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
        #return self.visitChildren(ctx)


    def visitStr(self, ctx):
        stri = ctx.STR().getText()
        striLoop = stri
        list_valus = []

        if (len(ctx.getText()) > 17):
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
        #return "STRING"



    def visitEqual(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))

        if type(l).__name__ != type(r).__name__ :
            if type(l).__name__ !=  "Id" and type(r).__name__ !=  "Id":

        # if (l != r):
        #     if l != "ID" and r != "ID":
                new_error = tables.Error("No corresponden los tipos de la comparacion <", ctx.start.line, ctx.start.column,ctx.getText())
                self.ERRORS.append(new_error) 

        equal = lista.Equal(l,r)
        self.equal.append(equal)

        return equal
        #return self.visitChildren(ctx)


    def visitIsVoid(self, ctx):
        vo = self.visit(ctx.expr())

        void = lista.Isvoid(vo)
        self.void.append(void)

        return void
        #return self.visitChildren(ctx)



    def visitTrue(self, ctx):
        true = ctx.TRUE().getText()

        truet = lista.TrueCount(true)
        self.truet.append(truet)

        return truet
        #return "TRUE"



    def visitLessEqual(self, ctx):
        l = self.visit(ctx.expr(0))
        r = self.visit(ctx.expr(1))

        if type(l).__name__ != type(r).__name__ :
            if type(l).__name__ !=  "Id" and type(r).__name__ !=  "Id":

        # if (l != r):
        #     if l != "ID" and r != "ID":
                new_error = tables.Error("No corresponden los tipos de la comparacion <=", ctx.start.line, ctx.start.column,ctx.getText())
                self.ERRORS.append(new_error) 

        lessequal = lista.LessEqual(l,r)
        self.lessequal.append(lessequal)

        return lessequal
        #return self.visitChildren(ctx)

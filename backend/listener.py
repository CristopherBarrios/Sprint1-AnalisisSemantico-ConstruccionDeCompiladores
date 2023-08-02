from YAPL.YAPLVisitor import YAPLVisitor
from YAPL.YAPLParser import YAPLParser
from YAPL.YAPLListener import YAPLListener

from backend.custom_error import indx
from backend.symbol import Symbol
from backend.help import *


class MyYAPLListener(YAPLListener):
    def __init__(self):
        self.symbol_table = Symbol()
        self.ERRORS = self.symbol_table.ERRORS
        self.letnum = 0

    def assign_value(self, ctx):
        self.symbol_table.set(ctx.children[0].getText(), ctx.children[0].symbol.line, ctx.children[2].getText())

    def insert_self(self, line: int):
        name = 'self'
        kind = ATTR
        typ = SELF_TYPE
        scope = self.symbol_table.get_scope()
        self.symbol_table.insert(name, typ, kind, scope, line)

    def insert_class(self, ctx):
        children = list(map(lambda x: x.getText(), ctx.children))
        name = children[1]
        kind = CLASS
        ind = indx(children, 'inherits')
        typ = children[ind + 1] if ind != -1 else 'Object'
        line = ctx.children[0].symbol.line
        scope = self.symbol_table.get_scope()
        self.symbol_table.insert(name, typ, kind, scope, line)

    def insert_feature(self, ctx):
        children = list(map(lambda x: x.getText(), ctx.children))
        name = children[0]
        kind = METHOD if children[1] != ':' else ATTR
        ind = indx(children, ':')
        typ = children[ind + 1]
        line = ctx.children[0].symbol.line
        value = None
        scope = self.symbol_table.get_scope()

        if kind == 'method':
            self.symbol_table.push_scope(children[0])
        else:
            index = indx(children, '<-')
            if index != -1:
                value = children[index + 1]

        self.symbol_table.insert(name, typ, kind, scope, line, value)
    
    def insert_param(self, ctx):
        children = list(map(lambda x: x.getText(), ctx.children))
        name = children[0]
        kind = PARAMETER
        typ = children[2]
        line = ctx.children[0].symbol.line
        scope = self.symbol_table.get_scope()
        self.symbol_table.insert(name, typ, kind, scope, line)

    def insert_letin(self, ctx):
        children = list(map(lambda x: x.getText(), ctx.children))
        self.letnum += 1
        name = children[0] + str(self.letnum)
        kind = LET
        texto = children[1]
        ind = indx(children[1], ':')
        typ = texto[ind + 1:].strip()
        line = ctx.children[0].symbol.line
        scope = self.symbol_table.get_scope()

        if children[0] == 'let':
            self.symbol_table.push_scope(name)

        self.symbol_table.insert(name, typ, kind, scope, line)

    def insert_decla(self, ctx):
        children = list(map(lambda x: x.getText(), ctx.children))
        name = children[0]
        kind = DECLARATION
        typ = children[2]
        line = ctx.children[0].symbol.line
        scope = self.symbol_table.get_scope()
        self.symbol_table.insert(name, typ, kind, scope, line)

    def getTable(self):
        return self.symbol_table.getTable()

    def enterClass_exp(self, ctx):
        self.insert_class(ctx)
        self.symbol_table.push_scope(ctx.children[1].getText())
        self.insert_self(ctx.children[0].symbol.line)

    def exitClass_exp(self, ctx):
        self.symbol_table.pop_scope()

    def enterMethod(self, ctx):
        self.insert_feature(ctx)

    def exitMethod(self, ctx):
        if ctx.children[1].getText() != ':':
            self.symbol_table.pop_scope()

    def enterAttribute(self, ctx):
        self.insert_feature(ctx)

    def exitAttribute(self, ctx):
        if ctx.children[1].getText() != ':':
            self.symbol_table.pop_scope()

    def enterFormal(self, ctx):
        self.insert_param(ctx)

    def enterDeclaration(self, ctx):
        self.insert_decla(ctx)

    def exitDeclaration(self, ctx):
        if ctx.children[1].getText() != ':':
            self.symbol_table.pop_scope()

    def enterLetIn(self, ctx):
        self.insert_letin(ctx)

    def exitLetIn(self, ctx):
        if ctx.children[1].getText() != ':':
            self.symbol_table.pop_scope()

    def enterExpr(self, ctx):
        children = list(map(lambda x: x.getText(), ctx.children))
        if '<-' in children:
            self.assign_value(ctx)

    def enterStart(self, ctx):
        pass

    def exitStart(self, ctx):
        pass

    def enterClass_list(self, ctx):
        pass

    def exitClass_list(self, ctx):
        pass

    def enterEnd(self, ctx):
        pass

    def exitEnd(self, ctx):
        pass

    def exitFormal(self, ctx):
        pass

    def enterMinus(self, ctx):
        pass

    def exitMinus(self, ctx):
        pass

    def enterNegation(self, ctx):
        pass

    def exitNegation(self, ctx):
        pass

    def enterDispatch(self, ctx):
        pass

    def exitDispatch(self, ctx):
        pass

    def enterWhile(self, ctx):
        pass

    def exitWhile(self, ctx):
        pass

    def enterDivision(self, ctx):
        pass

    def exitDivision(self, ctx):
        pass

    def enterNewObject(self, ctx):
        pass

    def exitNewObject(self, ctx):
        pass

    def enterLessThan(self, ctx):
        pass

    def exitLessThan(self, ctx):
        pass

    def enterBlock(self, ctx):
        pass

    def exitBlock(self, ctx):
        pass

    def enterNegInteger(self, ctx):
        pass

    def exitNegInteger(self, ctx):
        pass

    def enterId(self, ctx):
        pass

    def exitId(self, ctx):
        pass

    def enterIf(self, ctx):
        pass

    def exitIf(self, ctx):
        pass

    def enterCase(self, ctx):
        pass

    def exitCase(self, ctx):
        pass

    def enterAdd(self, ctx):
        pass

    def exitAdd(self, ctx):
        pass

    def enterStar(self, ctx):
        pass

    def exitStar(self, ctx):
        pass

    def enterAssignment(self, ctx):
        pass

    def exitAssignment(self, ctx):
        pass

    def enterFalse(self, ctx):
        pass

    def exitFalse(self, ctx):
        pass

    def enterParenthesis(self, ctx):
        pass

    def exitParenthesis(self, ctx):
        pass

    def enterInt(self, ctx):
        pass

    def exitInt(self, ctx):
        pass

    def enterCall(self, ctx):
        pass

    def exitCall(self, ctx):
        pass

    def enterStr(self, ctx):
        pass

    def exitStr(self, ctx):
        pass

    def enterEqual(self, ctx):
        pass

    def exitEqual(self, ctx):
        pass

    def enterIsVoid(self, ctx):
        pass

    def exitIsVoid(self, ctx):
        pass

    def enterTrue(self, ctx):
        pass

    def exitTrue(self, ctx):
        pass

    def enterLessEqual(self, ctx):
        pass

    def exitLessEqual(self, ctx):
        pass
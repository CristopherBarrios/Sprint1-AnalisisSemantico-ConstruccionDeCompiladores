# Generated from YAPL.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YAPLParser import YAPLParser
else:
    from YAPLParser import YAPLParser

# This class defines a complete generic visitor for a parse tree produced by YAPLParser.

class YAPLVisitor(ParseTreeVisitor):

    # Visit a parse tree produced by YAPLParser#start.
    def visitStart(self, ctx:YAPLParser.StartContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#class_list.
    def visitClass_list(self, ctx:YAPLParser.Class_listContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#end.
    def visitEnd(self, ctx:YAPLParser.EndContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#class_exp.
    def visitClass_exp(self, ctx:YAPLParser.Class_expContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#method.
    def visitMethod(self, ctx:YAPLParser.MethodContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#attribute.
    def visitAttribute(self, ctx:YAPLParser.AttributeContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#formal.
    def visitFormal(self, ctx:YAPLParser.FormalContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#declaration.
    def visitDeclaration(self, ctx:YAPLParser.DeclarationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#letIn.
    def visitLetIn(self, ctx:YAPLParser.LetInContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#minus.
    def visitMinus(self, ctx:YAPLParser.MinusContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#negation.
    def visitNegation(self, ctx:YAPLParser.NegationContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#dispatch.
    def visitDispatch(self, ctx:YAPLParser.DispatchContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#while.
    def visitWhile(self, ctx:YAPLParser.WhileContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#division.
    def visitDivision(self, ctx:YAPLParser.DivisionContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#newObject.
    def visitNewObject(self, ctx:YAPLParser.NewObjectContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#lessThan.
    def visitLessThan(self, ctx:YAPLParser.LessThanContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#block.
    def visitBlock(self, ctx:YAPLParser.BlockContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#negInteger.
    def visitNegInteger(self, ctx:YAPLParser.NegIntegerContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#id.
    def visitId(self, ctx:YAPLParser.IdContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#if.
    def visitIf(self, ctx:YAPLParser.IfContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#case.
    def visitCase(self, ctx:YAPLParser.CaseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#add.
    def visitAdd(self, ctx:YAPLParser.AddContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#star.
    def visitStar(self, ctx:YAPLParser.StarContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#assignment.
    def visitAssignment(self, ctx:YAPLParser.AssignmentContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#false.
    def visitFalse(self, ctx:YAPLParser.FalseContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#parenthesis.
    def visitParenthesis(self, ctx:YAPLParser.ParenthesisContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#int.
    def visitInt(self, ctx:YAPLParser.IntContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#call.
    def visitCall(self, ctx:YAPLParser.CallContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#str.
    def visitStr(self, ctx:YAPLParser.StrContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#equal.
    def visitEqual(self, ctx:YAPLParser.EqualContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#isVoid.
    def visitIsVoid(self, ctx:YAPLParser.IsVoidContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#true.
    def visitTrue(self, ctx:YAPLParser.TrueContext):
        return self.visitChildren(ctx)


    # Visit a parse tree produced by YAPLParser#lessEqual.
    def visitLessEqual(self, ctx:YAPLParser.LessEqualContext):
        return self.visitChildren(ctx)



del YAPLParser
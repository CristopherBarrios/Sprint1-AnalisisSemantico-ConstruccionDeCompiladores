# Generated from YAPL.g4 by ANTLR 4.10.1
from antlr4 import *
if __name__ is not None and "." in __name__:
    from .YAPLParser import YAPLParser
else:
    from YAPLParser import YAPLParser

# This class defines a complete listener for a parse tree produced by YAPLParser.
class YAPLListener(ParseTreeListener):

    # Enter a parse tree produced by YAPLParser#start.
    def enterStart(self, ctx:YAPLParser.StartContext):
        pass

    # Exit a parse tree produced by YAPLParser#start.
    def exitStart(self, ctx:YAPLParser.StartContext):
        pass


    # Enter a parse tree produced by YAPLParser#class_list.
    def enterClass_list(self, ctx:YAPLParser.Class_listContext):
        pass

    # Exit a parse tree produced by YAPLParser#class_list.
    def exitClass_list(self, ctx:YAPLParser.Class_listContext):
        pass


    # Enter a parse tree produced by YAPLParser#end.
    def enterEnd(self, ctx:YAPLParser.EndContext):
        pass

    # Exit a parse tree produced by YAPLParser#end.
    def exitEnd(self, ctx:YAPLParser.EndContext):
        pass


    # Enter a parse tree produced by YAPLParser#class_exp.
    def enterClass_exp(self, ctx:YAPLParser.Class_expContext):
        pass

    # Exit a parse tree produced by YAPLParser#class_exp.
    def exitClass_exp(self, ctx:YAPLParser.Class_expContext):
        pass


    # Enter a parse tree produced by YAPLParser#method.
    def enterMethod(self, ctx:YAPLParser.MethodContext):
        pass

    # Exit a parse tree produced by YAPLParser#method.
    def exitMethod(self, ctx:YAPLParser.MethodContext):
        pass


    # Enter a parse tree produced by YAPLParser#attribute.
    def enterAttribute(self, ctx:YAPLParser.AttributeContext):
        pass

    # Exit a parse tree produced by YAPLParser#attribute.
    def exitAttribute(self, ctx:YAPLParser.AttributeContext):
        pass


    # Enter a parse tree produced by YAPLParser#formal.
    def enterFormal(self, ctx:YAPLParser.FormalContext):
        pass

    # Exit a parse tree produced by YAPLParser#formal.
    def exitFormal(self, ctx:YAPLParser.FormalContext):
        pass


    # Enter a parse tree produced by YAPLParser#declaration.
    def enterDeclaration(self, ctx:YAPLParser.DeclarationContext):
        pass

    # Exit a parse tree produced by YAPLParser#declaration.
    def exitDeclaration(self, ctx:YAPLParser.DeclarationContext):
        pass


    # Enter a parse tree produced by YAPLParser#letIn.
    def enterLetIn(self, ctx:YAPLParser.LetInContext):
        pass

    # Exit a parse tree produced by YAPLParser#letIn.
    def exitLetIn(self, ctx:YAPLParser.LetInContext):
        pass


    # Enter a parse tree produced by YAPLParser#minus.
    def enterMinus(self, ctx:YAPLParser.MinusContext):
        pass

    # Exit a parse tree produced by YAPLParser#minus.
    def exitMinus(self, ctx:YAPLParser.MinusContext):
        pass


    # Enter a parse tree produced by YAPLParser#negation.
    def enterNegation(self, ctx:YAPLParser.NegationContext):
        pass

    # Exit a parse tree produced by YAPLParser#negation.
    def exitNegation(self, ctx:YAPLParser.NegationContext):
        pass


    # Enter a parse tree produced by YAPLParser#dispatch.
    def enterDispatch(self, ctx:YAPLParser.DispatchContext):
        pass

    # Exit a parse tree produced by YAPLParser#dispatch.
    def exitDispatch(self, ctx:YAPLParser.DispatchContext):
        pass


    # Enter a parse tree produced by YAPLParser#while.
    def enterWhile(self, ctx:YAPLParser.WhileContext):
        pass

    # Exit a parse tree produced by YAPLParser#while.
    def exitWhile(self, ctx:YAPLParser.WhileContext):
        pass


    # Enter a parse tree produced by YAPLParser#division.
    def enterDivision(self, ctx:YAPLParser.DivisionContext):
        pass

    # Exit a parse tree produced by YAPLParser#division.
    def exitDivision(self, ctx:YAPLParser.DivisionContext):
        pass


    # Enter a parse tree produced by YAPLParser#newObject.
    def enterNewObject(self, ctx:YAPLParser.NewObjectContext):
        pass

    # Exit a parse tree produced by YAPLParser#newObject.
    def exitNewObject(self, ctx:YAPLParser.NewObjectContext):
        pass


    # Enter a parse tree produced by YAPLParser#lessThan.
    def enterLessThan(self, ctx:YAPLParser.LessThanContext):
        pass

    # Exit a parse tree produced by YAPLParser#lessThan.
    def exitLessThan(self, ctx:YAPLParser.LessThanContext):
        pass


    # Enter a parse tree produced by YAPLParser#block.
    def enterBlock(self, ctx:YAPLParser.BlockContext):
        pass

    # Exit a parse tree produced by YAPLParser#block.
    def exitBlock(self, ctx:YAPLParser.BlockContext):
        pass


    # Enter a parse tree produced by YAPLParser#negInteger.
    def enterNegInteger(self, ctx:YAPLParser.NegIntegerContext):
        pass

    # Exit a parse tree produced by YAPLParser#negInteger.
    def exitNegInteger(self, ctx:YAPLParser.NegIntegerContext):
        pass


    # Enter a parse tree produced by YAPLParser#id.
    def enterId(self, ctx:YAPLParser.IdContext):
        pass

    # Exit a parse tree produced by YAPLParser#id.
    def exitId(self, ctx:YAPLParser.IdContext):
        pass


    # Enter a parse tree produced by YAPLParser#if.
    def enterIf(self, ctx:YAPLParser.IfContext):
        pass

    # Exit a parse tree produced by YAPLParser#if.
    def exitIf(self, ctx:YAPLParser.IfContext):
        pass


    # Enter a parse tree produced by YAPLParser#case.
    def enterCase(self, ctx:YAPLParser.CaseContext):
        pass

    # Exit a parse tree produced by YAPLParser#case.
    def exitCase(self, ctx:YAPLParser.CaseContext):
        pass


    # Enter a parse tree produced by YAPLParser#add.
    def enterAdd(self, ctx:YAPLParser.AddContext):
        pass

    # Exit a parse tree produced by YAPLParser#add.
    def exitAdd(self, ctx:YAPLParser.AddContext):
        pass


    # Enter a parse tree produced by YAPLParser#star.
    def enterStar(self, ctx:YAPLParser.StarContext):
        pass

    # Exit a parse tree produced by YAPLParser#star.
    def exitStar(self, ctx:YAPLParser.StarContext):
        pass


    # Enter a parse tree produced by YAPLParser#assignment.
    def enterAssignment(self, ctx:YAPLParser.AssignmentContext):
        pass

    # Exit a parse tree produced by YAPLParser#assignment.
    def exitAssignment(self, ctx:YAPLParser.AssignmentContext):
        pass


    # Enter a parse tree produced by YAPLParser#false.
    def enterFalse(self, ctx:YAPLParser.FalseContext):
        pass

    # Exit a parse tree produced by YAPLParser#false.
    def exitFalse(self, ctx:YAPLParser.FalseContext):
        pass


    # Enter a parse tree produced by YAPLParser#parenthesis.
    def enterParenthesis(self, ctx:YAPLParser.ParenthesisContext):
        pass

    # Exit a parse tree produced by YAPLParser#parenthesis.
    def exitParenthesis(self, ctx:YAPLParser.ParenthesisContext):
        pass


    # Enter a parse tree produced by YAPLParser#int.
    def enterInt(self, ctx:YAPLParser.IntContext):
        pass

    # Exit a parse tree produced by YAPLParser#int.
    def exitInt(self, ctx:YAPLParser.IntContext):
        pass


    # Enter a parse tree produced by YAPLParser#call.
    def enterCall(self, ctx:YAPLParser.CallContext):
        pass

    # Exit a parse tree produced by YAPLParser#call.
    def exitCall(self, ctx:YAPLParser.CallContext):
        pass


    # Enter a parse tree produced by YAPLParser#str.
    def enterStr(self, ctx:YAPLParser.StrContext):
        pass

    # Exit a parse tree produced by YAPLParser#str.
    def exitStr(self, ctx:YAPLParser.StrContext):
        pass


    # Enter a parse tree produced by YAPLParser#equal.
    def enterEqual(self, ctx:YAPLParser.EqualContext):
        pass

    # Exit a parse tree produced by YAPLParser#equal.
    def exitEqual(self, ctx:YAPLParser.EqualContext):
        pass


    # Enter a parse tree produced by YAPLParser#isVoid.
    def enterIsVoid(self, ctx:YAPLParser.IsVoidContext):
        pass

    # Exit a parse tree produced by YAPLParser#isVoid.
    def exitIsVoid(self, ctx:YAPLParser.IsVoidContext):
        pass


    # Enter a parse tree produced by YAPLParser#true.
    def enterTrue(self, ctx:YAPLParser.TrueContext):
        pass

    # Exit a parse tree produced by YAPLParser#true.
    def exitTrue(self, ctx:YAPLParser.TrueContext):
        pass


    # Enter a parse tree produced by YAPLParser#lessEqual.
    def enterLessEqual(self, ctx:YAPLParser.LessEqualContext):
        pass

    # Exit a parse tree produced by YAPLParser#lessEqual.
    def exitLessEqual(self, ctx:YAPLParser.LessEqualContext):
        pass



del YAPLParser
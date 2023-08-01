// Generated from YAPL.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.tree.ParseTreeListener;

/**
 * This interface defines a complete listener for a parse tree produced by
 * {@link YAPLParser}.
 */
public interface YAPLListener extends ParseTreeListener {
	/**
	 * Enter a parse tree produced by {@link YAPLParser#start}.
	 * @param ctx the parse tree
	 */
	void enterStart(YAPLParser.StartContext ctx);
	/**
	 * Exit a parse tree produced by {@link YAPLParser#start}.
	 * @param ctx the parse tree
	 */
	void exitStart(YAPLParser.StartContext ctx);
	/**
	 * Enter a parse tree produced by the {@code class_list}
	 * labeled alternative in {@link YAPLParser#program}.
	 * @param ctx the parse tree
	 */
	void enterClass_list(YAPLParser.Class_listContext ctx);
	/**
	 * Exit a parse tree produced by the {@code class_list}
	 * labeled alternative in {@link YAPLParser#program}.
	 * @param ctx the parse tree
	 */
	void exitClass_list(YAPLParser.Class_listContext ctx);
	/**
	 * Enter a parse tree produced by the {@code end}
	 * labeled alternative in {@link YAPLParser#program}.
	 * @param ctx the parse tree
	 */
	void enterEnd(YAPLParser.EndContext ctx);
	/**
	 * Exit a parse tree produced by the {@code end}
	 * labeled alternative in {@link YAPLParser#program}.
	 * @param ctx the parse tree
	 */
	void exitEnd(YAPLParser.EndContext ctx);
	/**
	 * Enter a parse tree produced by {@link YAPLParser#class_exp}.
	 * @param ctx the parse tree
	 */
	void enterClass_exp(YAPLParser.Class_expContext ctx);
	/**
	 * Exit a parse tree produced by {@link YAPLParser#class_exp}.
	 * @param ctx the parse tree
	 */
	void exitClass_exp(YAPLParser.Class_expContext ctx);
	/**
	 * Enter a parse tree produced by the {@code method}
	 * labeled alternative in {@link YAPLParser#feature}.
	 * @param ctx the parse tree
	 */
	void enterMethod(YAPLParser.MethodContext ctx);
	/**
	 * Exit a parse tree produced by the {@code method}
	 * labeled alternative in {@link YAPLParser#feature}.
	 * @param ctx the parse tree
	 */
	void exitMethod(YAPLParser.MethodContext ctx);
	/**
	 * Enter a parse tree produced by the {@code attribute}
	 * labeled alternative in {@link YAPLParser#feature}.
	 * @param ctx the parse tree
	 */
	void enterAttribute(YAPLParser.AttributeContext ctx);
	/**
	 * Exit a parse tree produced by the {@code attribute}
	 * labeled alternative in {@link YAPLParser#feature}.
	 * @param ctx the parse tree
	 */
	void exitAttribute(YAPLParser.AttributeContext ctx);
	/**
	 * Enter a parse tree produced by {@link YAPLParser#formal}.
	 * @param ctx the parse tree
	 */
	void enterFormal(YAPLParser.FormalContext ctx);
	/**
	 * Exit a parse tree produced by {@link YAPLParser#formal}.
	 * @param ctx the parse tree
	 */
	void exitFormal(YAPLParser.FormalContext ctx);
	/**
	 * Enter a parse tree produced by {@link YAPLParser#declaration}.
	 * @param ctx the parse tree
	 */
	void enterDeclaration(YAPLParser.DeclarationContext ctx);
	/**
	 * Exit a parse tree produced by {@link YAPLParser#declaration}.
	 * @param ctx the parse tree
	 */
	void exitDeclaration(YAPLParser.DeclarationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code letIn}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLetIn(YAPLParser.LetInContext ctx);
	/**
	 * Exit a parse tree produced by the {@code letIn}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLetIn(YAPLParser.LetInContext ctx);
	/**
	 * Enter a parse tree produced by the {@code minus}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterMinus(YAPLParser.MinusContext ctx);
	/**
	 * Exit a parse tree produced by the {@code minus}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitMinus(YAPLParser.MinusContext ctx);
	/**
	 * Enter a parse tree produced by the {@code negation}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNegation(YAPLParser.NegationContext ctx);
	/**
	 * Exit a parse tree produced by the {@code negation}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNegation(YAPLParser.NegationContext ctx);
	/**
	 * Enter a parse tree produced by the {@code dispatch}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterDispatch(YAPLParser.DispatchContext ctx);
	/**
	 * Exit a parse tree produced by the {@code dispatch}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitDispatch(YAPLParser.DispatchContext ctx);
	/**
	 * Enter a parse tree produced by the {@code while}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterWhile(YAPLParser.WhileContext ctx);
	/**
	 * Exit a parse tree produced by the {@code while}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitWhile(YAPLParser.WhileContext ctx);
	/**
	 * Enter a parse tree produced by the {@code division}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterDivision(YAPLParser.DivisionContext ctx);
	/**
	 * Exit a parse tree produced by the {@code division}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitDivision(YAPLParser.DivisionContext ctx);
	/**
	 * Enter a parse tree produced by the {@code newObject}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNewObject(YAPLParser.NewObjectContext ctx);
	/**
	 * Exit a parse tree produced by the {@code newObject}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNewObject(YAPLParser.NewObjectContext ctx);
	/**
	 * Enter a parse tree produced by the {@code lessThan}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLessThan(YAPLParser.LessThanContext ctx);
	/**
	 * Exit a parse tree produced by the {@code lessThan}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLessThan(YAPLParser.LessThanContext ctx);
	/**
	 * Enter a parse tree produced by the {@code block}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterBlock(YAPLParser.BlockContext ctx);
	/**
	 * Exit a parse tree produced by the {@code block}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitBlock(YAPLParser.BlockContext ctx);
	/**
	 * Enter a parse tree produced by the {@code negInteger}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterNegInteger(YAPLParser.NegIntegerContext ctx);
	/**
	 * Exit a parse tree produced by the {@code negInteger}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitNegInteger(YAPLParser.NegIntegerContext ctx);
	/**
	 * Enter a parse tree produced by the {@code id}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterId(YAPLParser.IdContext ctx);
	/**
	 * Exit a parse tree produced by the {@code id}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitId(YAPLParser.IdContext ctx);
	/**
	 * Enter a parse tree produced by the {@code if}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterIf(YAPLParser.IfContext ctx);
	/**
	 * Exit a parse tree produced by the {@code if}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitIf(YAPLParser.IfContext ctx);
	/**
	 * Enter a parse tree produced by the {@code case}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterCase(YAPLParser.CaseContext ctx);
	/**
	 * Exit a parse tree produced by the {@code case}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitCase(YAPLParser.CaseContext ctx);
	/**
	 * Enter a parse tree produced by the {@code add}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAdd(YAPLParser.AddContext ctx);
	/**
	 * Exit a parse tree produced by the {@code add}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAdd(YAPLParser.AddContext ctx);
	/**
	 * Enter a parse tree produced by the {@code star}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterStar(YAPLParser.StarContext ctx);
	/**
	 * Exit a parse tree produced by the {@code star}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitStar(YAPLParser.StarContext ctx);
	/**
	 * Enter a parse tree produced by the {@code assignment}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterAssignment(YAPLParser.AssignmentContext ctx);
	/**
	 * Exit a parse tree produced by the {@code assignment}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitAssignment(YAPLParser.AssignmentContext ctx);
	/**
	 * Enter a parse tree produced by the {@code false}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterFalse(YAPLParser.FalseContext ctx);
	/**
	 * Exit a parse tree produced by the {@code false}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitFalse(YAPLParser.FalseContext ctx);
	/**
	 * Enter a parse tree produced by the {@code parenthesis}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterParenthesis(YAPLParser.ParenthesisContext ctx);
	/**
	 * Exit a parse tree produced by the {@code parenthesis}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitParenthesis(YAPLParser.ParenthesisContext ctx);
	/**
	 * Enter a parse tree produced by the {@code int}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterInt(YAPLParser.IntContext ctx);
	/**
	 * Exit a parse tree produced by the {@code int}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitInt(YAPLParser.IntContext ctx);
	/**
	 * Enter a parse tree produced by the {@code call}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterCall(YAPLParser.CallContext ctx);
	/**
	 * Exit a parse tree produced by the {@code call}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitCall(YAPLParser.CallContext ctx);
	/**
	 * Enter a parse tree produced by the {@code str}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterStr(YAPLParser.StrContext ctx);
	/**
	 * Exit a parse tree produced by the {@code str}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitStr(YAPLParser.StrContext ctx);
	/**
	 * Enter a parse tree produced by the {@code equal}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterEqual(YAPLParser.EqualContext ctx);
	/**
	 * Exit a parse tree produced by the {@code equal}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitEqual(YAPLParser.EqualContext ctx);
	/**
	 * Enter a parse tree produced by the {@code isVoid}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterIsVoid(YAPLParser.IsVoidContext ctx);
	/**
	 * Exit a parse tree produced by the {@code isVoid}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitIsVoid(YAPLParser.IsVoidContext ctx);
	/**
	 * Enter a parse tree produced by the {@code true}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterTrue(YAPLParser.TrueContext ctx);
	/**
	 * Exit a parse tree produced by the {@code true}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitTrue(YAPLParser.TrueContext ctx);
	/**
	 * Enter a parse tree produced by the {@code lessEqual}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void enterLessEqual(YAPLParser.LessEqualContext ctx);
	/**
	 * Exit a parse tree produced by the {@code lessEqual}
	 * labeled alternative in {@link YAPLParser#expr}.
	 * @param ctx the parse tree
	 */
	void exitLessEqual(YAPLParser.LessEqualContext ctx);
}
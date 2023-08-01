// Generated from YAPL.g4 by ANTLR 4.10.1
import org.antlr.v4.runtime.atn.*;
import org.antlr.v4.runtime.dfa.DFA;
import org.antlr.v4.runtime.*;
import org.antlr.v4.runtime.misc.*;
import org.antlr.v4.runtime.tree.*;
import java.util.List;
import java.util.Iterator;
import java.util.ArrayList;

@SuppressWarnings({"all", "warnings", "unchecked", "unused", "cast"})
public class YAPLParser extends Parser {
	static { RuntimeMetaData.checkVersion("4.10.1", RuntimeMetaData.VERSION); }

	protected static final DFA[] _decisionToDFA;
	protected static final PredictionContextCache _sharedContextCache =
		new PredictionContextCache();
	public static final int
		T__0=1, T__1=2, T__2=3, T__3=4, T__4=5, T__5=6, T__6=7, T__7=8, T__8=9, 
		T__9=10, OPEN_COMMENT=11, CLOSE_COMMENT=12, COMMENT=13, ONE_LINE_COMMENT=14, 
		WHITESPACE=15, CLASS=16, INHERITS=17, TRUE=18, FALSE=19, ASSIGNMENT=20, 
		IF=21, ELSE=22, THEN=23, FI=24, WHILE=25, LOOP=26, POOL=27, LET=28, IN=29, 
		CASE=30, OF=31, ESAC=32, CASEARR=33, NEW=34, ISVOID=35, ADD=36, MINUS=37, 
		MULT=38, DIV=39, NOT=40, LT=41, LE=42, EQ=43, TYPE=44, STR=45, ID=46, 
		INT=47;
	public static final int
		RULE_start = 0, RULE_program = 1, RULE_class_exp = 2, RULE_feature = 3, 
		RULE_formal = 4, RULE_declaration = 5, RULE_expr = 6;
	private static String[] makeRuleNames() {
		return new String[] {
			"start", "program", "class_exp", "feature", "formal", "declaration", 
			"expr"
		};
	}
	public static final String[] ruleNames = makeRuleNames();

	private static String[] makeLiteralNames() {
		return new String[] {
			null, "';'", "'{'", "'}'", "'('", "','", "')'", "':'", "'@'", "'.'", 
			"'~'", "'(*'", "'*)'", null, null, null, null, null, null, null, "'<-'", 
			null, null, null, null, null, null, null, null, null, null, null, null, 
			"'=>'", null, null, "'+'", "'-'", "'*'", "'/'", null, "'<'", "'<='", 
			"'='"
		};
	}
	private static final String[] _LITERAL_NAMES = makeLiteralNames();
	private static String[] makeSymbolicNames() {
		return new String[] {
			null, null, null, null, null, null, null, null, null, null, null, "OPEN_COMMENT", 
			"CLOSE_COMMENT", "COMMENT", "ONE_LINE_COMMENT", "WHITESPACE", "CLASS", 
			"INHERITS", "TRUE", "FALSE", "ASSIGNMENT", "IF", "ELSE", "THEN", "FI", 
			"WHILE", "LOOP", "POOL", "LET", "IN", "CASE", "OF", "ESAC", "CASEARR", 
			"NEW", "ISVOID", "ADD", "MINUS", "MULT", "DIV", "NOT", "LT", "LE", "EQ", 
			"TYPE", "STR", "ID", "INT"
		};
	}
	private static final String[] _SYMBOLIC_NAMES = makeSymbolicNames();
	public static final Vocabulary VOCABULARY = new VocabularyImpl(_LITERAL_NAMES, _SYMBOLIC_NAMES);

	/**
	 * @deprecated Use {@link #VOCABULARY} instead.
	 */
	@Deprecated
	public static final String[] tokenNames;
	static {
		tokenNames = new String[_SYMBOLIC_NAMES.length];
		for (int i = 0; i < tokenNames.length; i++) {
			tokenNames[i] = VOCABULARY.getLiteralName(i);
			if (tokenNames[i] == null) {
				tokenNames[i] = VOCABULARY.getSymbolicName(i);
			}

			if (tokenNames[i] == null) {
				tokenNames[i] = "<INVALID>";
			}
		}
	}

	@Override
	@Deprecated
	public String[] getTokenNames() {
		return tokenNames;
	}

	@Override

	public Vocabulary getVocabulary() {
		return VOCABULARY;
	}

	@Override
	public String getGrammarFileName() { return "YAPL.g4"; }

	@Override
	public String[] getRuleNames() { return ruleNames; }

	@Override
	public String getSerializedATN() { return _serializedATN; }

	@Override
	public ATN getATN() { return _ATN; }

	public YAPLParser(TokenStream input) {
		super(input);
		_interp = new ParserATNSimulator(this,_ATN,_decisionToDFA,_sharedContextCache);
	}

	public static class StartContext extends ParserRuleContext {
		public ProgramContext program() {
			return getRuleContext(ProgramContext.class,0);
		}
		public StartContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_start; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterStart(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitStart(this);
		}
	}

	public final StartContext start() throws RecognitionException {
		StartContext _localctx = new StartContext(_ctx, getState());
		enterRule(_localctx, 0, RULE_start);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(14);
			program();
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ProgramContext extends ParserRuleContext {
		public ProgramContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_program; }
	 
		public ProgramContext() { }
		public void copyFrom(ProgramContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class EndContext extends ProgramContext {
		public TerminalNode EOF() { return getToken(YAPLParser.EOF, 0); }
		public EndContext(ProgramContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterEnd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitEnd(this);
		}
	}
	public static class Class_listContext extends ProgramContext {
		public Class_expContext class_exp() {
			return getRuleContext(Class_expContext.class,0);
		}
		public ProgramContext program() {
			return getRuleContext(ProgramContext.class,0);
		}
		public Class_listContext(ProgramContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterClass_list(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitClass_list(this);
		}
	}

	public final ProgramContext program() throws RecognitionException {
		ProgramContext _localctx = new ProgramContext(_ctx, getState());
		enterRule(_localctx, 2, RULE_program);
		try {
			setState(21);
			_errHandler.sync(this);
			switch (_input.LA(1)) {
			case CLASS:
				_localctx = new Class_listContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(16);
				class_exp();
				setState(17);
				match(T__0);
				setState(18);
				program();
				}
				break;
			case EOF:
				_localctx = new EndContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(20);
				match(EOF);
				}
				break;
			default:
				throw new NoViableAltException(this);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class Class_expContext extends ParserRuleContext {
		public TerminalNode CLASS() { return getToken(YAPLParser.CLASS, 0); }
		public List<TerminalNode> TYPE() { return getTokens(YAPLParser.TYPE); }
		public TerminalNode TYPE(int i) {
			return getToken(YAPLParser.TYPE, i);
		}
		public TerminalNode INHERITS() { return getToken(YAPLParser.INHERITS, 0); }
		public List<FeatureContext> feature() {
			return getRuleContexts(FeatureContext.class);
		}
		public FeatureContext feature(int i) {
			return getRuleContext(FeatureContext.class,i);
		}
		public Class_expContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_class_exp; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterClass_exp(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitClass_exp(this);
		}
	}

	public final Class_expContext class_exp() throws RecognitionException {
		Class_expContext _localctx = new Class_expContext(_ctx, getState());
		enterRule(_localctx, 4, RULE_class_exp);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(23);
			match(CLASS);
			setState(24);
			match(TYPE);
			setState(27);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==INHERITS) {
				{
				setState(25);
				match(INHERITS);
				setState(26);
				match(TYPE);
				}
			}

			setState(29);
			match(T__1);
			setState(35);
			_errHandler.sync(this);
			_la = _input.LA(1);
			while (_la==ID) {
				{
				{
				setState(30);
				feature();
				setState(31);
				match(T__0);
				}
				}
				setState(37);
				_errHandler.sync(this);
				_la = _input.LA(1);
			}
			setState(38);
			match(T__2);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FeatureContext extends ParserRuleContext {
		public FeatureContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_feature; }
	 
		public FeatureContext() { }
		public void copyFrom(FeatureContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class MethodContext extends FeatureContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode TYPE() { return getToken(YAPLParser.TYPE, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public List<FormalContext> formal() {
			return getRuleContexts(FormalContext.class);
		}
		public FormalContext formal(int i) {
			return getRuleContext(FormalContext.class,i);
		}
		public MethodContext(FeatureContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterMethod(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitMethod(this);
		}
	}
	public static class AttributeContext extends FeatureContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode TYPE() { return getToken(YAPLParser.TYPE, 0); }
		public TerminalNode ASSIGNMENT() { return getToken(YAPLParser.ASSIGNMENT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AttributeContext(FeatureContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterAttribute(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitAttribute(this);
		}
	}

	public final FeatureContext feature() throws RecognitionException {
		FeatureContext _localctx = new FeatureContext(_ctx, getState());
		enterRule(_localctx, 6, RULE_feature);
		int _la;
		try {
			setState(69);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,6,_ctx) ) {
			case 1:
				_localctx = new MethodContext(_localctx);
				enterOuterAlt(_localctx, 1);
				{
				setState(40);
				match(ID);
				setState(41);
				match(T__3);
				setState(52);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==ID) {
					{
					{
					setState(42);
					formal();
					setState(47);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__4) {
						{
						{
						setState(43);
						match(T__4);
						setState(44);
						formal();
						}
						}
						setState(49);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
					}
					setState(54);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(55);
				match(T__5);
				setState(56);
				match(T__6);
				setState(57);
				match(TYPE);
				setState(58);
				match(T__1);
				setState(59);
				expr(0);
				setState(60);
				match(T__2);
				}
				break;
			case 2:
				_localctx = new AttributeContext(_localctx);
				enterOuterAlt(_localctx, 2);
				{
				setState(62);
				match(ID);
				setState(63);
				match(T__6);
				setState(64);
				match(TYPE);
				setState(67);
				_errHandler.sync(this);
				_la = _input.LA(1);
				if (_la==ASSIGNMENT) {
					{
					setState(65);
					match(ASSIGNMENT);
					setState(66);
					expr(0);
					}
				}

				}
				break;
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class FormalContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode TYPE() { return getToken(YAPLParser.TYPE, 0); }
		public FormalContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_formal; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterFormal(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitFormal(this);
		}
	}

	public final FormalContext formal() throws RecognitionException {
		FormalContext _localctx = new FormalContext(_ctx, getState());
		enterRule(_localctx, 8, RULE_formal);
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(71);
			match(ID);
			setState(72);
			match(T__6);
			setState(73);
			match(TYPE);
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class DeclarationContext extends ParserRuleContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode TYPE() { return getToken(YAPLParser.TYPE, 0); }
		public TerminalNode ASSIGNMENT() { return getToken(YAPLParser.ASSIGNMENT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public DeclarationContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_declaration; }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterDeclaration(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitDeclaration(this);
		}
	}

	public final DeclarationContext declaration() throws RecognitionException {
		DeclarationContext _localctx = new DeclarationContext(_ctx, getState());
		enterRule(_localctx, 10, RULE_declaration);
		int _la;
		try {
			enterOuterAlt(_localctx, 1);
			{
			setState(75);
			match(ID);
			setState(76);
			match(T__6);
			setState(77);
			match(TYPE);
			setState(80);
			_errHandler.sync(this);
			_la = _input.LA(1);
			if (_la==ASSIGNMENT) {
				{
				setState(78);
				match(ASSIGNMENT);
				setState(79);
				expr(0);
				}
			}

			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			exitRule();
		}
		return _localctx;
	}

	public static class ExprContext extends ParserRuleContext {
		public ExprContext(ParserRuleContext parent, int invokingState) {
			super(parent, invokingState);
		}
		@Override public int getRuleIndex() { return RULE_expr; }
	 
		public ExprContext() { }
		public void copyFrom(ExprContext ctx) {
			super.copyFrom(ctx);
		}
	}
	public static class LetInContext extends ExprContext {
		public TerminalNode LET() { return getToken(YAPLParser.LET, 0); }
		public List<DeclarationContext> declaration() {
			return getRuleContexts(DeclarationContext.class);
		}
		public DeclarationContext declaration(int i) {
			return getRuleContext(DeclarationContext.class,i);
		}
		public TerminalNode IN() { return getToken(YAPLParser.IN, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public LetInContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterLetIn(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitLetIn(this);
		}
	}
	public static class MinusContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode MINUS() { return getToken(YAPLParser.MINUS, 0); }
		public MinusContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterMinus(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitMinus(this);
		}
	}
	public static class NegationContext extends ExprContext {
		public TerminalNode NOT() { return getToken(YAPLParser.NOT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public NegationContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterNegation(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitNegation(this);
		}
	}
	public static class DispatchContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode TYPE() { return getToken(YAPLParser.TYPE, 0); }
		public DispatchContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterDispatch(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitDispatch(this);
		}
	}
	public static class WhileContext extends ExprContext {
		public TerminalNode WHILE() { return getToken(YAPLParser.WHILE, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode LOOP() { return getToken(YAPLParser.LOOP, 0); }
		public TerminalNode POOL() { return getToken(YAPLParser.POOL, 0); }
		public WhileContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterWhile(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitWhile(this);
		}
	}
	public static class DivisionContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode DIV() { return getToken(YAPLParser.DIV, 0); }
		public DivisionContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterDivision(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitDivision(this);
		}
	}
	public static class NewObjectContext extends ExprContext {
		public TerminalNode NEW() { return getToken(YAPLParser.NEW, 0); }
		public TerminalNode TYPE() { return getToken(YAPLParser.TYPE, 0); }
		public NewObjectContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterNewObject(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitNewObject(this);
		}
	}
	public static class LessThanContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode LT() { return getToken(YAPLParser.LT, 0); }
		public LessThanContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterLessThan(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitLessThan(this);
		}
	}
	public static class BlockContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public BlockContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterBlock(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitBlock(this);
		}
	}
	public static class NegIntegerContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public NegIntegerContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterNegInteger(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitNegInteger(this);
		}
	}
	public static class IdContext extends ExprContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public IdContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterId(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitId(this);
		}
	}
	public static class IfContext extends ExprContext {
		public TerminalNode IF() { return getToken(YAPLParser.IF, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode THEN() { return getToken(YAPLParser.THEN, 0); }
		public TerminalNode ELSE() { return getToken(YAPLParser.ELSE, 0); }
		public TerminalNode FI() { return getToken(YAPLParser.FI, 0); }
		public IfContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterIf(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitIf(this);
		}
	}
	public static class CaseContext extends ExprContext {
		public TerminalNode CASE() { return getToken(YAPLParser.CASE, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode OF() { return getToken(YAPLParser.OF, 0); }
		public TerminalNode ESAC() { return getToken(YAPLParser.ESAC, 0); }
		public List<TerminalNode> ID() { return getTokens(YAPLParser.ID); }
		public TerminalNode ID(int i) {
			return getToken(YAPLParser.ID, i);
		}
		public List<TerminalNode> TYPE() { return getTokens(YAPLParser.TYPE); }
		public TerminalNode TYPE(int i) {
			return getToken(YAPLParser.TYPE, i);
		}
		public List<TerminalNode> CASEARR() { return getTokens(YAPLParser.CASEARR); }
		public TerminalNode CASEARR(int i) {
			return getToken(YAPLParser.CASEARR, i);
		}
		public CaseContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterCase(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitCase(this);
		}
	}
	public static class AddContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode ADD() { return getToken(YAPLParser.ADD, 0); }
		public AddContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterAdd(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitAdd(this);
		}
	}
	public static class StarContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode MULT() { return getToken(YAPLParser.MULT, 0); }
		public StarContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterStar(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitStar(this);
		}
	}
	public static class AssignmentContext extends ExprContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public TerminalNode ASSIGNMENT() { return getToken(YAPLParser.ASSIGNMENT, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public AssignmentContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterAssignment(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitAssignment(this);
		}
	}
	public static class FalseContext extends ExprContext {
		public TerminalNode FALSE() { return getToken(YAPLParser.FALSE, 0); }
		public FalseContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterFalse(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitFalse(this);
		}
	}
	public static class ParenthesisContext extends ExprContext {
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public ParenthesisContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterParenthesis(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitParenthesis(this);
		}
	}
	public static class IntContext extends ExprContext {
		public TerminalNode INT() { return getToken(YAPLParser.INT, 0); }
		public IntContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterInt(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitInt(this);
		}
	}
	public static class CallContext extends ExprContext {
		public TerminalNode ID() { return getToken(YAPLParser.ID, 0); }
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public CallContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterCall(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitCall(this);
		}
	}
	public static class StrContext extends ExprContext {
		public TerminalNode STR() { return getToken(YAPLParser.STR, 0); }
		public StrContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterStr(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitStr(this);
		}
	}
	public static class EqualContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode EQ() { return getToken(YAPLParser.EQ, 0); }
		public EqualContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterEqual(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitEqual(this);
		}
	}
	public static class IsVoidContext extends ExprContext {
		public TerminalNode ISVOID() { return getToken(YAPLParser.ISVOID, 0); }
		public ExprContext expr() {
			return getRuleContext(ExprContext.class,0);
		}
		public IsVoidContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterIsVoid(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitIsVoid(this);
		}
	}
	public static class TrueContext extends ExprContext {
		public TerminalNode TRUE() { return getToken(YAPLParser.TRUE, 0); }
		public TrueContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterTrue(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitTrue(this);
		}
	}
	public static class LessEqualContext extends ExprContext {
		public List<ExprContext> expr() {
			return getRuleContexts(ExprContext.class);
		}
		public ExprContext expr(int i) {
			return getRuleContext(ExprContext.class,i);
		}
		public TerminalNode LE() { return getToken(YAPLParser.LE, 0); }
		public LessEqualContext(ExprContext ctx) { copyFrom(ctx); }
		@Override
		public void enterRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).enterLessEqual(this);
		}
		@Override
		public void exitRule(ParseTreeListener listener) {
			if ( listener instanceof YAPLListener ) ((YAPLListener)listener).exitLessEqual(this);
		}
	}

	public final ExprContext expr() throws RecognitionException {
		return expr(0);
	}

	private ExprContext expr(int _p) throws RecognitionException {
		ParserRuleContext _parentctx = _ctx;
		int _parentState = getState();
		ExprContext _localctx = new ExprContext(_ctx, _parentState);
		ExprContext _prevctx = _localctx;
		int _startState = 12;
		enterRecursionRule(_localctx, 12, RULE_expr, _p);
		int _la;
		try {
			int _alt;
			enterOuterAlt(_localctx, 1);
			{
			setState(171);
			_errHandler.sync(this);
			switch ( getInterpreter().adaptivePredict(_input,13,_ctx) ) {
			case 1:
				{
				_localctx = new CallContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;

				setState(83);
				match(ID);
				setState(84);
				match(T__3);
				setState(95);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__3) | (1L << T__9) | (1L << TRUE) | (1L << FALSE) | (1L << IF) | (1L << WHILE) | (1L << LET) | (1L << CASE) | (1L << NEW) | (1L << ISVOID) | (1L << NOT) | (1L << STR) | (1L << ID) | (1L << INT))) != 0)) {
					{
					{
					setState(85);
					expr(0);
					setState(90);
					_errHandler.sync(this);
					_la = _input.LA(1);
					while (_la==T__4) {
						{
						{
						setState(86);
						match(T__4);
						setState(87);
						expr(0);
						}
						}
						setState(92);
						_errHandler.sync(this);
						_la = _input.LA(1);
					}
					}
					}
					setState(97);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(98);
				match(T__5);
				}
				break;
			case 2:
				{
				_localctx = new IfContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(99);
				match(IF);
				setState(100);
				expr(0);
				setState(101);
				match(THEN);
				setState(102);
				expr(0);
				setState(103);
				match(ELSE);
				setState(104);
				expr(0);
				setState(105);
				match(FI);
				}
				break;
			case 3:
				{
				_localctx = new WhileContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(107);
				match(WHILE);
				setState(108);
				expr(0);
				setState(109);
				match(LOOP);
				setState(110);
				expr(0);
				setState(111);
				match(POOL);
				}
				break;
			case 4:
				{
				_localctx = new BlockContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(113);
				match(T__1);
				setState(117); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(114);
					expr(0);
					setState(115);
					match(T__0);
					}
					}
					setState(119); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( (((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__3) | (1L << T__9) | (1L << TRUE) | (1L << FALSE) | (1L << IF) | (1L << WHILE) | (1L << LET) | (1L << CASE) | (1L << NEW) | (1L << ISVOID) | (1L << NOT) | (1L << STR) | (1L << ID) | (1L << INT))) != 0) );
				setState(121);
				match(T__2);
				}
				break;
			case 5:
				{
				_localctx = new LetInContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(123);
				match(LET);
				setState(124);
				declaration();
				setState(129);
				_errHandler.sync(this);
				_la = _input.LA(1);
				while (_la==T__4) {
					{
					{
					setState(125);
					match(T__4);
					setState(126);
					declaration();
					}
					}
					setState(131);
					_errHandler.sync(this);
					_la = _input.LA(1);
				}
				setState(132);
				match(IN);
				setState(133);
				expr(20);
				}
				break;
			case 6:
				{
				_localctx = new CaseContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(135);
				match(CASE);
				setState(136);
				expr(0);
				setState(137);
				match(OF);
				setState(145); 
				_errHandler.sync(this);
				_la = _input.LA(1);
				do {
					{
					{
					setState(138);
					match(ID);
					setState(139);
					match(T__6);
					setState(140);
					match(TYPE);
					setState(141);
					match(CASEARR);
					setState(142);
					expr(0);
					setState(143);
					match(T__0);
					}
					}
					setState(147); 
					_errHandler.sync(this);
					_la = _input.LA(1);
				} while ( _la==ID );
				setState(149);
				match(ESAC);
				}
				break;
			case 7:
				{
				_localctx = new NewObjectContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(151);
				match(NEW);
				setState(152);
				match(TYPE);
				}
				break;
			case 8:
				{
				_localctx = new IsVoidContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(153);
				match(ISVOID);
				setState(154);
				expr(17);
				}
				break;
			case 9:
				{
				_localctx = new NegIntegerContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(155);
				match(T__9);
				setState(156);
				expr(12);
				}
				break;
			case 10:
				{
				_localctx = new NegationContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(157);
				match(NOT);
				setState(158);
				expr(8);
				}
				break;
			case 11:
				{
				_localctx = new ParenthesisContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(159);
				match(T__3);
				setState(160);
				expr(0);
				setState(161);
				match(T__5);
				}
				break;
			case 12:
				{
				_localctx = new IntContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(163);
				match(INT);
				}
				break;
			case 13:
				{
				_localctx = new StrContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(164);
				match(STR);
				}
				break;
			case 14:
				{
				_localctx = new TrueContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(165);
				match(TRUE);
				}
				break;
			case 15:
				{
				_localctx = new FalseContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(166);
				match(FALSE);
				}
				break;
			case 16:
				{
				_localctx = new IdContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(167);
				match(ID);
				}
				break;
			case 17:
				{
				_localctx = new AssignmentContext(_localctx);
				_ctx = _localctx;
				_prevctx = _localctx;
				setState(168);
				match(ID);
				setState(169);
				match(ASSIGNMENT);
				setState(170);
				expr(1);
				}
				break;
			}
			_ctx.stop = _input.LT(-1);
			setState(218);
			_errHandler.sync(this);
			_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			while ( _alt!=2 && _alt!=org.antlr.v4.runtime.atn.ATN.INVALID_ALT_NUMBER ) {
				if ( _alt==1 ) {
					if ( _parseListeners!=null ) triggerExitRuleEvent();
					_prevctx = _localctx;
					{
					setState(216);
					_errHandler.sync(this);
					switch ( getInterpreter().adaptivePredict(_input,17,_ctx) ) {
					case 1:
						{
						_localctx = new StarContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(173);
						if (!(precpred(_ctx, 16))) throw new FailedPredicateException(this, "precpred(_ctx, 16)");
						setState(174);
						match(MULT);
						setState(175);
						expr(17);
						}
						break;
					case 2:
						{
						_localctx = new DivisionContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(176);
						if (!(precpred(_ctx, 15))) throw new FailedPredicateException(this, "precpred(_ctx, 15)");
						setState(177);
						match(DIV);
						setState(178);
						expr(16);
						}
						break;
					case 3:
						{
						_localctx = new AddContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(179);
						if (!(precpred(_ctx, 14))) throw new FailedPredicateException(this, "precpred(_ctx, 14)");
						setState(180);
						match(ADD);
						setState(181);
						expr(15);
						}
						break;
					case 4:
						{
						_localctx = new MinusContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(182);
						if (!(precpred(_ctx, 13))) throw new FailedPredicateException(this, "precpred(_ctx, 13)");
						setState(183);
						match(MINUS);
						setState(184);
						expr(14);
						}
						break;
					case 5:
						{
						_localctx = new LessThanContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(185);
						if (!(precpred(_ctx, 11))) throw new FailedPredicateException(this, "precpred(_ctx, 11)");
						setState(186);
						match(LT);
						setState(187);
						expr(12);
						}
						break;
					case 6:
						{
						_localctx = new LessEqualContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(188);
						if (!(precpred(_ctx, 10))) throw new FailedPredicateException(this, "precpred(_ctx, 10)");
						setState(189);
						match(LE);
						setState(190);
						expr(11);
						}
						break;
					case 7:
						{
						_localctx = new EqualContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(191);
						if (!(precpred(_ctx, 9))) throw new FailedPredicateException(this, "precpred(_ctx, 9)");
						setState(192);
						match(EQ);
						setState(193);
						expr(10);
						}
						break;
					case 8:
						{
						_localctx = new DispatchContext(new ExprContext(_parentctx, _parentState));
						pushNewRecursionContext(_localctx, _startState, RULE_expr);
						setState(194);
						if (!(precpred(_ctx, 25))) throw new FailedPredicateException(this, "precpred(_ctx, 25)");
						setState(197);
						_errHandler.sync(this);
						_la = _input.LA(1);
						if (_la==T__7) {
							{
							setState(195);
							match(T__7);
							setState(196);
							match(TYPE);
							}
						}

						setState(199);
						match(T__8);
						setState(200);
						match(ID);
						setState(201);
						match(T__3);
						setState(212);
						_errHandler.sync(this);
						_la = _input.LA(1);
						while ((((_la) & ~0x3f) == 0 && ((1L << _la) & ((1L << T__1) | (1L << T__3) | (1L << T__9) | (1L << TRUE) | (1L << FALSE) | (1L << IF) | (1L << WHILE) | (1L << LET) | (1L << CASE) | (1L << NEW) | (1L << ISVOID) | (1L << NOT) | (1L << STR) | (1L << ID) | (1L << INT))) != 0)) {
							{
							{
							setState(202);
							expr(0);
							setState(207);
							_errHandler.sync(this);
							_la = _input.LA(1);
							while (_la==T__4) {
								{
								{
								setState(203);
								match(T__4);
								setState(204);
								expr(0);
								}
								}
								setState(209);
								_errHandler.sync(this);
								_la = _input.LA(1);
							}
							}
							}
							setState(214);
							_errHandler.sync(this);
							_la = _input.LA(1);
						}
						setState(215);
						match(T__5);
						}
						break;
					}
					} 
				}
				setState(220);
				_errHandler.sync(this);
				_alt = getInterpreter().adaptivePredict(_input,18,_ctx);
			}
			}
		}
		catch (RecognitionException re) {
			_localctx.exception = re;
			_errHandler.reportError(this, re);
			_errHandler.recover(this, re);
		}
		finally {
			unrollRecursionContexts(_parentctx);
		}
		return _localctx;
	}

	public boolean sempred(RuleContext _localctx, int ruleIndex, int predIndex) {
		switch (ruleIndex) {
		case 6:
			return expr_sempred((ExprContext)_localctx, predIndex);
		}
		return true;
	}
	private boolean expr_sempred(ExprContext _localctx, int predIndex) {
		switch (predIndex) {
		case 0:
			return precpred(_ctx, 16);
		case 1:
			return precpred(_ctx, 15);
		case 2:
			return precpred(_ctx, 14);
		case 3:
			return precpred(_ctx, 13);
		case 4:
			return precpred(_ctx, 11);
		case 5:
			return precpred(_ctx, 10);
		case 6:
			return precpred(_ctx, 9);
		case 7:
			return precpred(_ctx, 25);
		}
		return true;
	}

	public static final String _serializedATN =
		"\u0004\u0001/\u00de\u0002\u0000\u0007\u0000\u0002\u0001\u0007\u0001\u0002"+
		"\u0002\u0007\u0002\u0002\u0003\u0007\u0003\u0002\u0004\u0007\u0004\u0002"+
		"\u0005\u0007\u0005\u0002\u0006\u0007\u0006\u0001\u0000\u0001\u0000\u0001"+
		"\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0001\u0003\u0001\u0016"+
		"\b\u0001\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0003\u0002\u001c"+
		"\b\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0001\u0002\u0005\u0002\""+
		"\b\u0002\n\u0002\f\u0002%\t\u0002\u0001\u0002\u0001\u0002\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0005\u0003.\b\u0003"+
		"\n\u0003\f\u00031\t\u0003\u0005\u00033\b\u0003\n\u0003\f\u00036\t\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003\u0001\u0003"+
		"\u0003\u0003D\b\u0003\u0003\u0003F\b\u0003\u0001\u0004\u0001\u0004\u0001"+
		"\u0004\u0001\u0004\u0001\u0005\u0001\u0005\u0001\u0005\u0001\u0005\u0001"+
		"\u0005\u0003\u0005Q\b\u0005\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0005\u0006Y\b\u0006\n\u0006\f\u0006\\"+
		"\t\u0006\u0005\u0006^\b\u0006\n\u0006\f\u0006a\t\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001"+
		"\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0004"+
		"\u0006v\b\u0006\u000b\u0006\f\u0006w\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0005\u0006\u0080\b\u0006\n\u0006"+
		"\f\u0006\u0083\t\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0004\u0006\u0092\b\u0006\u000b\u0006"+
		"\f\u0006\u0093\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0003\u0006"+
		"\u00ac\b\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0003\u0006\u00c6\b\u0006\u0001\u0006\u0001\u0006\u0001\u0006"+
		"\u0001\u0006\u0001\u0006\u0001\u0006\u0005\u0006\u00ce\b\u0006\n\u0006"+
		"\f\u0006\u00d1\t\u0006\u0005\u0006\u00d3\b\u0006\n\u0006\f\u0006\u00d6"+
		"\t\u0006\u0001\u0006\u0005\u0006\u00d9\b\u0006\n\u0006\f\u0006\u00dc\t"+
		"\u0006\u0001\u0006\u0000\u0001\f\u0007\u0000\u0002\u0004\u0006\b\n\f\u0000"+
		"\u0000\u00fe\u0000\u000e\u0001\u0000\u0000\u0000\u0002\u0015\u0001\u0000"+
		"\u0000\u0000\u0004\u0017\u0001\u0000\u0000\u0000\u0006E\u0001\u0000\u0000"+
		"\u0000\bG\u0001\u0000\u0000\u0000\nK\u0001\u0000\u0000\u0000\f\u00ab\u0001"+
		"\u0000\u0000\u0000\u000e\u000f\u0003\u0002\u0001\u0000\u000f\u0001\u0001"+
		"\u0000\u0000\u0000\u0010\u0011\u0003\u0004\u0002\u0000\u0011\u0012\u0005"+
		"\u0001\u0000\u0000\u0012\u0013\u0003\u0002\u0001\u0000\u0013\u0016\u0001"+
		"\u0000\u0000\u0000\u0014\u0016\u0005\u0000\u0000\u0001\u0015\u0010\u0001"+
		"\u0000\u0000\u0000\u0015\u0014\u0001\u0000\u0000\u0000\u0016\u0003\u0001"+
		"\u0000\u0000\u0000\u0017\u0018\u0005\u0010\u0000\u0000\u0018\u001b\u0005"+
		",\u0000\u0000\u0019\u001a\u0005\u0011\u0000\u0000\u001a\u001c\u0005,\u0000"+
		"\u0000\u001b\u0019\u0001\u0000\u0000\u0000\u001b\u001c\u0001\u0000\u0000"+
		"\u0000\u001c\u001d\u0001\u0000\u0000\u0000\u001d#\u0005\u0002\u0000\u0000"+
		"\u001e\u001f\u0003\u0006\u0003\u0000\u001f \u0005\u0001\u0000\u0000 \""+
		"\u0001\u0000\u0000\u0000!\u001e\u0001\u0000\u0000\u0000\"%\u0001\u0000"+
		"\u0000\u0000#!\u0001\u0000\u0000\u0000#$\u0001\u0000\u0000\u0000$&\u0001"+
		"\u0000\u0000\u0000%#\u0001\u0000\u0000\u0000&\'\u0005\u0003\u0000\u0000"+
		"\'\u0005\u0001\u0000\u0000\u0000()\u0005.\u0000\u0000)4\u0005\u0004\u0000"+
		"\u0000*/\u0003\b\u0004\u0000+,\u0005\u0005\u0000\u0000,.\u0003\b\u0004"+
		"\u0000-+\u0001\u0000\u0000\u0000.1\u0001\u0000\u0000\u0000/-\u0001\u0000"+
		"\u0000\u0000/0\u0001\u0000\u0000\u000003\u0001\u0000\u0000\u00001/\u0001"+
		"\u0000\u0000\u00002*\u0001\u0000\u0000\u000036\u0001\u0000\u0000\u0000"+
		"42\u0001\u0000\u0000\u000045\u0001\u0000\u0000\u000057\u0001\u0000\u0000"+
		"\u000064\u0001\u0000\u0000\u000078\u0005\u0006\u0000\u000089\u0005\u0007"+
		"\u0000\u00009:\u0005,\u0000\u0000:;\u0005\u0002\u0000\u0000;<\u0003\f"+
		"\u0006\u0000<=\u0005\u0003\u0000\u0000=F\u0001\u0000\u0000\u0000>?\u0005"+
		".\u0000\u0000?@\u0005\u0007\u0000\u0000@C\u0005,\u0000\u0000AB\u0005\u0014"+
		"\u0000\u0000BD\u0003\f\u0006\u0000CA\u0001\u0000\u0000\u0000CD\u0001\u0000"+
		"\u0000\u0000DF\u0001\u0000\u0000\u0000E(\u0001\u0000\u0000\u0000E>\u0001"+
		"\u0000\u0000\u0000F\u0007\u0001\u0000\u0000\u0000GH\u0005.\u0000\u0000"+
		"HI\u0005\u0007\u0000\u0000IJ\u0005,\u0000\u0000J\t\u0001\u0000\u0000\u0000"+
		"KL\u0005.\u0000\u0000LM\u0005\u0007\u0000\u0000MP\u0005,\u0000\u0000N"+
		"O\u0005\u0014\u0000\u0000OQ\u0003\f\u0006\u0000PN\u0001\u0000\u0000\u0000"+
		"PQ\u0001\u0000\u0000\u0000Q\u000b\u0001\u0000\u0000\u0000RS\u0006\u0006"+
		"\uffff\uffff\u0000ST\u0005.\u0000\u0000T_\u0005\u0004\u0000\u0000UZ\u0003"+
		"\f\u0006\u0000VW\u0005\u0005\u0000\u0000WY\u0003\f\u0006\u0000XV\u0001"+
		"\u0000\u0000\u0000Y\\\u0001\u0000\u0000\u0000ZX\u0001\u0000\u0000\u0000"+
		"Z[\u0001\u0000\u0000\u0000[^\u0001\u0000\u0000\u0000\\Z\u0001\u0000\u0000"+
		"\u0000]U\u0001\u0000\u0000\u0000^a\u0001\u0000\u0000\u0000_]\u0001\u0000"+
		"\u0000\u0000_`\u0001\u0000\u0000\u0000`b\u0001\u0000\u0000\u0000a_\u0001"+
		"\u0000\u0000\u0000b\u00ac\u0005\u0006\u0000\u0000cd\u0005\u0015\u0000"+
		"\u0000de\u0003\f\u0006\u0000ef\u0005\u0017\u0000\u0000fg\u0003\f\u0006"+
		"\u0000gh\u0005\u0016\u0000\u0000hi\u0003\f\u0006\u0000ij\u0005\u0018\u0000"+
		"\u0000j\u00ac\u0001\u0000\u0000\u0000kl\u0005\u0019\u0000\u0000lm\u0003"+
		"\f\u0006\u0000mn\u0005\u001a\u0000\u0000no\u0003\f\u0006\u0000op\u0005"+
		"\u001b\u0000\u0000p\u00ac\u0001\u0000\u0000\u0000qu\u0005\u0002\u0000"+
		"\u0000rs\u0003\f\u0006\u0000st\u0005\u0001\u0000\u0000tv\u0001\u0000\u0000"+
		"\u0000ur\u0001\u0000\u0000\u0000vw\u0001\u0000\u0000\u0000wu\u0001\u0000"+
		"\u0000\u0000wx\u0001\u0000\u0000\u0000xy\u0001\u0000\u0000\u0000yz\u0005"+
		"\u0003\u0000\u0000z\u00ac\u0001\u0000\u0000\u0000{|\u0005\u001c\u0000"+
		"\u0000|\u0081\u0003\n\u0005\u0000}~\u0005\u0005\u0000\u0000~\u0080\u0003"+
		"\n\u0005\u0000\u007f}\u0001\u0000\u0000\u0000\u0080\u0083\u0001\u0000"+
		"\u0000\u0000\u0081\u007f\u0001\u0000\u0000\u0000\u0081\u0082\u0001\u0000"+
		"\u0000\u0000\u0082\u0084\u0001\u0000\u0000\u0000\u0083\u0081\u0001\u0000"+
		"\u0000\u0000\u0084\u0085\u0005\u001d\u0000\u0000\u0085\u0086\u0003\f\u0006"+
		"\u0014\u0086\u00ac\u0001\u0000\u0000\u0000\u0087\u0088\u0005\u001e\u0000"+
		"\u0000\u0088\u0089\u0003\f\u0006\u0000\u0089\u0091\u0005\u001f\u0000\u0000"+
		"\u008a\u008b\u0005.\u0000\u0000\u008b\u008c\u0005\u0007\u0000\u0000\u008c"+
		"\u008d\u0005,\u0000\u0000\u008d\u008e\u0005!\u0000\u0000\u008e\u008f\u0003"+
		"\f\u0006\u0000\u008f\u0090\u0005\u0001\u0000\u0000\u0090\u0092\u0001\u0000"+
		"\u0000\u0000\u0091\u008a\u0001\u0000\u0000\u0000\u0092\u0093\u0001\u0000"+
		"\u0000\u0000\u0093\u0091\u0001\u0000\u0000\u0000\u0093\u0094\u0001\u0000"+
		"\u0000\u0000\u0094\u0095\u0001\u0000\u0000\u0000\u0095\u0096\u0005 \u0000"+
		"\u0000\u0096\u00ac\u0001\u0000\u0000\u0000\u0097\u0098\u0005\"\u0000\u0000"+
		"\u0098\u00ac\u0005,\u0000\u0000\u0099\u009a\u0005#\u0000\u0000\u009a\u00ac"+
		"\u0003\f\u0006\u0011\u009b\u009c\u0005\n\u0000\u0000\u009c\u00ac\u0003"+
		"\f\u0006\f\u009d\u009e\u0005(\u0000\u0000\u009e\u00ac\u0003\f\u0006\b"+
		"\u009f\u00a0\u0005\u0004\u0000\u0000\u00a0\u00a1\u0003\f\u0006\u0000\u00a1"+
		"\u00a2\u0005\u0006\u0000\u0000\u00a2\u00ac\u0001\u0000\u0000\u0000\u00a3"+
		"\u00ac\u0005/\u0000\u0000\u00a4\u00ac\u0005-\u0000\u0000\u00a5\u00ac\u0005"+
		"\u0012\u0000\u0000\u00a6\u00ac\u0005\u0013\u0000\u0000\u00a7\u00ac\u0005"+
		".\u0000\u0000\u00a8\u00a9\u0005.\u0000\u0000\u00a9\u00aa\u0005\u0014\u0000"+
		"\u0000\u00aa\u00ac\u0003\f\u0006\u0001\u00abR\u0001\u0000\u0000\u0000"+
		"\u00abc\u0001\u0000\u0000\u0000\u00abk\u0001\u0000\u0000\u0000\u00abq"+
		"\u0001\u0000\u0000\u0000\u00ab{\u0001\u0000\u0000\u0000\u00ab\u0087\u0001"+
		"\u0000\u0000\u0000\u00ab\u0097\u0001\u0000\u0000\u0000\u00ab\u0099\u0001"+
		"\u0000\u0000\u0000\u00ab\u009b\u0001\u0000\u0000\u0000\u00ab\u009d\u0001"+
		"\u0000\u0000\u0000\u00ab\u009f\u0001\u0000\u0000\u0000\u00ab\u00a3\u0001"+
		"\u0000\u0000\u0000\u00ab\u00a4\u0001\u0000\u0000\u0000\u00ab\u00a5\u0001"+
		"\u0000\u0000\u0000\u00ab\u00a6\u0001\u0000\u0000\u0000\u00ab\u00a7\u0001"+
		"\u0000\u0000\u0000\u00ab\u00a8\u0001\u0000\u0000\u0000\u00ac\u00da\u0001"+
		"\u0000\u0000\u0000\u00ad\u00ae\n\u0010\u0000\u0000\u00ae\u00af\u0005&"+
		"\u0000\u0000\u00af\u00d9\u0003\f\u0006\u0011\u00b0\u00b1\n\u000f\u0000"+
		"\u0000\u00b1\u00b2\u0005\'\u0000\u0000\u00b2\u00d9\u0003\f\u0006\u0010"+
		"\u00b3\u00b4\n\u000e\u0000\u0000\u00b4\u00b5\u0005$\u0000\u0000\u00b5"+
		"\u00d9\u0003\f\u0006\u000f\u00b6\u00b7\n\r\u0000\u0000\u00b7\u00b8\u0005"+
		"%\u0000\u0000\u00b8\u00d9\u0003\f\u0006\u000e\u00b9\u00ba\n\u000b\u0000"+
		"\u0000\u00ba\u00bb\u0005)\u0000\u0000\u00bb\u00d9\u0003\f\u0006\f\u00bc"+
		"\u00bd\n\n\u0000\u0000\u00bd\u00be\u0005*\u0000\u0000\u00be\u00d9\u0003"+
		"\f\u0006\u000b\u00bf\u00c0\n\t\u0000\u0000\u00c0\u00c1\u0005+\u0000\u0000"+
		"\u00c1\u00d9\u0003\f\u0006\n\u00c2\u00c5\n\u0019\u0000\u0000\u00c3\u00c4"+
		"\u0005\b\u0000\u0000\u00c4\u00c6\u0005,\u0000\u0000\u00c5\u00c3\u0001"+
		"\u0000\u0000\u0000\u00c5\u00c6\u0001\u0000\u0000\u0000\u00c6\u00c7\u0001"+
		"\u0000\u0000\u0000\u00c7\u00c8\u0005\t\u0000\u0000\u00c8\u00c9\u0005."+
		"\u0000\u0000\u00c9\u00d4\u0005\u0004\u0000\u0000\u00ca\u00cf\u0003\f\u0006"+
		"\u0000\u00cb\u00cc\u0005\u0005\u0000\u0000\u00cc\u00ce\u0003\f\u0006\u0000"+
		"\u00cd\u00cb\u0001\u0000\u0000\u0000\u00ce\u00d1\u0001\u0000\u0000\u0000"+
		"\u00cf\u00cd\u0001\u0000\u0000\u0000\u00cf\u00d0\u0001\u0000\u0000\u0000"+
		"\u00d0\u00d3\u0001\u0000\u0000\u0000\u00d1\u00cf\u0001\u0000\u0000\u0000"+
		"\u00d2\u00ca\u0001\u0000\u0000\u0000\u00d3\u00d6\u0001\u0000\u0000\u0000"+
		"\u00d4\u00d2\u0001\u0000\u0000\u0000\u00d4\u00d5\u0001\u0000\u0000\u0000"+
		"\u00d5\u00d7\u0001\u0000\u0000\u0000\u00d6\u00d4\u0001\u0000\u0000\u0000"+
		"\u00d7\u00d9\u0005\u0006\u0000\u0000\u00d8\u00ad\u0001\u0000\u0000\u0000"+
		"\u00d8\u00b0\u0001\u0000\u0000\u0000\u00d8\u00b3\u0001\u0000\u0000\u0000"+
		"\u00d8\u00b6\u0001\u0000\u0000\u0000\u00d8\u00b9\u0001\u0000\u0000\u0000"+
		"\u00d8\u00bc\u0001\u0000\u0000\u0000\u00d8\u00bf\u0001\u0000\u0000\u0000"+
		"\u00d8\u00c2\u0001\u0000\u0000\u0000\u00d9\u00dc\u0001\u0000\u0000\u0000"+
		"\u00da\u00d8\u0001\u0000\u0000\u0000\u00da\u00db\u0001\u0000\u0000\u0000"+
		"\u00db\r\u0001\u0000\u0000\u0000\u00dc\u00da\u0001\u0000\u0000\u0000\u0013"+
		"\u0015\u001b#/4CEPZ_w\u0081\u0093\u00ab\u00c5\u00cf\u00d4\u00d8\u00da";
	public static final ATN _ATN =
		new ATNDeserializer().deserialize(_serializedATN.toCharArray());
	static {
		_decisionToDFA = new DFA[_ATN.getNumberOfDecisions()];
		for (int i = 0; i < _ATN.getNumberOfDecisions(); i++) {
			_decisionToDFA[i] = new DFA(_ATN.getDecisionState(i), i);
		}
	}
}
grammar YAPL;


start 
    : program EOF
    ;

program 
    : class_exp ';' program        # class_list
    | EOF                          # end
    ;

class_exp
    : CLASS TYPE (INHERITS TYPE)? '{' (feature ';')* '}'
    ;

feature 
    : ID '(' (formal (',' formal)*)* ')' ':' TYPE '{' expr '}' # method
    | ID ':' TYPE ( ASSIGNMENT expr )?                         # attribute
    ;

formal 
    : ID ':' TYPE 
    ;

declaration
    : ID ':' TYPE ( ASSIGNMENT expr )?
    ;

expr
    : expr ('@' TYPE)? '.' ID '(' ( expr (',' expr)* )* ')'         # dispatch
    | ID '(' ( expr (',' expr)* )* ')'                              # call
    | IF expr THEN expr ELSE expr FI                                # if
    | WHILE expr LOOP expr POOL                                     # while
    | '{' (expr ';') + '}'                                          # block
    | LET declaration (',' declaration)* IN expr                    # letIn
    | CASE expr OF (ID ':' TYPE CASEARR expr ';') + ESAC            # case
    | NEW TYPE                                                      # newObject
    | ISVOID expr                                                   # isVoid
    | expr MULT expr                                                # star
    | expr DIV expr                                                 # division
    | expr ADD expr                                                 # add
    | expr MINUS expr                                               # minus
    | '~' expr                                                      # negInteger
    | expr LT expr                                                  # lessThan
    | expr LE expr                                                  # lessEqual
    | expr EQ expr                                                  # equal
    | NOT expr                                                      # negation
    | '('expr')'                                                    # parenthesis
    | INT                                                           # int
    | STR                                                           # str
    | TRUE                                                          # true
    | FALSE                                                         # false
    | ID                                                            # id
    | ID ASSIGNMENT expr                                            # assignment
    ;


// comments
OPEN_COMMENT
   : '(*'
   ;
CLOSE_COMMENT
   : '*)'
   ;
COMMENT
   : OPEN_COMMENT (COMMENT | .)*? CLOSE_COMMENT -> skip
   ;
ONE_LINE_COMMENT
   : '--' (~ '\n')* '\n'? -> skip
   ;

WHITESPACE
   : [ \t\r\n\f\\] + -> skip
   ;

// Keywords

CLASS : C L A S S;

INHERITS : I N H E R I T S;

TRUE : 't' R U E ;

FALSE : 'f' A L S E ;

ASSIGNMENT : '<-' ;

IF : I F ;

ELSE : E L S E ;

THEN : T H E N ;

FI : F I ;

WHILE : W H I L E ;

LOOP : L O O P ;

POOL : P O O L ;

LET : L E T ;

IN : I N ;

CASE : C A S E ;

OF : O F ;

ESAC : E S A C ;

CASEARR : '=>' ;

NEW : N E W ;

ISVOID : I S V O I D ;

ADD : '+' ;

MINUS : '-' ;

MULT : '*' ;

DIV : '/' ;

NOT : N O T ;

LT : '<' ;

LE : '<=' ;

EQ : '=' ;

TYPE : [A-Z]([a-zA-Z0-9]|'_')*;

STR : '"' .*? '"';

ID : [a-z]([a-zA-Z0-9]|'_')*;

INT : [0-9]+;


fragment A: [Aa];
fragment B: [Bb];
fragment C: [Cc];
fragment D: [Dd];
fragment E: [Ee];
fragment F: [Ff];
fragment G: [Gg];
fragment H: [Hh];
fragment I: [Ii];
fragment J: [Jj];
fragment K: [Kk];
fragment L: [Ll];
fragment M: [Mm];
fragment N: [Nn];
fragment O: [Oo];
fragment P: [Pp];
fragment Q: [Qq];
fragment R: [Rr];
fragment S: [Ss];
fragment T: [Tt];
fragment U: [Uu];
fragment V: [Vv];
fragment W: [Ww];
fragment X: [Xx];
fragment Y: [Yy];
fragment Z: [Zz];
fragment BACK: [\][.*];
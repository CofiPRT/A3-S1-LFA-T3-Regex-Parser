grammar Regex;

// LEXER RULES
PARENTHESIS_OPEN    : '('   ;
PARENTHESIS_CLOSE   : ')'   ;
KLEENE_STAR         : '*'+  ;
UNION               : '|'   ;
SYMBOL              : [a-z] ;

// PARSER RULES
// Force precedence in parse tree -> parenthesis > kleene star > concatenation > union
// The higher 'X' in 'precedenceX', the higher the precedence
expr        : precedence1 ;
precedence1 : precedence2 | union ;
precedence2 : precedence3 | concat ;
precedence3 : precedence4 | kleene ; // easily modified, can add a rule for "+"
precedence4 : parentheses | symbol ;

union       : precedence2 UNION precedence1 ;
concat      : precedence3 precedence2 ;
kleene      : precedence4 KLEENE_STAR ;
parentheses : PARENTHESIS_OPEN expr PARENTHESIS_CLOSE ;
symbol      : SYMBOL ;
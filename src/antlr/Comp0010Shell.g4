grammar Comp0010Shell;

command: pipe | command ';' command | call | <EOF>;
pipe: pipe '|' call | call '|' call | pipe '|' command;
call: WHITESPACE? (redirection WHITESPACE)* argument (WHITESPACE? atom)* WHITESPACE?;
atom: redirection | argument;
argument: (quoted | UNQUOTED)+;
redirection: '<' WHITESPACE? argument | '>' WHITESPACE? argument | '>>' WHITESPACE? argument;


UNQUOTED: ~[ \t\n'"`<>|;]+;
quoted: SINGLE_QUOTED | BACK_QUOTED | DOUBLE_QUOTED;
SINGLE_QUOTED: '\'' ~[\n']* '\'';
BACK_QUOTED: '`' ~[\n`]* '`';
DOUBLE_QUOTED: '"' (BACK_QUOTED | ~[\n"]+)* '"';
WHITESPACE: [ \t]+;
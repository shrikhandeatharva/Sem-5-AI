%{
#include <stdio.h>
%}

%%
[a-zA-Z][a-zA-Z0-9_]*\n { printf("IDENTIFIER: %s\n", yytext); }
-?0x[0-9a-fA-F]+\n       { printf("HEXADECIMAL: %s\n", yytext); }
-?0[0-7]+\n             { printf("OCTAL: %s\n", yytext); }
-?[0-9]+\n               { printf("INTEGER: %s\n", yytext); }
-?[0-9]+"."[0-9]+\n     { printf("FLOAT: %s\n", yytext); }
[0-9]+\.[0-9]+[Ee][-+]?[0-9]+\n { printf("EXPONENTIAL: %s\n", yytext); }
.                    { printf("Invalid: %s\n", yytext); }

%%

int yywrap(void) {
  return 1;
}

int main() {
  yylex();
  return 0;
}
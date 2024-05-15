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


/*Theory :-Regular Expression for. Decimal constant
Rules:
1. must have at least one digit
2. may be +ve of -ve
3. No spaces, comma, period (.) are allowed.
Regular Expression :- (+/-)? (Digit)+

b) Regular Expression for Real constant (Floating point Notation)
1. must have at least one digit
2. may be +ve o -ve
3. must contain decimal point
4. at least are digit often decimal point.
5) NO(-) (,) (.)
Regular Expression:- (+|-)? (Digit)* - (Digit)+
In lexical analysis. the source code is scanned. and broken. down into these individual tokens, 
which are then passed on the next stage of the compilation.
of interpretation Process.
Some of them Can be described as follows:-
1. Identifier:- ^[a-zA-Z][a-20A-Z0-9_J* $
Here,
A
matches the beginning of the string
・[a-zA-Z-J':- matches any uppercase letter lowercase letter, of, underscore.
[a-zA-Z, 0-9-J':- matches zero of more occurences of any uppercase letter. lowercase letter, digit of underscore.
'$'-
matches the end of Steing.
2. Integer Constant :- Regular expressions for decimal constant can be
a. must have at least one digit.
b. may be have +ve σε -ve
C. No space and commas, (+/-)? (Digit) + period (-) are allowed
3. Real, Constant :- This will includes two categories
i) floating point :- must contain decimal point
ii) Exponential point :- must contain montissa and Exponent Regular expression for real constant is seperated by 'E' of 'e'
exponent [eE][+-], {digit }+
{ digit }+ ". " {digit.}* { exponent }? |{ digit}+{ exponent }*/

%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#include <string.h>
%}

%%

[-+]?[0-9]+\.[0-9]+[Ee][-+]?[0-9]+ { 
    double base, result;
    int exponent;
    sscanf(yytext, "%lf", &base);
    sscanf(yytext + strlen(yytext) - 2, "%d", &exponent);
    result = base * pow(10, exponent);
    printf("Exponential as integer: %d\n", (int)result);
}

[-+]?[0-9]+\.[0-9]+   { printf("Floating-point as integer: %d\n\n", (int)atof(yytext)); }
[-+]?0[xX][0-9a-fA-F]+ { printf("Hexadecimal as integer: %d\n\n", (int)strtol(yytext, NULL, 16)); }
[-+]?0[0-7]+          { printf("Octal as integer: %d\n\n", (int)strtol(yytext, NULL, 8)); }
[-+]?[0-9]+           { printf("Decimal as integer: %d\n\n", atoi(yytext)); }
[ \t\n]               ;
.                     ;

%%

int yywrap(void) {
  return 1;
}

int main() {
    yylex();
    return 0;
}


/*Theory:-
Integer, constants :-

An integer constants can be a decimal, octal, of hexadecimal constant. Constants refer to fixed values that the program may not alter during it's execution. 
The constants can be of any of the basic data types like an integer constant, a Floating constant, a character constant or a String.

In this practical we used Deer Integer Constants

are represented in Decimal, octal and hexadecimal it can be positive integer o& Nat negative

Octal :- Integer constant represented in Decimal octal of A prefix specifies the base of Radix: O For octal representation. 
and it specifies a base: 8 foe, octal

Hexadecimal :- Integer constant represented in Decimal Hexadecimal constant: A prefix specifies a base 0% Radix: "ox" OR "OX" for 
hexadecimal constants. and Base for Hexadecimal is 16.

Default Integer constants consider (base. 10) Decimal.*/

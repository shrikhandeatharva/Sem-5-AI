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
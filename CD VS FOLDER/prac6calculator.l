%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
int op = 0;
float a, b;
void digi();
void digi() {
 if (op == 0) {
 a = atof(yytext);
 } else {
 b = atof(yytext);
 switch (op) {
 case 1:
 a = a + b;
 break;
 case 2:
 a = a - b;
 break;
 case 3:
 a = a * b;
 break;
 case 4:
 if (b != 0) {
 a = a / b;
 } else {
 printf("Error: Division by zero\n");
 exit(1);
 }
 break;
 case 5:
 a = pow(a, b);
 break;
 }
 op = 0;
 }
}
%}
dig [0-9]+|([0-9]*)\.([0-9]+)
add "+"
sub "-"
mul "*"
div "/"
pow "^"
ln "\n"
%%
{dig} { digi(); }
{add} { op = 1; }
{sub} { op = 2; }
{mul} { op = 3; }
{div} { op = 4; }
{pow} { op = 5; }
{ln} { printf("Result: %0.2f\n\n", a); }
. { printf("Invalid input: %s\n", yytext); }
%%
int main(int argc, char *argv[]) {
 yylex();
 return 0;
}
int yywrap() {
 return 1;
} 


/*Yacc (Yet Another Compiler Compiler) and Bison (GNU Bison) are tools used in compiler construction for parsing. 
They're both parser generators that take a formal grammar (a set of rules) as input. This grammar defines how to break down the structure 
of a programming language or any other textual format. Yacc and Bison then generate C code that implements a parser. 
This parser can analyze code or data according to the grammar's rules, identifying the constituent parts and their relationships. 
While Yacc was the original tool, Bison is a widely used, Yacc-compatible parser generator from the GNU project. 
They both play a vital role in building compilers and other programs that need to understand the structure of text input.*/

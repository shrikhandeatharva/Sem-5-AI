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
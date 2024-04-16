%{
#include <stdio.h>
#include <stdlib.h>
#include <math.h>
#define MAX_STACK_SIZE 100
double stack[MAX_STACK_SIZE];
int top = -1;
void push(double val) {
 if (top < MAX_STACK_SIZE - 1) {
 stack[++top] = val;
 } else {
 printf("Error: Stack Overflow\n");
 exit(1);
 }
}
double pop() {
 if (top >= 0) {
 return stack[top--];
 } else {
 printf("Error: Stack Underflow\n");
 exit(1);
 }
}
%}
DIGIT [0-9]
NUMBER ({DIGIT})
%%
{NUMBER} { push(atof(yytext)); } /* push single-digit number onto stack */
"+" { double b = pop(); double a = pop(); push(a + b); } /* addition */
"-" { double b = pop(); double a = pop(); push(a - b); } /* subtraction */
"*" { double b = pop(); double a = pop(); push(a * b); } /* multiplication */
"/" { double b = pop(); double a = pop(); push(a / b); } /* division */
"^" { double b = pop(); double a = pop(); push(pow(a, b)); } /* exponentiation
*/
\n { printf("Result: %.2f\n\n", pop());} /* print result on newline */
. { printf("Invalid input: %s\n", yytext); }
%%
int main() {
 yylex();
 return 0;
}
int yywrap() {
 return 1;
}
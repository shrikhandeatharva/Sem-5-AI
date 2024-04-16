#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include<stdbool.h>
void E(char *input);
void T(char *input);
void error();
int main() {
 while(true)
 {
 char input[100];
 printf("Enter a string: ");
 scanf("%s", input);
 T(input);
 if (input[strlen(input)] == '\0') {
 printf("String accepted!\n");
 } else {
 printf("String not fully consumed.\n");
 }
 }
}
void E(char *input) {
 while(*input == '+' || *input == '-') {
 input++;
 T(input);
 }
}
void T(char *input) {
 if (*input == 'a' || *input == 'b') {
 input++;
 E(input);
 } else {
 error();
 }
}
void error() {
 printf("Error: Invalid string format.\n");
 exit(1);
}
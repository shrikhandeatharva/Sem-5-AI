// #include <stdio.h>
// #include <stdlib.h>
// #include <string.h>
// #include<stdbool.h>
// void E(char *input);
// void T(char *input);
// void error();
// int main() {
//  while(true)
//  {
//  char input[100];
//  printf("Enter a string: ");
//  scanf("%s", input);
//  T(input);
//  if (input[strlen(input)] == '\0') {
//  printf("String accepted!\n");
//  } else {
//  printf("String not fully consumed.\n");
//  }
//  }
// }
// void E(char *input) {
//  while(*input == '+' || *input == '-') {
//  input++;
//  T(input);
//  }
// }
// void T(char *input) {
//  if (*input == 'a' || *input == 'b') {
//  input++;
//  E(input);
//  } else {
//  error();
//  }
// }
// void error() {
//  printf("Error: Invalid string format.\n");
//  exit(1);
// }

#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <stdbool.h>

void E(char **input);
void T(char **input);
void error();

int main() {
    while(true)
    {
        char input[100];
        printf("Enter a string: ");
        scanf("%s", input);
        char *ptr = input; // Pointer to the beginning of input string
        E(&ptr); // Pass the pointer to pointer to input string
        if (*ptr == '\0') { // Check if the pointer points to end of string
            printf("String accepted!\n\n");
        } else {
            printf("String not fully consumed.\n");
        }
    }
}

void E(char **input) {
    while(**input == '+' || **input == '-') {
        (*input)++; // Move to the next character
        T(input); // Call T() with updated pointer
    }
}

void T(char **input) {
    if (**input == 'a' || **input == 'b') {
        (*input)++; // Consume 'a' or 'b'
    } else {
        error();
    }
}
void error() {
    printf("Error: Invalid string format.\n");
    exit(1);
}



/*THEORY: A recursive descent parser is a top-down parsing technique where a parser tree is built from top and constructed 
down to leaves this type of parser starts with highest level of grammar and recursively. expands non-terminals until a terminal Symbol is reached-

To implement this grammar using recursive descent Parser, we need to follow steps to implement parser -

1) Analyze grammar, identify terminals, non-terminals production voles.

2) Write function to parse each non-terminal

3) Use tokenizers to convert input string into list of tokens.

4) Pass list tokens as input, function should return whether string can be derived from grammar or not.*/

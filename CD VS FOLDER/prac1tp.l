%{
#include <stdio.h>
#include <string.h>
%}

/* Rules Section */
%%
(a|b)*abb   {printf("Valid String\n");}
.        {printf("Invalid string\n"); break;} // Break the loop after printing invalid string
%%

int main()
{   
    while(1) {
        // The function that starts the analysis
        yylex();
        printf("Enter another string (or type 'exit' to quit): ");
        char input[100];
        scanf("%s", input);
        if(strcmp(input, "exit") == 0)
            break;
    }
  
    return 0;
}

int yywrap(void) {
    return 1; // Flex expects a return value from yywrap, typically 1 indicating no more input
}

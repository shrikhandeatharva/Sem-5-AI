%{
#include <stdio.h>
%}

/* Rules Section */
%%
(a|b)*abb   {printf("Valid String\n");}
%%

 int yywrap(void){}
int main()
{   
    // The function that starts the analysis
    yylex();
  
    return 0;
}
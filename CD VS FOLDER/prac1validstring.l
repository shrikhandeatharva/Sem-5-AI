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


extra 1 more code

%{
#include <stdio.h>
%}

/* Rules Section */
%%
(a|b)*abb   printf("Valid String: %s\n",yytext);
.           printf("Invalid string: %s\n",yytext); 
%%

 int yywrap(void){}
int main()
{   
    // The function that starts the analysis
    yylex();
  
    return 0;
}

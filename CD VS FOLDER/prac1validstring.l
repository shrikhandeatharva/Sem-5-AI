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



/*Regular Expression:-
The lexical analyzer needs
to scan and identify only a Finite set of valid string /
token / lexeme that belong to the language in hand.
Regular. Expression is an important notation for
Specifying pattern Each pattern matches a set of strings.
so regular expression serve as a names for a
set of strings Regular expression can also be described as a sequence of pattern that define a string. 
Regular expression are used to match character, combinations in strings. 
string Searching algorithm used this pattern to find the operations on a string.*/

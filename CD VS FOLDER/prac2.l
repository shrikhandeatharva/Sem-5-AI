% option noyywrap
%{
    #include<stdio.h>
%}
digit                [0-9]
lex_digit            [0-9a - fA-F]
integer              {digit}+'{alpha}
octal                0[0-7]*
hexadecimal          0[XX]{hex-digit}+
Float-num            {digit}+\.{digit}+
exp                  [eE] 
alpha                [a-Z,A-z]
%%
{integer}{printf("Integer constant : %s\n",yytext);}
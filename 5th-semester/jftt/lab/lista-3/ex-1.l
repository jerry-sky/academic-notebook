%option noyywrap
%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <stdbool.h>
#include <math.h>

#include "ex-1_y.h"

int yylex();

#define Z 1234577

%}
%%

(?# comments)
\#.*								{return COM;};

(?# continue a long line)
\\\n								{};

(?# operators)
\+									{return ADD;};
\*									{return MUL;};
\/									{return DIV;};
%									{return MOD;};
\^									{return POW;};
\(									{return LPR;};
\)									{return RPR;};

\-									{return SUB;};

(?# match integer numbers [only positive])
[[:digit:]]+						{int d; sscanf(yytext, "%d", &d); yylval = d % Z; return NUM;};

\n									{return TRM;};
[[:blank:]]							{};
.									{return ERR;};

%%

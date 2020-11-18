%{
#include<stdio.h>
#include <stdbool.h>

int yywrap();
int yylex();
int lines_count = 0;
int words_count = 0;

bool allow_shebang = true;
void shebang_done() {
	allow_shebang = false;
}

%}
%x string_mode
%x documentation
%%
(?# allow the first line to contain shebang)
#!.*\n							{if(allow_shebang) {ECHO; shebang_done();};};

(?# empty string — has to match an empty string with something preceding it otherwise it will be consumed by string_mode condition)
.?((\"\")|(\'\'))							{printf("%s", yytext);};

(?# documentation [or long string] mode — don’t remove anything)
[^\\][\"\']{3}					{printf("%s", yytext); BEGIN(documentation);};
<documentation>[^\\][\"\']{3}	{printf("%s", yytext); BEGIN(0);};

(?# string mode — don’t remove anything)
[^\\][\"\']						{printf("%s", yytext); BEGIN(string_mode);};
<string_mode>[^\\][\"\']		{printf("%s", yytext); BEGIN(0);};

(?# delete comments)
#.*\n?							{};

%%
int yywrap() {
	return 1;
}
int main() {
	return yylex();
}


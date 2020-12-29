%{
#include<stdio.h>
#include <stdbool.h>

int yywrap();
int yylex();

// whether to leave out documentation comments
bool DOC = false;

%}
%x string_mode
%x documentation
%x long_comment
%x ESCAPE
%%
(?# a different approach to the escaping character)
\\												{ECHO; BEGIN(ESCAPE);};
<ESCAPE>.										{ECHO; BEGIN(0);};

(?# empty string [or character] — has to match an empty string with something preceding it otherwise it will be consumed by string_mode condition)
.?\"\"											{ECHO;};

(?# short documentation comments)
\n?[[:blank:]]*((\/\/\/)|(\/\/!)).*(\\\n.*)*	{if(DOC) ECHO;};

(?# delete comments)
\n?[[:blank:]]*\/\/.*(\\\n.*)*					{};
\/\/.*(\\\n.*)*									{};

(?# documentation mode)
(^[[:blank:]]*)?(\/\*\*)|(\/\*!)				{if(DOC) ECHO; BEGIN(documentation);};
<documentation>\/*\**							{if(DOC) ECHO;};
<documentation>[^\*\/]*							{if(DOC) ECHO;};
<documentation>(\*\/)							{if(DOC) ECHO; BEGIN(0);};

(?# delete long comments)
(^[[:blank:]]*)?\/\*							{BEGIN(long_comment);};
<long_comment>\/*\**							{};
<long_comment>[^\*\/]*							{};
<long_comment>\*\/[[:blank:]]*\n?				{BEGIN(0);};

(?# string mode — don’t remove anything)
[\"]											{ECHO; BEGIN(string_mode);};
<string_mode>[^\\][\"]							{ECHO; BEGIN(0);};

%%
int yywrap() {
	return 1;
}
int main(int argc, char **argv) {
	if(argc > 1) {
		DOC = true;
	}
	return yylex();
}

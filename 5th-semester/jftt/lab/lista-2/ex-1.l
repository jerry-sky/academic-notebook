%{
#include<stdio.h>
#include<string.h>

int yywrap();
int yylex();
int lines_count = 1;
int words_count = 0;
%}
%%
(?# remove any unnecessary empty lines)
^[[:blank:]\\]*\n	{};
(?# remove excess whitespace at the beginning of every line)
^[[:blank:]]+		{};
(?# remove excess whitespace at the end of every line)
[[:blank:]]+$		{};
(?# replace excess whitespace between words with one space character)
[[:blank:]]+		{printf(" ");};

(?# count words and lines)
([^[:blank:]\n])+/[[:blank:]]	{ECHO; words_count++;};
([^[:blank:]\n])+$				{ECHO; words_count++;};
\n								{ECHO; lines_count++;};
%%
int yywrap() {
	return 1;
}
int main() {
	yylex();

	printf("\nlines count: %d\nwords count: %d\n", lines_count, words_count);
	return 0;
}

%{
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <limits.h>
#include <stdbool.h>
#include <math.h>

int yywrap();
int yylex();

#define err_max_length 512
#define stack_max 1024
int stack_pointer = 0;
int *stack;
char err[err_max_length] = "none";

// every time a newline is encountered or an error occurred the stack is reset
void reset() {
	stack_pointer = 0;
	strcpy(err, "none");
}

void assert_number_of_arguments() {
	if(stack_pointer < 2) {
		strcpy(err, "Error: too few arguments");
	}
}

bool assert_divisor_neq_zero() {
	// assert the divisor is not equal to zero
	if(stack[stack_pointer] == 0) {
		strcpy(err, "Error: division by zero");
		return false;
	}
	return true;
}

void unrecognized_character(char* invalid_characters) {
	// compose an error message
	strcpy(err, "Error: invalid input ‘");
	strcat(err, invalid_characters);
	strcat(err, "’");
}

void add() {
	assert_number_of_arguments();
	stack_pointer--;
	stack[stack_pointer-1] = stack[stack_pointer-1] + stack[stack_pointer];
}

void subtract() {
	assert_number_of_arguments();
	stack_pointer--;
	stack[stack_pointer-1] = stack[stack_pointer-1] - stack[stack_pointer];
}

void multiply() {
	assert_number_of_arguments();
	stack_pointer--;
	stack[stack_pointer-1] = stack[stack_pointer-1] * stack[stack_pointer];
}

void divide() {
	assert_number_of_arguments();
	stack_pointer--;
	if(assert_divisor_neq_zero()) {
		stack[stack_pointer-1] = stack[stack_pointer-1] / stack[stack_pointer];
	}
}

void mod() {
	assert_number_of_arguments();
	stack_pointer--;
	if(assert_divisor_neq_zero()) {
		stack[stack_pointer-1] = stack[stack_pointer-1] % stack[stack_pointer];
	}
}

void power() {
	assert_number_of_arguments();
	stack_pointer--;
	stack[stack_pointer-1] = pow((double)stack[stack_pointer-1], (double)stack[stack_pointer]);
}

void output() {
	// check if the stack is empty (contains only one last number)
	if (stack_pointer > 1) {
		strcpy(err, "Error: too few operators");
	}

	// check for errors
	if(strcmp("none", err) != 0) {
		// error state is ≠ from 'none'
		printf("%s\n", err);
	} else {
		// everything is good — print the output
		printf("%d\n", stack[stack_pointer-1]);
	}
	// reset the stack
	reset();
}

%}
%%
(?# match integer numbers)
\-?[[:digit:]]+				{stack[stack_pointer] = atoi(yytext); stack_pointer++;};

(?# avoid copying over the blanks)
[[:blank:]]+				{};

(?# the operators)
\+							{add();};
\-							{subtract();};
\*							{multiply();};
\/							{divide();};
%							{mod();};
\^							{power();};
\n							{output();};

(?# if one invalid character matched — invalidate whole line)
[^[:blank:][:digit:]\+\-\*\/\%\^\n].*	{unrecognized_character(yytext);};

%%
int yywrap() {
	return 1;
}
int main() {
	stack = malloc(stack_max * sizeof(int));
	return yylex();
}

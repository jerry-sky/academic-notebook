%{
#define YYSTYPE int
#include<stdio.h>
#include<math.h>
#include<string.h>
#include <stdlib.h>
#define Z 1234577
#define expression_max_length 4096

int yylex();
int yyerror(char*);

char RPN_acc[expression_max_length];

void empty_RPN_acc() {
    RPN_acc[0] = '\0';
}

int flatten(int x) {
    return ((x % Z) + Z) % Z;
}

int add(int x, int y) {
    return flatten(flatten(x) + flatten(y));
}

int subtract(int x, int y) {
    return flatten(flatten(x) - flatten(y));
}

int multiply(int x, int y) {
    int output = flatten(x);
    for(int i = 1; i < y; i++) {
        output += x;
        output = flatten(output);
    }
    return output;
}

int inverse(int a) {
    int m = Z;
    int x = 1;
    int y = 0;

    while( a > 1) {
        int quotient = a / m;
        int t = m;

        m = a % m;
        a = t;
        t = y;

        y = x - quotient * y;
        x = t;
    }

    if(x < 0)
        x += Z;

    return x;
}

int divide(int x, int y) {
    if(y == 0) {
        yyerror("division by zero");
        return -1;
    } else {
        int inv = inverse(y);
        return flatten(multiply(x, inv));
    }
}

int mod(int x, int y) {
    if(y == 0) {
        yyerror("mod by zero");
        return -1;
    } else {
        return flatten(flatten(x) % flatten(y));
    }
}

int power(int x, int y) {
    int output = 1;
    for (int i = 0; i < y; i++) {
        output *= x;
        output = flatten(output);
    }
    return output;
}


%}

%token NUM

%token ADD
%token SUB
%token MUL
%token DIV
%token MOD
%token POW
%token LPR
%token RPR
%token TRM
%token ERR
%token COM
%token COT

%left ADD SUB
%left MUL DIV MOD
%right POW
%precedence NEG

%%

INPT: %empty
    | INPT STAR TRM
;

STAR: EXPR {printf("\n%s\nans = %d\n", RPN_acc, $1);empty_RPN_acc();}
    | EXPR error
    | error
    | COM
;

NUMR: NUM {$$ = $1; sprintf(RPN_acc + strlen(RPN_acc), "%d ", $$);}
    | SUB NUM %prec NEG {$$ = subtract(0, $2); sprintf(RPN_acc + strlen(RPN_acc), "%d ", $$);}
;

EXPR: EXPR ADD EXPR {sprintf(RPN_acc + strlen(RPN_acc), "+ "); $$ = add($1, $3);}
    | EXPR SUB EXPR {sprintf(RPN_acc + strlen(RPN_acc), "- "); $$ = subtract($1, $3);}
    | EXPR MUL EXPR {sprintf(RPN_acc + strlen(RPN_acc), "* "); $$ = multiply($1, $3);}
    | EXPR DIV EXPR {sprintf(RPN_acc + strlen(RPN_acc), "/ "); $$ = divide($1, $3); if($$ == -1) YYERROR;}
    | EXPR MOD EXPR {sprintf(RPN_acc + strlen(RPN_acc), "%% "); $$ = mod($1, $3); if($$ == -1) YYERROR;}
    | NUMR POW NUMR {sprintf(RPN_acc + strlen(RPN_acc), "^ "); $$ = power($1, $3);}
    | LPR EXPR RPR {$$ = $2;}
    | NUMR
;

%%
int yyerror(char *s)
{
    printf("Fatal error: %s\n",s);
    empty_RPN_acc();
}

int main()
{
    yyparse();
    return 0;
}


#!/usr/bin/env python3

import ply.yacc as yacc
import ply.lex as lex
from auxiliary import *
from sys import stdin

tokens = (
    'ADD', 'SUB', 'MUL', 'DIV', 'MOD', 'POW',
    'LPR', 'RPR',
    'NUM',
    'COM'
)

# all the tokens
t_COM = r'\#.*'

t_ADD = r'\+'
t_MUL = r'\*'
t_DIV = r'\/'
t_MOD = r'%'
t_POW = r'\^'
t_LPR = r'\('
t_RPR = r'\)'

t_SUB = r'-'


def t_NUM(t):
    r'[0-9]+'
    t.value = int(t.value)
    return t


# ignore blanks
t_ignore = ' \t'


def t_newline(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')


def t_error(t):
    print(f'\ninvalid character: {t.value[0]!r}')
    t.lexer.skip(1)


# build the lexer
lex.lex()

# precedence rules for the arithmetic operators
precedence = (
    ('left', 'ADD', 'SUB'),
    ('left', 'MUL', 'DIV', 'MOD'),
    ('right', 'NEG', 'POW')
)


def p_STAR_EXPR(p):
    'STAR : EXPR'
    print()
    print('ans =', p[1])


# allow comments
def p_STAR_COM(p):
    'STAR : COM'
    pass


def p_NUMR(p):
    'NUMR : NUM'
    p[0] = flatten(p[1])
    print_(p[0], '')


def p_NUMR_NEG(p):
    'NUMR : SUB NUM %prec NEG'
    p[0] = flatten(0 - flatten(p[2]))
    print_(p[0], '')


def p_EXPR_ADD(p):
    'EXPR : EXPR ADD EXPR'
    p[0] = flatten(flatten(p[1]) + flatten(p[3]))
    print_('+ ')


def p_EXPR_SUB(p):
    'EXPR : EXPR SUB EXPR'
    p[0] = flatten(flatten(p[1]) - flatten(p[3]))
    print_('- ')


def p_EXPR_MUL(p):
    'EXPR : EXPR MUL EXPR'
    p[0] = multiply(p[1], p[3])
    print_('* ')


def p_EXPR_DIV(p):
    'EXPR : EXPR DIV EXPR'
    x = p[1]
    y = p[3]
    if y == 0:
        raise 'division by zero'
    p[0] = flatten(multiply(x, inverse(y)))
    print_('/ ')


def p_EXPR_MOD(p):
    'EXPR : EXPR MOD EXPR'
    x = p[1]
    y = p[3]
    if y == 0:
        raise 'mod by zero'
    p[0] = flatten(flatten(x) % flatten(y))
    print_('% ')


# allow only one `POW`er move per `EXPR`
def p_EXPR_POW(p):
    'EXPR : NUMR POW NUMR'
    x = p[1]
    y = p[3]
    output = 1
    for i in range(0, y):
        output *= x
        output = flatten(output)
    p[0] = output
    print_('^ ')


def p_EXPR_PRS(p):
    'EXPR : LPR EXPR RPR'
    p[0] = p[2]


def p_EXPR_NUM(p):
    'EXPR : NUMR'
    p[0] = p[1]


def p_error(p):
    if p != None:
        print(f'\nsyntax error: ‘{p.value}’')
    else:
        print(f'syntax error')


yacc.yacc()

acc = ''
for line in stdin:
    if line[-2] == '\\':
        # accumulate for later evaluation
        acc += line[:-2]
    elif acc != '':
        acc += line
        # evaluate a concatenation of multiple lines
        yacc.parse(acc)
        # empty the accumulator
        acc = ''
    else:
        # otherwise parse one given line
        yacc.parse(line)

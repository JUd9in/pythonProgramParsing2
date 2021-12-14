#! /usr/bin/env python
# coding=utf-8
import ply.yacc as yacc
from py_lex import *
from node import node, num_node, int_node


# YACC for parsing Python

def simple_node(t, name):
    t[0] = node(name)
    for i in range(1, len(t)):
        t[0].add(node(t[i]))
    return t[0]


def p_program(t):
    '''program : statements'''
    if len(t) == 2:
        t[0] = node('[PROGRAM]')
        t[0].add(t[1])


def p_statements(t):
    '''statements : statements statement
                  | statement'''
    if len(t) == 3:
        t[0] = node('[STATEMENTS]')
        t[0].add(t[1])
        t[0].add(t[2])
        # t[0].add(node('returnFlag'))
    elif len(t) == 2:
        t[0] = node('[STATEMENTS]')
        t[0].add(t[1])
        # t[0].add(node('returnFlag'))


def p_statement(t):
    ''' statement : assignment
                  | operation
                  | print
                  | modification
                  | iF
                  | whilE
                  | for
                  | break
                  | return
                  | function
                  | runfunction '''
    if len(t) == 2:
        t[0] = node('[STATEMENT]')
        t[0].add(t[1])


def p_break(t):
    ''' break : BREAK statements
              | BREAK'''
    t[0] = node('[BREAK]')
    t[0].add(node('break'))


def p_return(t):
    ''' return : RETURN '''
    t[0] = node('[RETURN]')
    t[0].add(node('return'))


def p_for(t):
    '''for : FOR '(' operation ';' condition ';' operation ')' '{' statements '}' '''
    if len(t) == 12:
        t[0] = node('[FOR]')
        t[0].add(t[3])
        t[0].add(t[5])
        t[0].add(t[7])
        t[0].add(t[10])


def p_condition(t):
    '''condition : VARIABLE '>' VARIABLE
                 | VARIABLE '<' VARIABLE
                 | VARIABLE '>' NUMBER
                 | VARIABLE '<' NUMBER
                 | VARIABLE '<' '=' VARIABLE
                 | VARIABLE '>' '=' VARIABLE
                 | VARIABLE '[' factor ']' '>' VARIABLE
                 | VARIABLE '[' factor ']' '<' VARIABLE
                 | VARIABLE '<' VARIABLE AND VARIABLE '[' factor ']' '>' VARIABLE
                 | VARIABLE '<' VARIABLE AND VARIABLE '[' factor ']' '<' '=' VARIABLE '''
    if len(t) == 4:
        t[0] = simple_node(t, '[CONDITION]')
    elif len(t) == 5:
        t[0] = simple_node(t, '[CONDITION]')
    elif len(t) == 7:
        t[0] = node('[CONDITION]')
        t[0].add(node(t[1]))
        t[0].add(node(t[2]))
        t[0].add(t[3])
        t[0].add(node(t[4]))
        t[0].add(node(t[5]))
        t[0].add(node(t[6]))
    elif len(t) == 11:
        t[0] = node('[CONDITION_COMPLEX1]')
        t[0].add(node(t[1]))
        t[0].add(node(t[3]))
        t[0].add(node(t[5]))
        t[0].add(t[7])
        t[0].add(node(t[10]))
    elif len(t) == 12:
        t[0] = node('[CONDITION_COMPLEX2]')
        t[0].add(node(t[1]))
        t[0].add(node(t[3]))
        t[0].add(node(t[5]))
        t[0].add(t[7])
        t[0].add(node(t[11]))


def p_if(t):
    r''' iF : IF '(' condition ')' '{' statements '}'
            | IF '(' condition ')' '{' statements '}' ELIF '(' condition ')' '{' statements '}' ELSE '{' statements '}' '''
    if len(t) == 8:
        t[0] = node('[IF]')
        t[0].add(t[3])
        t[0].add(t[6])
    else:
        t[0] = node('[IF]')
        t[0].add(t[3])
        t[0].add(t[6])
        t[0].add(t[10])
        t[0].add(t[13])
        t[0].add(t[17])


def p_while(t):
    r'''whilE : WHILE '(' condition ')' '{' statements '}' '''
    # print(1)
    if len(t) == 8:
        # print(1)
        t[0] = node('[WHILE]')
        # print(2)
        t[0].add(t[3])
        # print(3)
        t[0].add(t[6])


def p_assignment(t):
    '''assignment : VARIABLE '=' NUMBER
                  | VARIABLE '=' '[' sentence ']' '''
    if len(t) == 4:
        t[0] = node('[ASSIGNMENT]')
        t[0].add(node(t[1]))
        t[0].add(node(t[2]))
        t[0].add(num_node(t[3]))
    else:
        t[0] = node('[ASSIGNMENT]')
        t[0].add(node(t[1]))
        t[0].add(node(t[2]))
        t[0].add(node(t[3]))
        t[0].add(t[4])
        t[0].add(node(t[5]))


def p_modification(t):
    '''modification : VARIABLE '[' factor ']' '=' VARIABLE '[' factor ']'
                    | VARIABLE '[' factor ']' '=' VARIABLE '''
    if len(t) == 10:
        t[0] = node('[MODIFICATION]')
        t[0].add(node(t[1]))
        t[0].add(t[3])
        t[0].add(node(t[6]))
        t[0].add(t[8])
    elif len(t) == 7:
        t[0] = node('[MODIFICATION]')
        t[0].add(node(t[1]))
        t[0].add(t[3])
        t[0].add(node(t[6]))


# operation part
def p_operation(t):
    '''operation : VARIABLE '=' expression
                 | VARIABLE '+' '+'
                 | VARIABLE '-' '-' '''
    if len(t) == 4:
        if t[2] == '=':
            t[0] = node('[OPERATION]')
            t[0].add(node(t[1]))
            t[0].add(node(t[2]))
            t[0].add(t[3])
        else:
            t[0] = node('[OPERATION]')
            t[0].add(node(t[1]))
            t[0].add(node(t[2]))
    # elif len(t) == 3:
    #     t[0] = node('[OPERATION]')
    #     t[0].add(node(t[1]))


def p_expression(t):
    '''expression : expression '+' term
                  | expression '-' term
                  | term
                  | VARIABLE '[' factor ']'
                  | LEN '(' term ')' '''

    if len(t) == 4:
        t[0] = node('[EXPR]')
        if t[2] == '+' or t[2] == '-':
            t[0].add(t[1])
            t[0].add(node(t[2]))
            t[0].add(t[3])

    elif len(t) == 2:
        t[0] = node('[EXPR]')
        t[0].add(t[1])
    elif len(t) == 5:
        if t[2] == '[':
            t[0] = node('[EXPR]')
            t[0].add(node(t[1]))
            t[0].add(node(t[2]))
            t[0].add(t[3])
            t[0].add(node(t[4]))
        else:
            t[0] = node('[EXPR]')
            # t[0].add(node(t[1]))
            t[0].add(node('len('))
            t[0].add(t[3])
            t[0].add(node(t[4]))


def p_term(t):
    ''' term : term '*' factor
             | term '/' factor
             | term '/' '/' factor
             | factor'''
    if len(t) == 4:
        t[0] = node('[TERM]')
        if (t[2] == '*') or (t[2] == '/'):
            t[0].add(t[1])
            t[0].add(node(t[2]))
            t[0].add(t[3])
    elif len(t) == 5:
        t[0] = node('[TERM]')
        t[0].add(t[1])
        t[0].add(node('//'))
        t[0].add(t[4])
    elif len(t) == 2:
        t[0] = node('[TERM]')
        t[0].add(t[1])


def p_factor(t):
    '''factor : VARIABLE
              | '(' expression ')'
              | NUMBER'''
    if len(t) == 2:
        t[0] = node('[FACTOR]')
        # print(t[1])
        try:
            if type(eval(t[1])) == int or float:
                t[0].add(num_node(t[1]))
        except NameError or ValueError:
            t[0].add(node(t[1]))
    elif len(t) == 4:
        t[0] = node('[FACTOR]')
        t[0].add(node(t[1]))
        t[0].add(t[2])
        t[0].add(node(t[3]))


# print part
def p_print(t):
    '''print : PRINT '(' sentence ')' '''
    t[0] = node('[PRINT]')
    t[0].add(node(t[1]))
    t[0].add(node(t[2]))
    t[0].add(t[3])
    t[0].add(node(t[4]))


def p_sentence(t):
    '''sentence : word ',' sentence
                | word'''
    t[0] = node('[SENTENCE]')
    if len(t) == 2:
        t[0].add(t[1])
    else:
        t[0].add(t[1])
        t[0].add(node(t[2]))
        t[0].add(t[3])


def p_word(t):
    '''word : NUMBER
            | VARIABLE'''
    t[0] = node('[WORD]')
    try:
        if type(eval(t[1])) == (int or float):
            t[0].add(num_node(t[1]))
            # print(type(eval(t[1])))
    except NameError:
        t[0].add(node(t[1]))
        # print(0)


# FunctionPart

def p_function(t):
    r'''function : DEF VARIABLE '(' sentence ')' '{' statements '}' '''
    if len(t) == 9:
        t[0] = node('[FUNCTION]')
        t[0].add(node(t[2]))
        t[0].add(t[4])
        t[0].add(t[7])
        # t[0].add(node(t[9]))
    # if len(t) == 13:
    #     print(222)
    #     t[0] = node('[FUNCTION]')
    #     t[0].add(node(t[2]))
    #     t[0].add(node(t[4]))
    #     t[0].add(node(t[6]))
    #     t[0].add(node(t[8]))
    #     t[0].add(t[11])


def p_runfunction(t):
    r'''runfunction : VARIABLE '(' sentence ')' '''
    if len(t) == 5:
        t[0] = node('[RUNFUNCTION]')
        t[0].add(node(t[1]))
        t[0].add(t[3])


def p_error(t):
    print("Syntax error at '%s'" % t.value)


yacc.yacc()

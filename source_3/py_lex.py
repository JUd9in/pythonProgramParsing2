#! /usr/bin/env python
# coding=utf-8
import ply.lex as lex

# LEX for parsing Python

# Tokens


tokens = ['VARIABLE', 'NUMBER', 'PRINT', 'WHILE', 'IF', 'ELSE', 'ELIF', 'FOR', 'BREAK', 'LEN', 'DEF', 'RETURN', 'AND',
          'CLASS','SELF','INIT','STR']

literals = ['=', '+', '-', '*', '/', '(', ')', '{', '}', '<', '>', ',', '[', ']', ';', ':', '.']


# Define of tokens
def t_CLASS(t):
    r'class'
    return t

def t_SELF(t):
    r'self'
    return t

def t_INIT(t):
    r'__init__'
    return t

def t_RETURN(t):
    r'return'
    return t


def t_AND(t):
    r'and'
    return t


def t_DEF(t):
    r'def'
    return t


def t_BREAK(t):
    r'break'
    return t


def t_FOR(t):
    r'for'
    return t


def t_ELSE(t):
    r'else'
    return t


def t_ELIF(t):
    r'elif'
    return t


def t_IF(t):
    r'if'
    return t


def t_WHILE(t):
    r'while'
    return t


def t_LEN(t):
    r'len'
    return t


def t_NUMBER(t):
    r'[0-9]+'
    return t




def t_STR(t):
    r'\'[a-zA-Z]+\''
    return t

def t_VARIABLE(t):
    r'[a-zA-Z_]+'
    return t

def t_PRINT(t):
    r'print'
    return t




# Ignored
t_ignore = " \t"


def t_error(t):
    print("Illegal character '%s'" % t.value[0])
    t.lexer.skip(1)


lex.lex()

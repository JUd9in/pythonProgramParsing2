#! /usr/bin/env python
# coding=utf-8
from py_yacc import yacc
from util import clear_text
from translation import trans, v_table
print('====================以下是select_sort的程序解析=========================')
text = clear_text(open('select_sort.py', 'r').read())
# syntax parse
root = yacc.parse(text)
root.print_node(0)

# translation
trans(root)
print('v_table:{0}'.format(v_table))
print('=========================================================================================',end='\n\n')
print('====================以下是binary_search的程序解析=========================')
text = clear_text(open('binary_search.py', 'r').read())
# syntax parse
root = yacc.parse(text)
root.print_node(0)

# translation
trans(root)
print('v_table:{0}'.format(v_table))
print('========================================================================================',end='\n\n')
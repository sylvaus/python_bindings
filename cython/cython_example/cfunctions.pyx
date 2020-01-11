# distutils: language = c

from . cimport c_functions

def print_hello():
    c_functions.print_hello()


def add(lhs, rhs):
    return c_functions.add(lhs, rhs)
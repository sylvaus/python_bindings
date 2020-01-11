# distutils: language = c++

from . cimport cpp_functions


def plus_two_list(l):
    return cpp_functions.plus_two_list(l)
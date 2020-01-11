# distutils: language = c++

from libcpp.vector cimport vector

cdef extern from "cpp/functions.h":
    const vector[int] plus_two_list(const vector[int]);
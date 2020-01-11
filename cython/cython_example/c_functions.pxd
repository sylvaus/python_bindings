# distutils: language = c


cdef extern from "c/functions.h":
    void print_hello();
    int add(int lhs, int rhs);
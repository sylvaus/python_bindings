# distutils: language = c++

from libcpp.string cimport string
from libcpp.vector cimport vector

cdef extern from "c/constants.h":
    const double PI;
    const char* CONST_RAW_STRING;

cdef extern from "cpp/constants.h":
    const string CONST_STRING;
    const vector[int] PRIME_NUMBERS;
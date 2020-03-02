%module (package="swig_example")constants

%{
#define SWIG_FILE_WITH_INIT
#include "c/constants.h"
#include "cpp/constants.h"
%}

%constant const double PI = PI;
%constant const char* CONST_RAW_STRING = CONST_RAW_STRING;

%include "std_vector.i"
// Instantiate templates used by example
namespace std {
   %template(IntVector) vector<int>;
}

%constant const std::string CONST_STRING = CONST_STRING;
%constant const std::vector<int> PRIME_NUMBERS = PRIME_NUMBERS;
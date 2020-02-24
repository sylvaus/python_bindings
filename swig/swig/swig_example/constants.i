%module (package="swig_example")constants

%{
#define SWIG_FILE_WITH_INIT
#include "c/constants.h"
%}

%constant double PI = PI;
%constant const char *CONST_RAW_STRING = CONST_RAW_STRING;
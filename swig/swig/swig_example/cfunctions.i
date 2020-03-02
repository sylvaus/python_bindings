%module (package="swig_example")cfunctions

%{
#define SWIG_FILE_WITH_INIT
#include "c/functions.h"
%}

%include "c/functions.h"
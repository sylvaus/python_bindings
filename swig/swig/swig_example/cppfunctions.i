%module (package="swig_example")cppfunctions

%{
#define SWIG_FILE_WITH_INIT
#include "cpp/functions.h"
%}

%include "std_vector.i"
// Instantiate templates used by example
namespace std {
   %template(IntVector) vector<int>;
}

%include "cpp/functions.h"
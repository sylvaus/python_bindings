%module (package="swig_example")classes

%{
#define SWIG_FILE_WITH_INIT
#include "cpp/simple_classes.h"
#include "cpp/virtual_classes.h"
#include "cpp/inherited_classes.h"
#include "cpp/namespace_simple_class.h"
%}

%include <std_string.i>

%include "cpp/simple_classes.h"
%include "cpp/virtual_classes.h"
%include "cpp/inherited_classes.h"
%include "cpp/namespace_simple_class.h"
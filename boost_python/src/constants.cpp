#define BOOST_PYTHON_STATIC_LIB
#include <boost/python.hpp>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>

#include <conversions.h>

extern "C"
{
#include <c/constants.h>
}
#include <cpp/constants.h>


BOOST_PYTHON_MODULE(constants)
{
    using namespace boost::python;
    // Register vector conversions
    register_vector_to_list<int>();
    sequence_to_vector<int>();

    scope().attr("PI") = PI;
    scope().attr("CONST_RAW_STRING") = CONST_RAW_STRING;
    scope().attr("CONST_STRING") = CONST_STRING;
    scope().attr("PRIME_NUMBERS") = PRIME_NUMBERS;
}

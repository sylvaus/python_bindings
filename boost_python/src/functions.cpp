#define BOOST_PYTHON_STATIC_LIB

#include <vector>
#include <boost/python.hpp>
#include <boost/python/suite/indexing/vector_indexing_suite.hpp>

#include <conversions.h>

extern "C"
{
#include <c/functions.h>
}

#include <cpp/functions.h>



BOOST_PYTHON_MODULE (functions)
{
    using namespace boost::python;
    // Register vector conversions
    register_vector_to_list<int>();
    sequence_to_vector<int>();

    def("print_hello", &print_hello);
    def("add", &add);
    def("plus_two_list", &plus_two_list);
}
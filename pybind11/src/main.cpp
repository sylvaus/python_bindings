#include <pybind11/pybind11.h>
#include <pybind11/stl.h>  // Needed for casting from vector to Python type
#include <vector>
#include <cmath>
#include <vector>

extern "C"
{
#include <c/constants.h>
#include <c/functions.h>
#include <c/structs.h>
}
#include <cpp/constants.h>
#include <cpp/functions.h>
#include <cpp/inherited_classes.h>
#include <cpp/namespace_simple_class.h>
#include <cpp/simple_classes.h>
#include <cpp/virtual_classes.h>

using namespace pybind11::literals;

void init_attributes_submodule(pybind11::module &m) {
    m.doc() = "pybind11 attributes example plugin"; // optional module docstring
    m.attr("PI") = PI;
    m.attr("CONST_RAW_STRING") = CONST_RAW_STRING;
    m.attr("CONST_STRING") = CONST_STRING;
    m.attr("PRIME_NUMBERS") = pybind11::cast(PRIME_NUMBERS);
}

// Necessary class for virtual function to works
class PyShape : public Shape {
public:
    // Inherit the constructors
    using Shape::Shape;

    // Trampoline (need one for each virtual function)
    double area() const override {
        PYBIND11_OVERLOAD_PURE(
                double,     // Return type
                Shape,      // Parent class
                area,       // Name of function in C++ (must match Python name)
        );
    }
};


    void print_hello();
    int add(int, int);


void init_functions_submodule(pybind11::module &m) {
    m.doc() = "pybind11 function example plugin"; // optional module docstring
    m.def("print_hello", &print_hello, "A function which prints hello");
    m.def("add", &add, "i"_a, "j"_a, "A function which adds two ints");
    m.def("plus_two_list", &plus_two_list, "v"_a, "A function which adds two to each elements of a list");
}


void init_struct_submodule(pybind11::module &m) {
    m.doc() = "pybind11 struct example plugin"; // optional module docstring
    pybind11::class_<CPoint>(m, "CPoint")
            .def(pybind11::init<>())
            .def(pybind11::init<double, double>())
            .def_readwrite("x", &CPoint::x)
            .def_readwrite("y", &CPoint::y)
            .def("__repr__", [](const CPoint& p){return "[" + std::to_string(p.x) + ", " + std::to_string(p.y) + "]";});

    pybind11::class_<CRectangle>(m, "CRectangle")
            .def(pybind11::init<>())
            .def(pybind11::init<CPoint, CPoint>())
            .def_readwrite("top_left", &CRectangle::top_left)
            .def_readwrite("bottom_right", &CRectangle::bottom_right);
}


void init_class_submodule(pybind11::module &m) {
    m.doc() = "pybind11 class example plugin"; // optional module docstring
    pybind11::class_<Point>(m, "Point")
            .def(pybind11::init<>())
            .def(pybind11::init<double, double>())
            .def_readwrite("x", &Point::x)
            .def_readwrite("y", &Point::y)
            .def("__repr__", [](const Point& p){return "[" + std::to_string(p.x) + ", " + std::to_string(p.y) + "]";});

    pybind11::class_<Shape, PyShape>(m, "Shape") // <--- trampoline
            .def(pybind11::init<>())
            .def("area", &Shape::area)
            .def("is_shape", &Shape::is_shape);

    pybind11::class_<Rectangle, Shape>(m, "Rectangle")
            .def(pybind11::init<>())
            .def(pybind11::init<const Point&, const Point&>());

    pybind11::class_<Circle>(m, "Circle")
            .def(pybind11::init<>())
            .def(pybind11::init<const Point&, double>())
            .def_readwrite("center", &Circle::center)
            .def_readwrite("radius", &Circle::radius)
            .def("area", &Circle::area);

    pybind11::class_<space::Planet>(m, "Planet")
            .def(pybind11::init<const std::string&, double>())
            .def_property_readonly("name", &space::Planet::name)
            .def_property_readonly("mass", &space::Planet::mass);
}

PYBIND11_MODULE(pybind_example, m) {
    init_attributes_submodule(m.def_submodule("constants", "Submodule containing attributes examples"));
    init_functions_submodule(m.def_submodule("functions", "Submodule containing functions examples"));
    init_struct_submodule(m.def_submodule("structs", "Submodule containing struct examples"));
    init_class_submodule(m.def_submodule("classes", "Submodule containing class examples"));
}
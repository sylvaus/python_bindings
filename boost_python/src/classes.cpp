#define BOOST_PYTHON_STATIC_LIB
#include <boost/python.hpp>
#include <boost/shared_ptr.hpp>
#include <boost/make_shared.hpp>
#include <iostream>

#include <cpp/inherited_classes.h>
#include <cpp/namespace_simple_class.h>
#include <cpp/simple_classes.h>
#include <cpp/virtual_classes.h>

// necessary for repr to work
std::ostream& operator<<(std::ostream& os, const Point& p)
{
    os << "[" + std::to_string(p.x) + ", " + std::to_string(p.y) + "]";
    return os;
}

// Necessary for virtual methods
struct ShapeWrap: Shape, boost::python::wrapper<Shape>
{
    double area() const
    {
        return this->get_override("area")();
    }
};

BOOST_PYTHON_MODULE(classes)
{
    using namespace boost::python;
    class_<Point>("Point")
            .def(init<>())
            .def(init<double, double>())
            .def_readwrite("x", &Point::x)
            .def_readwrite("y", &Point::y);
    
    class_<ShapeWrap, boost::noncopyable>("Shape")
            .def(init<>())
            .def("area", pure_virtual(&Shape::area))
            .def("is_shape", &Shape::is_shape);

    class_<Rectangle, bases<Shape>>("Rectangle")
            .def(init<>())
            .def(init<const Point&, const Point&>());

    class_<Circle>("Circle")
            .def(init<>())
            .def(init<const Point&, double>())
            .def_readwrite("center", &Circle::center)
            .def_readwrite("radius", &Circle::radius)
            .def("area", &Circle::area);

    class_<space::Planet>("Planet", init<const std::string&, double>())
            .add_property("name", &space::Planet::name)
            .add_property("mass", &space::Planet::mass);
}
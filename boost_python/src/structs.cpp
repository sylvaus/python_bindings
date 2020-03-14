#define BOOST_PYTHON_STATIC_LIB
#include <boost/python.hpp>
#include <boost/shared_ptr.hpp>
#include <boost/make_shared.hpp>
#include <iostream>

extern "C"
{
#include <c/structs.h>
}

// necessary for repr to work
std::ostream& operator<<(std::ostream& os, const CPoint& p)
{
    os << "[" + std::to_string(p.x) + ", " + std::to_string(p.y) + "]";
    return os;
}

boost::shared_ptr<CPoint> init_cpoint(double x = 0, double y = 0)
{
    auto p = boost::make_shared<CPoint>();
    p->x = x;
    p->y = y;
    return p;
}

boost::shared_ptr<CRectangle> init_rectangle(CPoint top_left = CPoint(), CPoint bottom_right = CPoint())
{
    auto r = boost::make_shared<CRectangle>();
    r->top_left = top_left;
    r->bottom_right = bottom_right;
    return r;
}

BOOST_PYTHON_MODULE(structs)
{
    using namespace boost::python;
    class_<CPoint, boost::shared_ptr<CPoint>>("CPoint")
        .def("__init__", make_constructor(&init_cpoint))
        .def_readwrite("x", &CPoint::x)
        .def_readwrite("y", &CPoint::y)
        .def(repr(self))
    ;

    class_<CRectangle, boost::shared_ptr<CRectangle>>("CRectangle")
        .def("__init__", make_constructor(&init_rectangle))
        .def_readwrite("top_left", &CRectangle::top_left)
        .def_readwrite("bottom_right",&CRectangle::bottom_right)
    ;
}
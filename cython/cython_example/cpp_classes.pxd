# distutils: language = c++
from libcpp cimport bool
from libcpp.string cimport string

cdef extern from "cpp/simple_classes.h":
    cdef cppclass Point:
        Point() except +
        Point(double, double) except +
        double x, y
        double norm()

    cdef cppclass Circle:
        Circle() except +
        Circle(const Point& center, double radius)  except +
        double area()
        Point center
        double radius


cdef extern from "cpp/virtual_classes.h":
    cdef cppclass Shape:
        double area()
        bool is_shape()

    cdef cppclass Rectangle(Shape):
        Rectangle() except +
        Rectangle(const Point& top_left, const Point& bottom_right)  except +


cdef extern from "cpp/namespace_simple_class.h" namespace "space":
    cdef cppclass Planet:
        Planet(const string &name, double mass)
        string name()
        double mass()
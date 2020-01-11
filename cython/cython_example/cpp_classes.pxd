# distutils: language = c++

cdef extern from "cpp/simple_classes.h":
    cdef cppclass Point:
        Point() except +
        Point(double, double) except +
        double x, y
        double norm()

    cdef cppclass Circle:
        Circle()
        Circle(const Point& center, double radius)  except +
        double area()
        Point center
        double radius
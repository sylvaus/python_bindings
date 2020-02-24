# distutils: language = c++
from libcpp.string cimport string
from . cimport cpp_classes

cdef class Point:
    cdef cpp_classes.Point _point

    def __cinit__(self, double x = 0, double y = 0):
        self._point = cpp_classes.Point(x, y)

    def norm(self):
        return self._point.norm()

    @property
    def x(self):
        return self._point.x

    @x.setter
    def x(self, value):
        self._point.x = value

    @property
    def y(self):
        return self._point.y

    @y.setter
    def y(self, value):
        self._point.y = value

cdef class Circle:
    cdef cpp_classes.Circle _circle

    def __cinit__(self, Point center=None, double radius=0.0):
        if center is None:
            center = Point()

        self._circle = cpp_classes.Circle(center._point, radius)

    def area(self):
        return self._circle.area()

    @property
    def center(self):
        return Point(self._circle.center.x, self._circle.center.y)

    @center.setter
    def center(self, center):
        pass

    @property
    def radius(self):
        return self._circle.radius

    @radius.setter
    def radius(self, value):
        self._circle.radius = value

cdef class Rectangle:
    cdef cpp_classes.Rectangle _rectangle

    def __cinit__(self, Point top_left=None, Point bottom_right=None):
        if top_left is None:
            top_left = Point()
        if bottom_right is None:
            bottom_right = Point()
        self._rectangle = cpp_classes.Rectangle(top_left._point, bottom_right._point)

    def area(self):
        return self._rectangle.area()

    def is_shape(self):
        return self._rectangle.is_shape()


cdef class Planet:
    # pointer necessary when default constructor is not provided
    cdef cpp_classes.Planet* _planet

    def __cinit__(self, name="", double mass=0.0):
        self._planet = new cpp_classes.Planet(name.encode("UTF-8"), mass)

    @property
    def name(self):
        return self._planet.name().decode("UTF-8")

    @property
    def mass(self):
        return self._planet.mass()

    def __dealloc__(self):
        del self._planet


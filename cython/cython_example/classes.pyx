# distutils: language = c++

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

    def __cinit__(self, Point center, double radius):
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
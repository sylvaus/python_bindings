from . cimport c_structs

cdef class CPoint:
    cdef c_structs.CPoint _point

    def __init__(self, x = 0, y = 0):
        self._point.x = x
        self._point.y = y

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


cdef class CRectangle:
    cdef c_structs.CRectangle _rectangle

    def __cinit__(self, CPoint top_left = CPoint(), CPoint bottom_right = CPoint()):
        self._rectangle = c_structs.CRectangle(top_left._point, bottom_right._point)

    cdef _get_pointer(self, CPoint p):
        return p._point

    @property
    def top_left(self):
        return CPoint(self._rectangle.top_left.x, self._rectangle.top_left.y)

    @top_left.setter
    def top_left(self, point):
        self._rectangle.top_left = self._get_pointer(point)

    @property
    def bottom_right(self):
        return CPoint(self._rectangle.bottom_right.x, self._rectangle.bottom_right.y)

    @bottom_right.setter
    def bottom_right(self, point):
        self._rectangle.bottom_right = self._get_pointer(point)


# distutils: language = c

cdef extern from "c/structs.h":
    struct CPoint:
        double x, y;

    struct CRectangle:
        CPoint top_left, bottom_right;
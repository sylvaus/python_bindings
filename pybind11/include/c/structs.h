#ifndef C_STRUCTS_H
#define C_STRUCTS_H

typedef struct CPoint
{
    double x, y;
} CPoint;

typedef struct CRectangle
{
    CPoint top_left, bottom_right;
} CRectangle;

#endif
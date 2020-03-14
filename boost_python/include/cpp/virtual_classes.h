#ifndef CPP_VIRTUAL_CLASSES_H
#define CPP_VIRTUAL_CLASSES_H

#include "cpp/simple_classes.h"

class Shape
{
public:
    bool is_shape(); // here to see if function is inherited properly
    virtual double area() const = 0;
    virtual ~Shape() {};
};

class Rectangle: public Shape
{
public:
    Rectangle();
    Rectangle(const Point& top_left, const Point& bottom_right);

    double area() const override;
    Point top_left, bottom_right;
};

#endif

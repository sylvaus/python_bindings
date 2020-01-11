#ifndef CPP_SIMPLE_CLASS_H
#define CPP_SIMPLE_CLASS_H

class Point
{
public:
    double x, y;

    double norm();
};

class Circle
{
public:
    Point center;
    double radius;
    Circle();
    Circle(const Point& center, double radius);
    double area();
};

#endif


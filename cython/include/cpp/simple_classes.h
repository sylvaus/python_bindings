#ifndef CPP_SIMPLE_CLASS_H
#define CPP_SIMPLE_CLASS_H

class Point
{
public:
    double x, y;
    Point();
    Point(double x, double y);
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


#include "cpp/simple_classes.h"

Point::Point(): x{0}, y{0} {};
Point::Point(double x, double y): x{x}, y{y} {};

double Point::norm()
{
    return x * x + y * y;
}

Circle::Circle(): center{0, 0}, radius(0) {};
Circle::Circle(const Point& center, double radius): center(center), radius(radius) {};
double Circle::area()
{
    return 3.14159265359 * radius * radius;
}



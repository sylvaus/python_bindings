
#include <cmath>
#include "cpp/virtual_classes.h"

bool Shape::is_shape()
{
    return true;
}

Rectangle::Rectangle(): top_left{}, bottom_right{} {};
Rectangle::Rectangle(const Point& top_left, const Point& bottom_right): top_left(top_left), bottom_right(bottom_right) {};

double Rectangle::area() const
{
    return std::fabs(top_left.x - bottom_right.x) * std::fabs(top_left.y - bottom_right.y);
}




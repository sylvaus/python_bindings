
#include <cmath>
#include "cpp/virtual_classes.h"


Rectangle::Rectangle(const Point& top_left, const Point& bottom_right): top_left(top_left), bottom_right(bottom_right) {};

double Rectangle::area() const
{
    return std::fabs(top_left.x - bottom_right.x) * std::fabs(top_left.y - bottom_right.y);
}




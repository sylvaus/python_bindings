
#include "cpp/namespace_simple_class.h"

namespace space
{
    space::Planet::Planet(const std::string &name, double mass): name_(name), mass_(mass)
    {}

    std::string Planet::name()
    {
        return name_;
    }

    double Planet::mass()
    {
        return mass_;
    }
}

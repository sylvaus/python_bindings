#ifndef CPP_NAMESPACE_SIMPLE_CLASS_H
#define CPP_NAMESPACE_SIMPLE_CLASS_H

#include <string>

namespace space
{
    class Planet
    {
    public:
        std::string name;
        double mass;
        Planet(const std::string& name, double mass);
    };
}

#endif

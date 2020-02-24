#ifndef CPP_NAMESPACE_SIMPLE_CLASS_H
#define CPP_NAMESPACE_SIMPLE_CLASS_H

#include <string>

namespace space
{
    class Planet
    {
    public:
        Planet(const std::string& name, double mass);
        std::string name();
        double mass();
    private:
        std::string name_;
        double mass_;
    };
}

#endif

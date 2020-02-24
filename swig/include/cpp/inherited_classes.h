#ifndef CPP_INHERITED_CLASSES_H
#define CPP_INHERITED_CLASSES_H

#include <string>

class Person
{
public:
    std::string name;

    Person(const std::string& name);
};

class Student: public Person
{
public:
    int id_number;

    Student(const std::string& name, int id_number);
};

#endif

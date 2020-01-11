#include "cpp/inherited_classes.h"

Person::Person(const std::string& name): name(name) {};


Student::Student(const std::string& name, const int id_number): Person(name), id_number(id_number){};




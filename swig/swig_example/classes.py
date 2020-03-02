# This file was automatically generated by SWIG (http://www.swig.org).
# Version 4.0.1
#
# Do not make changes to this file unless you know what you are doing--modify
# the SWIG interface file instead.

from sys import version_info as _swig_python_version_info
if _swig_python_version_info < (2, 7, 0):
    raise RuntimeError("Python 2.7 or later required")

# Import the low-level C/C++ module
if __package__ or "." in __name__:
    from . import _classes
else:
    import _classes

try:
    import builtins as __builtin__
except ImportError:
    import __builtin__

def _swig_repr(self):
    try:
        strthis = "proxy of " + self.this.__repr__()
    except __builtin__.Exception:
        strthis = ""
    return "<%s.%s; %s >" % (self.__class__.__module__, self.__class__.__name__, strthis,)


def _swig_setattr_nondynamic_instance_variable(set):
    def set_instance_attr(self, name, value):
        if name == "thisown":
            self.this.own(value)
        elif name == "this":
            set(self, name, value)
        elif hasattr(self, name) and isinstance(getattr(type(self), name), property):
            set(self, name, value)
        else:
            raise AttributeError("You cannot add instance attributes to %s" % self)
    return set_instance_attr


def _swig_setattr_nondynamic_class_variable(set):
    def set_class_attr(cls, name, value):
        if hasattr(cls, name) and not isinstance(getattr(cls, name), property):
            set(cls, name, value)
        else:
            raise AttributeError("You cannot add class attributes to %s" % cls)
    return set_class_attr


def _swig_add_metaclass(metaclass):
    """Class decorator for adding a metaclass to a SWIG wrapped class - a slimmed down version of six.add_metaclass"""
    def wrapper(cls):
        return metaclass(cls.__name__, cls.__bases__, cls.__dict__.copy())
    return wrapper


class _SwigNonDynamicMeta(type):
    """Meta class to enforce nondynamic attributes (no new attributes) for a class"""
    __setattr__ = _swig_setattr_nondynamic_class_variable(type.__setattr__)


class Point(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    x = property(_classes.Point_x_get, _classes.Point_x_set)
    y = property(_classes.Point_y_get, _classes.Point_y_set)

    def __init__(self, *args):
        _classes.Point_swiginit(self, _classes.new_Point(*args))

    def norm(self):
        return _classes.Point_norm(self)
    __swig_destroy__ = _classes.delete_Point

# Register Point in _classes:
_classes.Point_swigregister(Point)

class Circle(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    center = property(_classes.Circle_center_get, _classes.Circle_center_set)
    radius = property(_classes.Circle_radius_get, _classes.Circle_radius_set)

    def __init__(self, *args):
        _classes.Circle_swiginit(self, _classes.new_Circle(*args))

    def area(self):
        return _classes.Circle_area(self)
    __swig_destroy__ = _classes.delete_Circle

# Register Circle in _classes:
_classes.Circle_swigregister(Circle)

class Shape(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")

    def __init__(self, *args, **kwargs):
        raise AttributeError("No constructor defined - class is abstract")
    __repr__ = _swig_repr

    def is_shape(self):
        return _classes.Shape_is_shape(self)

    def area(self):
        return _classes.Shape_area(self)
    __swig_destroy__ = _classes.delete_Shape

# Register Shape in _classes:
_classes.Shape_swigregister(Shape)

class Rectangle(Shape):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, *args):
        _classes.Rectangle_swiginit(self, _classes.new_Rectangle(*args))

    def area(self):
        return _classes.Rectangle_area(self)
    top_left = property(_classes.Rectangle_top_left_get, _classes.Rectangle_top_left_set)
    bottom_right = property(_classes.Rectangle_bottom_right_get, _classes.Rectangle_bottom_right_set)
    __swig_destroy__ = _classes.delete_Rectangle

# Register Rectangle in _classes:
_classes.Rectangle_swigregister(Rectangle)

class Person(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    name = property(_classes.Person_name_get, _classes.Person_name_set)

    def __init__(self, name):
        _classes.Person_swiginit(self, _classes.new_Person(name))
    __swig_destroy__ = _classes.delete_Person

# Register Person in _classes:
_classes.Person_swigregister(Person)

class Student(Person):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr
    id_number = property(_classes.Student_id_number_get, _classes.Student_id_number_set)

    def __init__(self, name, id_number):
        _classes.Student_swiginit(self, _classes.new_Student(name, id_number))
    __swig_destroy__ = _classes.delete_Student

# Register Student in _classes:
_classes.Student_swigregister(Student)

class Planet(object):
    thisown = property(lambda x: x.this.own(), lambda x, v: x.this.own(v), doc="The membership flag")
    __repr__ = _swig_repr

    def __init__(self, name, mass):
        _classes.Planet_swiginit(self, _classes.new_Planet(name, mass))

    def name(self):
        return _classes.Planet_name(self)

    def mass(self):
        return _classes.Planet_mass(self)
    __swig_destroy__ = _classes.delete_Planet

# Register Planet in _classes:
_classes.Planet_swigregister(Planet)




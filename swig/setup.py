from distutils.core import setup, Extension

ext_modules = [
    Extension(
        "swig_example._constants"
        , sources=["src/cpp/constants_wrap.cxx"]
        , include_dirs=["include"]
    )
    , Extension(
        "swig_example._cfunctions"
        , sources=["src/c/cfunctions_wrap.c", "src/c/functions.c"]
        , include_dirs=["include"]
    )
    , Extension(
        "swig_example._cppfunctions"
        , sources=["src/cpp/cppfunctions_wrap.cxx", "src/cpp/functions.cpp"]
        , include_dirs=["include"]
    )
    , Extension(
        "swig_example._structs"
        , sources=["src/c/structs_wrap.c"]
        , include_dirs=["include"]
    )
    , Extension(
        "swig_example._classes"
        , sources=[
            "src/cpp/classes_wrap.cxx", "src/cpp/simple_classes.cpp", "src/cpp/virtual_classes.cpp"
            , "src/cpp/inherited_classes.cpp", "src/cpp/namespace_simple_class.cpp"
        ]
        , include_dirs=["include"]
    )
]

setup(
    name="swig_example",
    ext_modules=ext_modules,
    packages=["swig_example"],
)
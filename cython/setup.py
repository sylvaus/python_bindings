import glob
from distutils.core import setup
from distutils.extension import Extension
from Cython.Build import cythonize



setup(
    name="cython_example",
    ext_modules=cythonize([
        Extension(
            "cython_example.constants"
            , ["cython_example/constants.pyx"]
            , include_dirs=["include"]
        )
        , Extension(
            "cython_example.cfunctions"
            , ["cython_example/cfunctions.pyx", "src/c/functions.c"]
            , include_dirs=["include"]
        )
        , Extension(
            "cython_example.cppfunctions"
            , ["cython_example/cppfunctions.pyx", "src/cpp/functions.cpp"]
            , include_dirs=["include"]
        )
        , Extension(
            "cython_example.structs"
            , ["cython_example/structs.pyx"]
            , include_dirs=["include"]
        )
        , Extension(
            "cython_example.classes"
            , ["cython_example/classes.pyx", "src/cpp/simple_classes.cpp"]
            , include_dirs=["include"]
        )]
        , compiler_directives={"language_level": 3, "embedsignature": True}
    )
)
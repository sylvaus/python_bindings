from distutils.core import setup, Extension

example_module = Extension(
    "swig_example._constants"
    , sources=['src/c/constants_wrap.c']
    , include_dirs=["include"]
)

setup(
    name="swig_example",
    ext_modules=[example_module],
    packages=["swig_example"],
)
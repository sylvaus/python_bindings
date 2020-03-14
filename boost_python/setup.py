import os

from setuptools import Extension, setup

# This required boost installation (tested with 1.72)
# Modify the BOOST_ROOT_FOLDER below to fit your installation
# The options are needed: link=static runtime-link=static
BOOST_ROOT_FOLDER = r"C:\boost"
BOOST_STAGE_LIB = os.path.join(BOOST_ROOT_FOLDER, r"stage\lib")
BOOST_STAGE_LIB_LINKER = f"/LIBPATH:{BOOST_STAGE_LIB}"

ext_modules = [
    Extension(
        'boost_example.constants'
        , ['src/constants.cpp']
        , include_dirs=["include", BOOST_ROOT_FOLDER]
        , extra_link_args=[BOOST_STAGE_LIB_LINKER]
        , library_dirs=[BOOST_STAGE_LIB]
        , language='c++'
    ),
    Extension(
        'boost_example.functions'
        , ['src/functions.cpp', 'src/c/functions.c', 'src/cpp/functions.cpp']
        , include_dirs=["include", BOOST_ROOT_FOLDER]
        , extra_link_args=[BOOST_STAGE_LIB_LINKER]
        , library_dirs=[BOOST_STAGE_LIB]
        , language='c++'
    ),
    Extension(
        'boost_example.structs'
        , ['src/structs.cpp']
        , include_dirs=["include", BOOST_ROOT_FOLDER]
        , extra_link_args=[BOOST_STAGE_LIB_LINKER]
        , library_dirs=[BOOST_STAGE_LIB]
        , language='c++'
    ),
    Extension(
        'boost_example.classes'
        , ['src/classes.cpp', 'src/cpp/inherited_classes.cpp'
            , 'src/cpp/namespace_simple_class.cpp', 'src/cpp/simple_classes.cpp'
            , 'src/cpp/virtual_classes.cpp'
        ]
        , include_dirs=["include", BOOST_ROOT_FOLDER]
        , extra_link_args=[BOOST_STAGE_LIB_LINKER]
        , library_dirs=[BOOST_STAGE_LIB]
        , language='c++'
    ),
]

setup(
    name='boost_example',
    ext_modules=ext_modules
)
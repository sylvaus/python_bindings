import os
import shutil
import subprocess as sbp

THIS_FOLDER = os.path.abspath(os.path.dirname(__file__))
C_SWIG_COMMAND = ["swig", "-python", "-Iinclude"]
CPP_SWIG_COMMAND = ["swig", "-c++", "-python", "-Iinclude"]
# Swig files have to be put in a folder named swig_example otherwise they won<t have the right import
SWIG_FOLDER = os.path.join(THIS_FOLDER, "swig", "swig_example")
C_SWIG_FILES = [
    "cfunctions.i"
    , "structs.i"
]
CPP_SWIG_FILES = [
    "constants.i"
    , "cppfunctions.i"
    , "classes.i"
]
C_OUTPUT_FOLDER = os.path.join(THIS_FOLDER, "src", "c")
CPP_OUTPUT_FOLDER = os.path.join(THIS_FOLDER, "src", "cpp")
PYTHON_OUTPUT_FOLDER = os.path.join(THIS_FOLDER, "swig_example")
C_WRAP_EXTENSION = "_wrap.c"
CPP_WRAP_EXTENSION = "_wrap.cxx"


def delete_file(filepath):
    if os.path.exists(filepath):
        os.remove(filepath)


def generate_wrapper(filename, command, swig_folder, wrap_ext, src_folder, py_folder):
    name = filename.rsplit(".", 1)[0]
    sbp.run(command + [os.path.join(swig_folder, filename)])
    c_file = os.path.join(swig_folder, name + wrap_ext)
    python_file = os.path.join(swig_folder, name + ".py")
    delete_file(os.path.join(src_folder, name + wrap_ext))
    shutil.move(c_file, src_folder)
    delete_file(os.path.join(py_folder, name + ".py"))
    shutil.move(python_file, py_folder)


def main():
    for filename in C_SWIG_FILES:
        generate_wrapper(
            filename, C_SWIG_COMMAND, SWIG_FOLDER, C_WRAP_EXTENSION, C_OUTPUT_FOLDER, PYTHON_OUTPUT_FOLDER
        )

    for filename in CPP_SWIG_FILES:
        generate_wrapper(
            filename, CPP_SWIG_COMMAND, SWIG_FOLDER, CPP_WRAP_EXTENSION, CPP_OUTPUT_FOLDER, PYTHON_OUTPUT_FOLDER
        )


if __name__ == '__main__':
    main()

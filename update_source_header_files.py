import os
import shutil

SRC_FOLDERS_TO_COPY = ["c_cpp_code/src/c", "c_cpp_code/src/cpp"]
INCLUDE_FOLDERS_TO_COPY = ["c_cpp_code/include/c", "c_cpp_code/include/cpp"]
TARGET_FOLDERS = ["boost_python", "cython", "pybind11", "swig"]


def main():
    for target_folder in TARGET_FOLDERS:
        copy_folders(SRC_FOLDERS_TO_COPY, target_folder, "src")
        copy_folders(INCLUDE_FOLDERS_TO_COPY, target_folder, "include")


def copy_folders(folders_to_copy, target_folder, subfolder):
    for src_folder in folders_to_copy:
        dst_folder = os.path.join(
            target_folder
            , subfolder
            , os.path.basename(src_folder)
        )

        os.makedirs(os.path.dirname(dst_folder), exist_ok=True)
        if os.path.exists(dst_folder):
            shutil.rmtree(dst_folder)

        shutil.copytree(src_folder, dst_folder)


if __name__ == '__main__':
    main()

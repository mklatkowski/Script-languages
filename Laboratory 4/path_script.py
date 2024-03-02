import os
import sys


def print_path_dirs():
    path_dirs = os.environ['PATH'].split(os.pathsep)
    for dir in path_dirs:
        print(dir)

def print_executables_in_dir(dir):
    path_dirs = os.environ['PATH'].split(os.pathsep)

    for dir in path_dirs:

        if os.path.isdir(dir):
            files = os.listdir(dir)
            executables = [f for f in files if os.access(os.path.join(dir, f), os.X_OK)]
            print(f"Executable files in {dir}:")
            for file in executables:
                print(os.path.join(dir, file))

if len(sys.argv) > 1:
    print_executables_in_dir(dir)
else:
    print_path_dirs()
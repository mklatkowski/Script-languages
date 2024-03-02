import os
import sys


if len(sys.argv) > 1:
    filtered_vars = {}
    for arg in sys.argv[1:]:
        if arg in os.environ:
            filtered_vars[arg] = os.environ[arg]
    for var_name in sorted(filtered_vars.keys()):
        print(f"{var_name} = {filtered_vars[var_name]}")
else:
    for var_name in sorted(os.environ.keys()):
        print(f"{var_name} = {os.environ[var_name]}")
import os
import sys

PYTHON3BIN = "python3"


def run(argv):
    if len(argv) != 2:
        print("Usage: smoketest.py <approvaltests version number>")
        return
    os.system("rm -rf smoke_test_env")
    os.system(PYTHON3BIN + " -m venv smoke_test_env")
    os.system("smoke_test_env/bin/pip install approvaltests==" + argv[1])
    os.system("smoke_test_env/bin/python test_hello_world.py")


if __name__ == "__main__":
    run(sys.argv)

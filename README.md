# approvaltests-python-smoketest
A little hack to check if a specific ApprovalTests.Python library version blows up or not

# Use

Example runs on Ubuntu 20.04:

```bash
olof@computer$ python3 smoketest.py 0.3
Collecting approvaltests==0.3
  Using cached approvaltests-0.3.0-py3-none-any.whl (21 kB)
... # lots of things being installed
Successfully installed approvaltests-0.3.0 attrs-21.2.0 iniconfig-1.1.1 packaging-21.3 pluggy-1.0.0 py-1.11.0 pyparsing-3.0.6 pyperclip-1.5.27 pytest-6.2.5 toml-0.10.2
.
----------------------------------------------------------------------
Ran 1 test in 0.006s

OK
```

```bash
olof@computer$ python3 smoketest.py 3.1
Collecting approvaltests==3.1
  Downloading approvaltests-3.1.0-py3-none-any.whl (32 kB)
... # lots of things being installed
Successfully installed approvaltests-3.1.0 attrs-21.2.0 beautifulsoup4-4.10.0 bs4-0.0.1 iniconfig-1.1.1 packaging-21.3 pluggy-1.0.0 py-1.11.0 pyparsing-3.0.6 pyperclip-1.5.27 pytest-6.2.5 soupsieve-2.3.1 toml-0.10.2
Traceback (most recent call last):
  File "/home/olof/repos/unhosted/temp1/test_hello_world.py", line 2, in <module>
    from approvaltests import verify
  File "/home/olof/repos/unhosted/temp1/smoke_test_env/lib/python3.9/site-packages/approvaltests/__init__.py", line 2, in <module>
    from .utils import *
  File "/home/olof/repos/unhosted/temp1/smoke_test_env/lib/python3.9/site-packages/approvaltests/utils.py", line 5, in <module>
    import empty_files
ModuleNotFoundError: No module named 'empty_files'
```

# approvaltests-python-smoketest
A little hack to check if a specific ApprovalTests.Python library version blows up or not

# Use

Example runs on Ubuntu 20.04:

```bash
/home/olof/approvaltests-python-smoketest/$ python3 smoketest.py 0.3
Collecting approvaltests==0.3
  Using cached approvaltests-0.3.0-py3-none-any.whl (21 kB)
... # lots of things being installed
Successfully installed approvaltests-0.3.0 attrs-21.2.0 iniconfig-1.1.1 packaging-21.3 pluggy-1.0.0 py-1.11.0 pyparsing-3.0.6 pyperclip-1.5.27 pytest-6.2.5 toml-0.10.2
.
----------------------------------------------------------------------
Ran 1 test in 0.006s

OK
```

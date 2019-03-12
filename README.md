# python_test_sample_unittest
This project contains a code with basic math operations. It was created to make unit tests and comprehend how [unittest](https://docs.python.org/3/library/unittest.html) works.

## Executing tests
Before execute the tests, is necessary to install the dependencies using the following command:

`pip install -r requirements.txt`


After that, the tests can be executed using the following command:

`nose2`

The output should be something like this:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.010s
  
OK
```

Also, the tests can be executed checking the coverage. It is necessary to use the following command:

`nose2 -C --coverage python_test_sample/`

And the output should be something like this:

```
.........
----------------------------------------------------------------------
Ran 9 tests in 0.006s

OK
Name                 Stmts   Miss  Cover
----------------------------------------
python_test_sample/math_helper.py      12      0   100%
```
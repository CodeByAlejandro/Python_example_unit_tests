# Python_example_unit_tests
Python example project to showcase unit tests

# Installation
Install using following commands:
```shell
git clone https://github.com/CodeByAlejandro/Python_example_unit_tests.git
cd Python_example_unit_tests
```

# Usage
There are 2 ways to run testmodules:
1. Run a specific testmodule
2. Run all testmodules

## Examples
Simply run a specific testmodule:
```shell
python3 test_main.py
```
Output:
```

pre-test initialization
running test : test_bool_value_guess
post-test cleanup
.
pre-test initialization
post-test cleanup
.
pre-test initialization
running test : test_out_of_range_lower_bound_guess
post-test cleanup
.
pre-test initialization
running test : test_out_of_range_upper_bound_guess
post-test cleanup
.
pre-test initialization
running test : test_string_value_guess
post-test cleanup
.
pre-test initialization
running test : test_succesful_guess
post-test cleanup
.
pre-test initialization
running test : test_wrongh_guess
post-test cleanup
.
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```
Run all testmodules:
```shell
python3 -m unittest
```
Output:
```

pre-test initialization
running test : test_bool_value_guess
post-test cleanup
.
pre-test initialization
post-test cleanup
.
pre-test initialization
running test : test_out_of_range_lower_bound_guess
post-test cleanup
.
pre-test initialization
running test : test_out_of_range_upper_bound_guess
post-test cleanup
.
pre-test initialization
running test : test_string_value_guess
post-test cleanup
.
pre-test initialization
running test : test_succesful_guess
post-test cleanup
.
pre-test initialization
running test : test_wrongh_guess
post-test cleanup
.
----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```
Run all testmodules with verbose output:
```shell
python3 -m unittest -v
```
Output:
```
test_bool_value_guess (test_main.TestSuccesfulGuess) ...
pre-test initialization
running test : test_bool_value_guess
post-test cleanup
ok
test_none_value_guess (test_main.TestSuccesfulGuess) ...
pre-test initialization
post-test cleanup
ok
test_out_of_range_lower_bound_guess (test_main.TestSuccesfulGuess) ...
pre-test initialization
running test : test_out_of_range_lower_bound_guess
post-test cleanup
ok
test_out_of_range_upper_bound_guess (test_main.TestSuccesfulGuess) ...
pre-test initialization
running test : test_out_of_range_upper_bound_guess
post-test cleanup
ok
test_string_value_guess (test_main.TestSuccesfulGuess) ...
pre-test initialization
running test : test_string_value_guess
post-test cleanup
ok
test_succesful_guess (test_main.TestSuccesfulGuess) ...
pre-test initialization
running test : test_succesful_guess
post-test cleanup
ok
test_wrongh_guess (test_main.TestSuccesfulGuess) ...
pre-test initialization
running test : test_wrongh_guess
post-test cleanup
ok

----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```
Verbose output without extra print statements:
```
test_bool_value_guess (test_main.TestSuccesfulGuess) ... ok
test_none_value_guess (test_main.TestSuccesfulGuess) ... ok
test_out_of_range_lower_bound_guess (test_main.TestSuccesfulGuess) ... ok
test_out_of_range_upper_bound_guess (test_main.TestSuccesfulGuess) ... ok
test_string_value_guess (test_main.TestSuccesfulGuess) ... ok
test_succesful_guess (test_main.TestSuccesfulGuess) ... ok
test_wrongh_guess (test_main.TestSuccesfulGuess) ... ok

----------------------------------------------------------------------
Ran 7 tests in 0.001s

OK
```

# Uninstall
Remove the project:
```shell
cd ..
rm -rf Python_example_unit_tests
```

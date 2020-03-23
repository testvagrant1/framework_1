About Framework
==================
This fraamework is intended to provide api for test developer to write their suite.

Pre-requisite
==================

python module:
requests


How To Use
====================

For Tester
-------------------
1. Go to suites folder
2. .exp stand for expectation. Hence it hold expected information as per testcase.
3. .py is suite file. It is written by using python unittest framework module.
4. To execute:
	
	$> python -m unittest <suite file name without .py>
	
	Example:
		$> python -m unittest punkapi_test

For Test Developer
------------------
1. Refer link for python unittest framework: https://docs.python.org/3/library/unittest.html
2. Go to suites folder
3. import module from src/api/*
4. Write suite using unnitest framework


For framework Developer
-----------------------
1. Go to src/api folder
2. Create module
3. Go to Test folder and create test to verify module
4. Franework guideline will be update soon.

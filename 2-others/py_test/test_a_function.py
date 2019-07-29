# Why Test your code ?
# When you write a function or a class, you can also write tests for that code.
# Testing proves that your code works as it's supposed to in the situations it's designed to handle,
# and also when people use your programs in unexpected ways.
# Writing tests gives you confidence that your code will work correctly as more people begin to use your programs.
# You can also add new features to your programs and know that you haven't broken existing behavior.

# Unit test
#     - A unit test verifies that one specific aspect of your code works as it's supposed to.

# Test case
#     - A test case is a "Collection of unit tests", that  verify your code's behavior in a wide variety of situations

# Testing a Function
#     - A Function to Test - Passing testcase : get_full_name()
#     - Usecase where the Function is used : names
#     - Testcase : test_full_names()
#     - Run the test
#     - A Function to Test - Failing testcase : get_title_name() to return name in Title case
#     - Fix the Code - Without modifying your unit test

import unittest
from full_names import get_full_name
from full_names import get_title_name


class NamesTestCase(unittest.TestCase):
    """Tests for names.py"""

    def test_full_names(self):
        """Test names for Full Name Assertion"""
        full_name = get_full_name("Janis", "Joplin")
        self.assertEqual(full_name, "Janis Joplin")
    
    def test_full_names_small(self):
        """Test names for Full Name Assertion"""
        full_name = get_full_name("janis", "joplin")
        self.assertEqual(full_name, "janis joplin")

    def test_title_names(self):
        """Test names for Full Name in Title case Assertion"""
        title_name = get_title_name("Janis", "Joplin")
        self.assertEqual(title_name, "Janis Joplin")
    
    def test_title_names_small(self):
        """Test names for Full Name in Title case Assertion"""
        title_name = get_title_name("janis", "joplin")
        self.assertEqual(title_name, "Janis Joplin")

unittest.main()

# Python reports on each unit test in the test case. The dot reports a
# single passing test. Python informs us that it ran 1 test in less than
# 0.001 seconds, and the OK lets us know that all unit tests in the
# test case passed
# ####
# .
# ----------------------------------------------------------------------
# Ran 1 test in 0.001s

# OK


# Below is the output when
    # - 4 unit tests were run [ ...F ]
    # - The last unit test failed among them
    # - Traceback of the unit test method is printed
# ####
# ...F
# ======================================================================
# FAIL: test_title_names_mixed_case (__main__.NamesTestCase)
# Test names for Full Name in Title case Assertion
# ----------------------------------------------------------------------
# Traceback (most recent call last):
#   File ".\test_full_names.py", line 26, in test_title_names_mixed_case
#     self.assertEqual(title_name, "Janis Joplin")
# AssertionError: 'jaNis jOPlin' != 'Janis Joplin'
# - jaNis jOPlin
# + Janis Joplin
# ----------------------------------------------------------------------
# Ran 4 tests in 0.002s

# FAILED (failures=1)



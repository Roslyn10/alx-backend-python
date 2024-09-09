#!/usr/bin/env python3
"""A modules that contains unittests"""


import unittest
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """A class that tests the access nested map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
if __name__ == '__main__':
    unittest.main()

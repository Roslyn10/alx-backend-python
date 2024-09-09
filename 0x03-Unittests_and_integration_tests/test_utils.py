#!/usr/bin/env python3
"""A modules that contains unittests"""


import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """A class that tests the access nested map"""
    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2),
        ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map with various inputs"""
        self.assertEqual(access_nested_map(nested_map, path), expected)


    def test_access_nested_map_exception(self, nested_map, path, expected):
        """Test access_nested_map while raising an exception"""
        with self.assertRaises(exception):
            access_nested_map(nested_map, path)


if __name__ == '__main__':
    unittest.main()

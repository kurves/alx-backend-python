#!/usr/bin/env python3
"""Test Module for utils.access_nested_map"""

import unittest
from parameterized import parameterized
from utils import access_nested_map


class TestAccessNestedMap(unittest.TestCase):
    """Test class for access_nested_map function"""

    @parameterized.expand([
        ({"a": 1}, ("a",), 1),
        ({"a": {"b": 2}}, ("a",), {"b": 2}),
        ({"a": {"b": 2}}, ("a", "b"), 2)
    ])
    def test_access_nested_map(self, nested_map, path, expected):
        """Test access_nested_map with various inputs"""
        self.assertEqual(access_nested_map(nested_map, path), expected)

    @parameterized.expand([
        ({}, ("a",)),
        ({"a": 1}, ("a", "b")),
    ])
    def test_access_nested_map_exception(self, nested_map, path):
        """Test access_nested_map raises KeyError with correct message"""
        with self.assertRaises(KeyError) as context:
            access_nested_map(nested_map, path)
        self.assertEqual(str(context.exception), str(path[-1]))


class TestGetJson(unittest.TestCase):
    """
    Test class for utils.get_json function
    """

    @parameterized.expand([
        ("http://example.com", {"payload": True}),
        ("http://holberton.io", {"payload": False}),
    ])
    @patch('utils.requests.get')
    def test_get_json(self, test_url, test_payload, mock_get):
        """
        Test get_json method from utils module

        Args:
            test_url (str): URL to pass to get_json
            test_payload (dict): Expected payload to return

        Mocks:
            requests.get: Mocked to return a predefined response
        """

        mock_response = Mock()
        mock_response.json.return_value = test_payload

        mock_get.return_value = mock_response

        result = get_json(test_url)

        self.assertEqual(result, test_payload)

        mock_get.assert_called_once_with(test_url)


class TestMemoize(unittest.TestCase):
    """ Test class for memoize decorator """

    def test_memoize(self):
        """ Test memoize decorator with a mock """

        test_obj = TestClass()

        with patch.object(TestClass, 'a_method', return_value=42) as mock_method:
            first_call = test_obj.a_property
            second_call = test_obj.a_property

            self.assertEqual(first_call, 42)
            self.assertEqual(second_call, 42)

            mock_method.assert_called_once()
if __name__ == "__main__":
    unittest.main()

#!/usr/bin/env python3
"""A module that tests the client file"""

import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import Mock, patch


class TestGithubOrgClient(unittest.TestCase):
    @parameterized.expand([
        ("google"),
        ("abc"),
        ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org, mock_org):
        """Test GithubOrgClients org"""
        org_test = GithubOrgClient(org)
        test_response = org_test.org
        self.assertEqual(test_response, mock_org.return_value)
        mock_org.assert_called_once()


if __name__ == '__main__':
    unittest.main()

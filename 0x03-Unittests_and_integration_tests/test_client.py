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

    def test_public_repos_url(self):
        """test the property of a public repos url"""
        with patch("GithubOrgClient.org", new_callable=PropertyMock,) as mock_org:
            mock_org.return_value = {
                    'repos_url': "https://api.github.com/users/google/repos",
                    }
            self.assertEqual(
                    GithubOrgClient("google")._public_repos_url,
                    "https://api.github.com/users/google/repos",
                    )



if __name__ == '__main__':
    unittest.main()

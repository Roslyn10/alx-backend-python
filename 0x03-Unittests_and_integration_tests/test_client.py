#!/usr/bin/env python3
"""A module that tests the GithubOrgClient class"""

import unittest
from client import GithubOrgClient
from parameterized import parameterized
from unittest.mock import Mock, patch, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Test class for GithubOrgClient methods"""

    @parameterized.expand([
        ("google"),
        ("abc"),
    ])
    @patch('client.get_json', return_value={"payload": True})
    def test_org(self, org, mock_get_json):
        """Test GithubOrgClient.org returns the correct data"""
        org_test = GithubOrgClient(org)
        test_response = org_test.org
        self.assertEqual(test_response, mock_get_json.return_value)
        mock_get_json.assert_called_once()

    def test_public_repos_url(self):
        """Test the _public_repos_url property"""
        with patch(
                'client.GithubOrgClient.org', new_callable=PropertyMock
                ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://api.github.com/users/google/repos",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://api.github.com/users/google/repos",
            )

    @patch("client.get_json")
    def test_public_repos(self, mock_get_json):
        """Test the public_repos method"""
    with patch('client.GithubOrgClient._public_repos_url',
               new_callable=PropertyMock) as mock_public:

        mock_public.return_value = "https://api.github.com/org/repos"
        test_class = GithubOrgClient("test")
        result = test_class.public_repos()

        expected = [item["name"] for item in payload]
        self.assertEqual(result, expected)
        mock_public.assert_called_once()
        mock_json.assert_called_once()

    @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "other_license", False)
    ])
    def test_has_license(self, repo, license_key, expected):
        """Test the has_license static method"""
        result = GithubOrgClient.has_license(repo, license_key)
        self.assertEqual(result, expected)


class TestIntergrationGithubOrgClient(unittest.TestCase):
    """Integration test class for GithbOrgClient,
    focusing on extrnal requests"""

    def setUpClass(cls):
        """Set up the test environment before any test methods are run"""
        self.org_name = "google"
        self.client = GithubOrgClient(self.org_name)

    def test_public_repos(self):
        """Test public_repos method against mock data"""
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.org, self.org_payload)
        self.assertEqual(test_class.repos_payload, self.repos_payload)
        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("LICENSE"), [])
        self.mock.assert_called()

    def test_public_repos_wih_license(self):
        """Test public_repos_with_license againt the apache-2.0"""
        test_class = GithubOrgClient("google")

        self.assertEqual(test_class.public_repos(), self.expected_repos)
        self.assertEqual(test_class.public_repos("License", [])
        self.assertequal(test_class.publicrepos("apache-2.0"), self.apache2_repos)
        self.mock.assert_called()

    def tearDownClass(cls):
        """Tear down the test environment after all test methods haverun"""
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()

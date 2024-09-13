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
    @patch('client.get_json')
    def test_org(self, input, mock_get_json):
        """Test GithubOrgClient.org returns the correct data"""
        org_test = GithubOrgClient(input)
        test_response = org_test.org
        mock_get_json.called_with_once(orf_test.ORG_URL.format(org=input))

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


class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration test class for GithubOrgClient,
    focusing on external requests."""

    @classmethod
    def setUpClass(cls):
        """Set up the test environment before any test methods are run."""
        cls.org_name = "google"
        cls.client = GithubOrgClient(cls.org_name)
        cls.org_payload = {"https://api.github.com/orgs/google/repos"}
        cls.repos_payload = [
            {"name": "repo1", "license": {"key": "mit"}},
            {"name": "repo2", "license": {"key": "apache-2.0"}}
        ]
        cls.expected_repos = ["repo1", "repo2"]

        cls.get_patcher = patch('client.get_json', side_effect=[
            cls.org_payload, cls.repos_payload
            ])
        cls.mock_get_json = cls.get_patcher.start()

    def test_public_repos(self):
        """Test public_repos method against mock data."""
        self.assertEqual(self.client.org, self.org_payload)
        self.assertEqual(self.client.repos_payload, self.repos_payload)
        self.assertEqual(self.client.public_repos(), self.expected_repos)
        self.assertEqual(self.client.public_repos("XLICENSE"), [])
        self.mock_get_json.assert_called()

    def test_public_repos_with_license(self):
        """Test public_repos used to test public repos with license"""
        self.assertEqual(self.client.org, self.org_payload)
        self.assertEqual(self.client.repos_payload, self.repos_payload)
        self.assertEqual(self.client.public_repos(), self.expected_repos)
        self.assertEqual(self.client.public_repos("apache-2.0"), ["repo2"])
        self.mock_get_json.assert_called()

    @classmethod
    def tearDownClass(cls):
        """Tear down the test environment after all test methods have run."""
        cls.get_patcher.stop()


if __name__ == '__main__':
    unittest.main()

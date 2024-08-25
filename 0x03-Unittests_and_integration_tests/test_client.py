#!/usr/bin/env python3
"""
Unit tests for GithubOrgClient.
"""

import unittest
from unittest.mock import patch
from parameterized import parameterized
from client import GithubOrgClient


class TestGithubOrgClient(unittest.TestCase):
    """Test cases for GithubOrgClient"""

    @parameterized.expand([
        ("google",),
        ("abc",)
    ])
    @patch('client.get_json', return_value={'key': 'value'})
    def test_org(self, org_name, mock_get_json):
        """
        Test that GithubOrgClient.org returns the correct value.
        """
        client = GithubOrgClient(org_name)
        result = client.org

        mock_get_json.assert_called_once_with(f"https://api.github.com/orgs/{org_name}")
        self.assertEqual(result, {'key': 'value'})

    @patch('client.GithubOrgClient.org', new_callable=PropertyMock)
    def test_public_repos_url(self, mock_org):
        """
        Test that GithubOrgClient._public_repos_url returns the correct value.
        """
        mock_org.return_value = {"repos_url": "https://api.github.com/orgs/google/repos"}

        client = GithubOrgClient("google")

        result = client._public_repos_url

        self.assertEqual(result, "https://api.github.com/orgs/google/repos")


    @patch('client.get_json', return_value=[{'name': 'repo1'}, {'name': 'repo2'}])
    def test_public_repos(self, mock_get_json):
        """
        Test that GithubOrgClient.public_repos  repos.
        """
        with patch('client.GithubOrgClient._public_repos_url', new_callable=PropertyMock) as mock_public_repos_url:
            mock_public_repos_url.return_value = "https://api.github.com/orgs/google/repos"

            client = GithubOrgClient("google")

            repos = client.public_repos()

            self.assertEqual(repos, ['repo1', 'repo2'])

            mock_public_repos_url.assert_called_once()

            mock_get_json.assert_called_once_with("https://api.github.com/orgs/google/repos")

    
     @parameterized.expand([
        ({"license": {"key": "my_license"}}, "my_license", True),
        ({"license": {"key": "other_license"}}, "my_license", False),
        ({}, "my_license", False),
        ({"license": {}}, "my_license", False),
    ])
    def test_has_license(self, repo, license_key, expected):
        """
        Test that GithubOrgClient.has_license returns the correct boolean
        based on whether the repo has the specified license key.
        """
        client = GithubOrgClient("test_org")

        result = client.has_license(repo, license_key)

        self.assertEqual(result, expected)


@parameterized_class([
    {"org_payload": org_payload, "repos_payload": repos_payload, "expected_repos": expected_repos, "apache2_repos": apache2_repos},
])
class TestIntegrationGithubOrgClient(unittest.TestCase):
    """Integration tests for GithubOrgClient.public_repos."""

    @classmethod
    def setUpClass(cls):
        """Set up class method to patch requests.get and return fixture data."""
        cls.get_patcher = patch('requests.get')

        cls.mock_get = cls.get_patcher.start()

        cls.mock_get.side_effect = cls.mock_requests_get

    @classmethod
    def mock_requests_get(cls, url):
        """Mock requests.get().json() based on the requested URL."""
        if url == "https://api.github.com/orgs/google":
            return Mock(**{"json.return_value": cls.org_payload})
        elif url == "https://api.github.com/orgs/google/repos":
            return Mock(**{"json.return_value": cls.repos_payload})

    @classmethod
    def tearDownClass(cls):
        """Tear down class method to stop the patcher."""
        cls.get_patcher.stop()

    def test_public_repos(self):
        """Test public_repos method."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(), self.expected_repos)

    def test_public_repos_with_license(self):
        """Test public_repos method filtering by license."""
        client = GithubOrgClient("google")
        self.assertEqual(client.public_repos(license="apache-2.0"), self.apache2_repos)


if __name__ == "__main__":
    unittest.main()

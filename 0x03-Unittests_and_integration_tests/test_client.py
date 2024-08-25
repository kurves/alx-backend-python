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


if __name__ == "__main__":
    unittest.main()

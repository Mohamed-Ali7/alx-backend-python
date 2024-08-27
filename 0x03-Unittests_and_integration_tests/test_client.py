#!/usr/bin/env python3
"""This module contains TestGithubOrgClient class"""

from client import GithubOrgClient
from parameterized import parameterized
import unittest
from unittest.mock import patch, Mock, PropertyMock


class TestGithubOrgClient(unittest.TestCase):
    """Tests GithubOrgClient() class"""


    @parameterized.expand([("google", {"status": 200}), ("abc", {"status": 200})])
    @patch("client.get_json")
    def test_org(self, param1, response, mock_get_json):
        """Tests org() method"""

        mock_response = Mock()
        mock_response.return_value = response
        mock_get_json.return_value = mock_response
        git_org = GithubOrgClient(param1)
        self.assertEqual(git_org.org(), response)

    def test_public_repos_url(self):
        """tests `_public_repos_url property"""

        with patch(
                "client.GithubOrgClient.org",
                new_callable=PropertyMock,
                ) as mock_org:
            mock_org.return_value = {
                'repos_url': "https://example.com",
            }
            self.assertEqual(
                GithubOrgClient("google")._public_repos_url,
                "https://example.com",
            )


if __name__ == "__main__":
    unittest.main()

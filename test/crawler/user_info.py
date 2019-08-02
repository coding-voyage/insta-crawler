import unittest
import logging
from crawler.user_info import get_user_info_html_doc, get_followers

logger = logging.getLogger(__file__)

TEST_USER_ID = "zuck"


class UserInfoTest(unittest.TestCase):
    def test_get_user_info_html_doc(self):
        content = get_user_info_html_doc(TEST_USER_ID)
        self.assertTrue(content.startswith('<!DOCTYPE html>'))

    def test_get_followers(self):
        self.assertGreater(get_followers(TEST_USER_ID), 5335000)


if __name__ == '__main__':
    unittest.main()

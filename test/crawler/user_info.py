import logging
import unittest

from crawler.user_info import get_user_info_html_doc, get_followers, search_related_to, get_related_users_by

logger = logging.getLogger(__file__)

TEST_USER_ID = "zuck"


class UserInfoTest(unittest.TestCase):
    def test_get_user_info_html_doc(self):
        content = get_user_info_html_doc(TEST_USER_ID)
        self.assertTrue(content.startswith('<!DOCTYPE html>'))

    def test_get_followers(self):
        self.assertGreater(get_followers(TEST_USER_ID), 5335000)

    def test_search_related_to(self):
        self.assertTrue(search_related_to(TEST_USER_ID), list)

    def test_get_related_users_by_position(self):
        dict_position_user = get_related_users_by(TEST_USER_ID)
        for i in dict_position_user:
            self.assertTrue("pk" in dict_position_user[i])
            self.assertTrue("full_name" in dict_position_user[i])
            self.assertTrue("follower_count" in dict_position_user[i])


if __name__ == '__main__':
    unittest.main()

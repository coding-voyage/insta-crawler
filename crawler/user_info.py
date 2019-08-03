import json
import sys

import requests

BASIC_URI = "https://instagram.com"
SEARCH_API = "/web/search/topsearch/"
QUERY = "?query={}"
KEY_OF_FOLLOWERS = "userInteractionCount"
ENCODING = "utf-8"


def get_user_info_html_doc(user_id: str) -> str:
    response = requests.get(BASIC_URI + '/' + user_id)
    return check_response_and_get_content(response)


def get_followers(user_id: str) -> int:
    content = get_user_info_html_doc(user_id)
    if KEY_OF_FOLLOWERS in content:
        idx_start_key_of_followers = content.find(KEY_OF_FOLLOWERS)
        idx_start_colon = content.find(':', idx_start_key_of_followers)
        idx_start_value_of_followers = content.find("\"", idx_start_colon + 1)
        idx_end_value_of_followers = content.find("\"", idx_start_value_of_followers + 1)
        follower_str = content[idx_start_value_of_followers + 1: idx_end_value_of_followers]
        return int(follower_str)
    else:
        raise KeyError("No Such Key in the content - " + KEY_OF_FOLLOWERS)


def get_related_users_by(keyword: str) -> dict:
    """
    :param keyword: The word what you want to search the user id related to it
    :return: dict[int, user] The key(int) is the position of each user
    """
    result = {}
    for user_with_position in search_related_to(keyword).get("users"):
        position = user_with_position.get("position")  # int
        user = user_with_position.get("user")  # map
        result[position] = user
    return result


def search_related_to(keyword: str) -> dict:
    response = requests.get(BASIC_URI + SEARCH_API + QUERY.format(keyword))
    content = check_response_and_get_content(response)
    return json.loads(content)


def check_response_and_get_content(response: requests.Response) -> str:
    if response.status_code == 200:
        return str(response.content, ENCODING)
    else:
        response.raise_for_status()


if __name__ == '__main__':
    method = sys.argv[1]
    if method == 'get_followers':
        print(get_followers(sys.argv[2]))
    elif method == 'get_related_users_by':
        print(get_related_users_by(sys.argv[2]))

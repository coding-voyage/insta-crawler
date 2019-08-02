import requests

BASIC_URI = "https://instagram.com"
KEY_OF_FOLLOWERS = "userInteractionCount"
ENCODING = "utf-8"


def get_user_info_html_doc(user_id: str) -> str:
    response = requests.get(BASIC_URI + '/' + user_id)
    print(response)
    if response.status_code == 200:
        return str(response.content, ENCODING)
    else:
        response.raise_for_status()


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

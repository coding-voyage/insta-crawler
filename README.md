# insta-crawler

This is the crawler for Instagram.

It can get the follower count from the user information of the Instagram.

It can make the normal distribution of the follower count using the crawled follower count data.

It can make the user enable to check my ranking of the follower counts based on the normal distribution of it.

## Usage
### Get followers by user id
```console
>python crawler/user_info.py get_followers ${user id}
```
example
```console
>python crawler/user_info.py get_followers zuck
```

### Search related users by keyword
```console
>python crawler/user_info.py get_related_users_by ${user id}
```
example
```console
>python crawler/user_info.py get_related_users_by zuck
```

## LICENSE

[MIT](./LICENSE)

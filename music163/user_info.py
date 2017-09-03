import urllib
from bs4 import BeautifulSoup


def soup_result(result):
    soup = BeautifulSoup(result, "html.parser")

    return


def write_result(result):
    return


def get_user_playlist_info(playlist_id):
    # return song_id and song_name
    headers = {"Content-type": "application/x-www-form-urlencoded",
               'Accept-Language': 'zh-CN,zh;q=0.8',
               'User-Agent': "Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0",
               "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
               "Connection": "close",
               "Cache-Control": "no-cache"}
    url = "http://music.163.com/api/playlist/detail?id=82729253"
    req = urllib.request.Request(url=url, headers=headers)
    resp = urllib.request.urlopen(req)
    result = resp.read()
    soup_result(result)


def get_user_playlist(user_id):
    # return playlist_id and playlist_name
    playlist_id = ''
    playlist_name = ''
    user_playlist_list = []
    user_playlist_list.append({'playlist_id': playlist_id, 'playlist_name': playlist_name})
    return user_playlist_list


def search_user(search_word):
    # return 1 result:user_id and user_name
    user_id = ""
    user_name = ""
    search_result = {'user_id': user_id, 'user_name': user_name}
    return search_result

import urllib
from bs4 import BeautifulSoup
import requests

# s: 搜索词
# limit: 返回数量
# sub: 意义不明(非必须参数)；取值：false
# type:
#    1 单曲
#    10 专辑
#    100 歌手
#    1000 歌单
#    1002 用户

headers = {"Content-type": "application/x-www-form-urlencoded",
           'Accept-Language': 'zh-CN,zh;q=0.8',
           'User-Agent': "Mozilla/5.0 (Windows NT 6.1; rv:32.0) Gecko/20100101 Firefox/32.0",
           "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
           "Connection": "close",
           "Cache-Control": "no-cache"}
RETURN_MAX_LIMIT = 10000


def soup_result(result):
    soup = BeautifulSoup(result, "html.parser")

    return


def write_result(result):
    return


def get_user_playlist_info(playlist_id):
    # return song_id and song_name

    url = "http://music.163.com/api/playlist/detail?id=82729253"
    req = urllib.request.Request(url=url, headers=headers)
    resp = urllib.request.urlopen(req)
    result = resp.read()
    soup_result(result)


def get_user_playlist(user_id):
    # return playlist_id and playlist_name
    url = "http://music.163.com/api/user/playlist"
    req = requests.get(url, params={'uid': user_id, 'offset': 0, 'limit': RETURN_MAX_LIMIT})
    context = req.json()
    playlist_id = ''
    playlist_name = ''
    user_playlist_list = []
    user_playlist_list.append({'playlist_id': playlist_id, 'playlist_name': playlist_name})
    return user_playlist_list


def search_user(search_word):
    # return 1 result:user_id and user_name
    url = "http://music.163.com/api/search/get/"
    req = requests.post(url, data={'s': search_word, 'limit': 1, 'type': 1002})
    context = req.json()
    resp_code = context['code']
    print("返回结果"+str(resp_code))
    user_id = context['result']['userprofiles'][0]['userId']
    user_name = context['result']['userprofiles'][0]['nickname']
    search_result = {'user_id': user_id, 'user_name': user_name}
    return search_result

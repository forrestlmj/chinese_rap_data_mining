import requests


def get_lyric_text(song_id):
    url = "http://music.163.com/api/song/media"
    req = requests.get(url, params={'id': song_id})
    context = req.json()
    assert isinstance(context['lyric'], str)
    print(context['lyric'])
    return context['lyric']


def test():
    SONG_ID = '492151700'
    get_lyric_text(SONG_ID)
    return


def main():
    return


if __name__ == "__main__":
    test()
    main()

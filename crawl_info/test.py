
import requests as re
# 模拟firefox以view-source的方式访问
# https://music.163.com/discover/artist/cat?id=2001时候浏览器的请求头
headers = {
    "Host": "music.163.com",
    "User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
    "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
    "Accept-Encoding": "gzip, deflate, br",
    "DNT": "1",
    "Connection":"keep-alive",
    "Upgrade-Insecure-Requests": "1"
}
#
headers_2 = {
"Host":"music.163.com",
"User-Agent":"Mozilla/5.0 (X11; Ubuntu; Linux x86_64; rv:61.0) Gecko/20100101 Firefox/61.0",
"Accept":"text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8",
"Accept-Language":"zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
"Accept-Encoding":"gzip, deflate, br",
"Referer":"https://music.163.com/discover/artist/cat?id=2001&initial=70",
"Cookie":"_ntes_nnid=d89de8ba7e81b490541d634727f5f54f,1532954822591; _ntes_nuid=d89de8ba7e81b490541d634727f5f54f; __utma=94650624.461628771.1532954826.1533362508.1533393495.6; __utmz=94650624.1533362508.5.3.utmcsr=baidu|utmccn=(organic)|utmcmd=organic; WM_NI=r4U%2BceBcjaEyQ%2FtBVV6AZTuVYbbvvGkzelErXnCGlYg%2FKplyTLLetqVg93Jn%2Fqxboi9NIBhwqDvtGbkXpuVhfr4c%2FeRVfA7ZKdPyt09Uf1Mnzvblpd8gpCHDzqHGLMwPNlA%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea9f87ab69d8bb4ec5e89869c93f13c81efbeb3cb63f79b8da7c46af8a9ad97f22af0fea7c3b92ab2ec9bcce26f82bda682c87393f1bca3d55ef69f96b5f85e9bbeae97f54da9a6ab8dc87a9cb28da8ef53a5f18591ef7398948486f77b96b9f7d4c966edafb883ee63fb9287a3eb7db39cba95c66aa988c096d564a6aefc84ae6f928aaaa2b65289bca09af73cfb8baad2d066baaaae8df370fcb9c0a4cb50baaf88a8cf47b590828dc437e2a3; WM_TID=GWU%2BAkEfmzKgFbUKEXJL04qb9ulhu3bo; usertrack=ezq0pFtiZyBY/VaDL8YqAg==; Province=010; City=010; _ga=GA1.2.1858012805.1533175590; JSESSIONID-WYYY=ysQ9tPtS%5CTwqS35ahyopIlFyg1HebqbzGQoMxI%2BrTrW6PJraYynw0FdHb%5C%2FGS0u%5Cw8gw04OS6%2BCGdotNAOh57GaBk8YTIPrEhV4ZQ0NVQFuNRKHqps00FQzMXM0ptVevuhmpSBSkHkBjceh2Tnylr%5CqvIWO4FW7%5CysgZne4eR9NkeG9M%3A1533395292028; _iuqxldmzr_=32; __utmb=94650624.16.10.1533393495; __utmc=94650624",
"Connection":"keep-alive",
"Upgrade-Insecure-Requests":"1",
"Cache-Control":"max-age=0"
}

# "Cookie":"JSESSIONID-WYYY=oAkTXXbzyu%2F9G9HAuVpiHTxa%2BxDJMiG2VU5CnU3vCcGFNwfuVOYyK5MXBXPKREiw8Hy4WBxzA7p3sRrNsKuDC8Qy5IJYxkYTsKA%2FXANVJf2T%5C05Sjgz1tS00ABpolIJ0et%2BjC4AJOwvt1%5Cc9PShGfNCAvnSP7i%5CsEfvUIpmriDTRcRf5%3A1533392526074; _iuqxldmzr_=32; _ntes_nnid=05b00c1b3c2c5fc4f2c9d259e432dfa4,1533390726092; _ntes_nuid=05b00c1b3c2c5fc4f2c9d259e432dfa4; __utma=94650624.1551482594.1533390728.1533390728.1533390728.1; __utmb=94650624.17.10.1533390728; __utmc=94650624; __utmz=94650624.1533390728.1.1.utmcsr=(direct)|utmccn=(direct)|utmcmd=(none); WM_NI=SCno3iMUr%2BwhY3KBA%2BTwo1nuF3POEPEXLmlWiuWuDnPE3DZfCjhVrRX4ejw0%2Fj7MOOJK7wCUPhwoq1hkjJh0v3FHTftNvPApAyoSOZ%2FbACCQUy6DKzh1azSnZk3vPKWnVzc%3D; WM_NIKE=9ca17ae2e6ffcda170e2e6eea9d77cfbba8491e66b8986f8abd86892f09db3c646a3edff9bd442b69e8299b72af0fea7c3b92a919da290b2638f8bbeccf6649bed85a3c42198a9a1d2ed7f86eda0b0c85c8788848eef5dabab9996c766949bfda5d96e81b6a8b7f15a9cecab8bf63cedb6f9aece458a95f998c25f94b8b990f43bacb5a6abeb3cb6ed8aa9d76eb892bab1c47c83a7a1b4ce52edbe8fa4c25b97a7faa5ca72acefaf9bd2669ab5fd97d34195b29a9be237e2a3; WM_TID=XYoF9tZSzJZTpQPdCvFKVZOSBVvAQiW%2B",
url_hot = "https://music.163.com/discover/artist/cat?id=2001"
# 注意url中discover/#/artist部分要去掉＃
url_page_F = "https://music.163.com/discover/artist/cat?id=2001&initial=70"

# print(re.get(url=url_hot, headers=headers).text)
print(re.get(url=url_page_F, headers=headers).text)


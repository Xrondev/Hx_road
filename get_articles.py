'''

'''

import json
import threading
import requests
import random
import string

requests.packages.urllib3.disable_warnings()
base_url = "https://www.jumboxtech.com:8022/article/queryArticles"
header = {
    'Host': 'www.jumboxtech.com:8022',
    'Connection': 'keep-alive',
    # 'Content-Length': '39',
    'User-Agent': 'Mozilla/5.0 (Linux; Android 7.1.2; GM1900 Build/N2G47H; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/68.0.3440.70 Safari/537.36 MMWEBID/9558 MicroMessenger/8.0.2.1860(0x28000234) Process/appbrand0 WeChat/arm32 Weixin Android Tablet NetType/WIFI Language/zh_CN ABI/arm64 MiniProgramEnv/android',
    'charset': 'utf-8',
    'Accept-Encoding': 'gzip,compress,br,deflate',
    'content-type': 'application/x-www-form-urlencoded',
    'Referer': 'https://servicewechat.com/wxf7f31446cd68367a/5/page-frame.html',
}

page_num = 130


def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))


chars = string.ascii_uppercase + string.digits * 3
size = 32
exists_articles = set()
with open('article.txt', 'r', encoding='utf-8') as f:
    for line in f:
        exists_articles.add(line.replace('\n', '').split(',')[0])

with open('article.txt', 'a+', encoding='utf-8') as f:
    s = requests.session()
    s.keep_alive = False
    ex = False
    for i in range(1, page_num):
        if ex: break
        user_id = random_string_generator(size, chars)
        payload = f'page={i}&userId={user_id}&queryType=0&orderType=0&selectedTag='
        req = s.post(base_url, headers=header, data=payload, verify=False)
        ob = json.loads(req.content.decode(encoding='utf-8'))
        print(ob)
        articles = ob['data']['rows']  # 10 articles per page
        for article in articles:
            id = article['id']
            if id in exists_articles:
                ex = True
                break
            title = article['articleTitle']
            userId = article['userId']
            f.write(f'{id},{title},{userId}\n')

    # print(req.content.decode(encoding='utf-8'))

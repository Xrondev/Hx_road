'''

'''

import json
import threading
import requests
import random
import string

requests.packages.urllib3.disable_warnings()
base_url = "https://www.jumboxtech.com:8022/social/getMainComments"
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

with open('article.txt', 'r', encoding='utf-8') as f:
    user_set = set()
    s = requests.session()
    s.keep_alive = False
    for line in f:
        a_id, title, userId = line.strip().split(',')
        counter, page_num = 1, 1
        while counter <= page_num:
            payload = f'page={counter}&type=0&targetType=ARTICLE&targetId={a_id}&userId={userId}'
            # print(payload)
            req = s.post(base_url, headers=header, data=payload, verify=False)
            ob = json.loads(req.content.decode(encoding='utf-8'))
            # print(ob)
            page_num = ob['data']['total']
            counter += 1
            for row in ob['data']['rows']:
                user1 = row['fromUserId']
                user2 = row['toUserId']
                user_set.add(user1)
                user_set.add(user2)
    print(len(user_set))

ids = set()
with open('ids.txt', 'r', encoding='utf-8') as f:
    for line in f:
        ids.add(line.strip().split(',')[0])
    print(len(ids))


final = user_set | ids
print(len(final))
with open('final.txt', 'w', encoding='utf-8') as f:
    for i in final:
        f.write(f'{i}\n')


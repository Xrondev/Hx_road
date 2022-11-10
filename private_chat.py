'''
Private chat used websockets
'''

import asyncio
import random
import time

import websockets
import json
import threading
import requests

user_id = 'XXX'

# 接口地址，接口地址表单形式，包含了token
url = 'wss://www.jumboxtech.com:8014/ws'


async def hello():
    data2 = json.dumps({"action": 2,
                        "data": {"senderId": "E34BB82134BA736CFE92B9E297EC5565",
                                 "receiverId": "3590227AC3624024CD73C4CE8D3BD02A",
                                 "msg": "Hello", "msgId": None, "createDate": int(time.time() * 1000 + 50)},
                        "extend": "E34BB82134BA736CFE92B9E297EC5565"})

    data1 = json.dumps({"action": 1, "data": None, "extend": "E34BB82134BA736CFE92B9E297EC5565"})
    data4 = json.dumps({"action": 4, "data": None, "extend": None})

    async with websockets.connect(url) as websocket:

        # 发送数据
        await websocket.send(data1)
        print(f"> {data1}")

        await websocket.send(data2)
        print(f"> {data2}")
        res = await websocket.recv()
        print(f"< {res}")
        # time.sleep(1.5)
        # await websocket.send(data4)
        # print(f"> {data4}")
        # time.sleep(1)

        # 接收数据
        # while True:
        #     greeting = await websocket.recv()
        #     print(f"< {greeting}")

            # if greeting is not None:
            #     ob = json.loads(greeting)
            #     id = ob['data']['msgId']
            #     data3 = json.dumps({"action": 3, "data": None, "extend": id})
            #     time.sleep(1)
            #     await websocket.send(data3)
            #     time.sleep(1)
            #     print(f"> {data3}")
            #     await websocket.send(data4)
            #     while True:
            #         greeting = await websocket.recv()
            #         print(f"< {greeting}")
            #         break
            #     break

        # # 接收数据
        # while True:
        #     data = await websocket.recv()
        #     print(data)

asyncio.get_event_loop().run_until_complete(hello())
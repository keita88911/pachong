# !usr/bin/python
# -*- coding: utf-8 -*-
'''
飘花网在线电影下载1
进入网页查看最大TS包文件名，填入for.max
完成后进入shell输入copy/b  E:\temps\*.ts  E:\temps\new.ts 合并文件
http://www.piaohua.pro/
'''
import requests
import json
import sys
default_encoding = 'utf-8'
if sys.getdefaultencoding() != default_encoding:
    reload(sys)
    sys.setdefaultencoding(default_encoding)
class BuChongXinxi():
    @classmethod
    def BuChongxinxi(self):
        headers = {'Content-Type': "video/mp2t", }
        '''获取最大ts文件包'''
        for i in range(100, 1774):
            url1 = []
            if 0 < i < 10:
                print("000%d" % i)
                i=("000%d" % i)
                url = "http://bilibili.com-l-bilibili.com/20190223/8039_6a310f25/1000k/hls/19d27272ee700" + str(i) + ".ts"
                url1.append(url)
            elif 10 <= i < 100:
                print(type(i))
                print("00%d" % i)
                i = ("00%d" % i)
                url = "http://bilibili.com-l-bilibili.com/20190223/8039_6a310f25/1000k/hls/19d27272ee700" + str(i) + ".ts"
                url1.append(url)
            elif 100 <= i < 1000:
                print(type(i))
                print("0%d" % i)
                i = ("0%d" % i)
                url = "http://bilibili.com-l-bilibili.com/20190223/8039_6a310f25/1000k/hls/19d27272ee700" + str(i) + ".ts"

                url1.append(url)
            elif 1000 <= i < 10000:
                print("%d" % i)
                i = ("%d" % i)
                url = "http://bilibili.com-l-bilibili.com/20190223/8039_6a310f25/1000k/hls/19d27272ee700" + str(i) + ".ts"
                url1.append(url)
            # print(url1[0])
            '''保存ts文件'''
            r = requests.get(url1[0], stream=True)
            f = open("ts/"+str(i)+".ts", "wb")
            for chunk in r.iter_content(chunk_size=512):
                if chunk:
                    f.write(chunk)
a=BuChongXinxi.BuChongxinxi()
# for  i  in range(0,1774):
#     if 0<i<10:
#         print("000%d"%i)
#     elif 10<=i<100:
#         print("00%d" % i)
#     elif 100 <= i < 1000:
#         print("0%d" % i)
#     elif 1000 <= i < 10000:
#         print("%d" % i)

#!usr/bin/python
# coding=utf-8
import gevent
import requests
import time
from threading import Thread
from lxml import etree
import requests
from gevent import monkey

from multiprocessing import Process, Queue
import sys

reload(sys)
sys.setdefaultencoding('utf8')
import gevent

# socket发送请求以后就会进入等待状态，gevent更改了这个机制
# socket.setblocking(False)  -->发送请求后就不会等待服务器响应
monkey.patch_all()  # 找到内置的socket并更改为gevent自己的东西


class getimg(Thread):
    def __init__(self, url, q, title):
        # 重写写父类的__init__方法
        super(getimg, self).__init__()
        self.url = url
        self.q = q
        self.title = title
        self.headers = {'Content-Type': 'image/jpeg'}

    # @classmethod
    # def geturl(self):
    #     test = []
    #     for n in range(1,3):
    #         for t in range(0, 2):
    #             for i in range(0,2):
    #                 for m in range(0, 3):
    #                     # http://img.jojoft.com/532/JOJO_002-003.jpg
    #                     m1=m+1
    #
    #                     url1="http://img.jojoft.com/"+str(n)+"/JOJO_"+str(t)+str(i)+str(m)+".jpg"
    #                     test.append(url1)
    #                     url2="http://img.jojoft.com/"+str(n)+"/JOJO_"+str(t)+str(i)+str(m)+"-"+str(t)+str(i)+str(m1)+".jpg"
    #                     test.append(url2)
    #                     url3="http://img.jojoft.com/"+str(n)+"/JOJO_"+str(t)+str(i)+str(m)+".png"
    #                     test.append(url3)
    #                     url4="http://img.jojoft.com/"+str(n)+"/JOJO_"+str(t)+str(i)+str(m)+"-"+str(t)+str(i)+str(m1)+".png"
    #                     test.append(url4)
    # print(test)
    # return test
    def run(self):
        # type: () -> object

        self.page()

    def page(self):
        ts1 = self.pachong1(self.url)
        # print(type(self.url))
        # ts1=getimg.pachong1

        if ts1.status_code == 200:
            a = self.title
            print(a)
            with open(a.decode(), 'wb') as fd:
                for chunk in ts1:
                    fd.write(chunk)
        else:
            print("error")

    def pachong1(self, url):
        # print(url)
        s = requests.session()
        s.keep_alive = False
        # 增加重试连接次数
        s.adapters.DEFAULT_RETRIES = 511

        ts = requests.get(url=url, headers=self.headers)

        return ts

        # if ts.status_code == 200:
        #     a =url+ ".jpg"
        #     # print(a)
        #     with open(a.decode(), 'wb') as fd:
        #         for chunk in ts:
        #             fd.write(chunk)
        # ts2=requests.get(url2,headers=header)
        # ts3=requests.get(url3,headers=header)
        # ts4=requests.get(url4,headers=header)
        #
        # print(ts.status_code)
        # # print ts.iter_content(128)
        # # for chunk in ts.iter_content(128):
        # #     getimg.wirt(chunk)
        # if  ts.status_code==200:
        #     a="第"+str(n)+"话"+str(t)+str(i)+str(m)+"页"+".jpg"
        #     print(a)
        #     with open(a.decode(), 'wb') as fd:
        #         for chunk in ts:
        #             fd.write(chunk)
        # elif ts2.status_code==200:
        #     a="第"+str(n)+"话"+str(t)+str(i)+str(m)+"-"+str(t)+str(i)+str(m1)+"页"+".jpg"
        #     print(a)
        #     with open(a.decode(), 'wb') as fd:
        #         for chunk in ts:
        #             fd.write(chunk)
        # elif ts3.status_code==200:
        #     a="第"+str(n)+"话"+str(t)+str(i)+str(m)+"页"+".png"
        #     print(a)
        #     with open(a.decode(), 'wb') as fd:
        #         for chunk in ts:
        #             fd.write(chunk)
        # elif ts4.status_code==200:
        #     a = "第" + str(n) + "话" + str(t) + str(i) + str(m) + "-" + str(t) + str(i) + str(
        #         m1) + "页" + ".png"
        #     print(a)
        #     with open(a.decode(), 'wb') as fd:
        #         for chunk in ts:
        #             fd.write(chunk)

    @staticmethod
    def wirt(t):
        with open('demo.jpg', 'wb') as fd:  # 若是'wb'就表示写二进制文件
            fd.write(t)
            fd.close()
        # with open('demo.jpg', 'wb') as fd:
        #     for chunk in ts:
        #         fd.write(chunk)


# a=getimg()
# a.geturl()
def main():
    url_list = []
    titile = []
    for n in range(0, 10):
        for t in range(0, 2):
            for i in range(0, 2):
                for m in range(0, 10):
                    # http://img.jojoft.com/532/JOJO_002-003.jpg
                    m1 = m + 1

                    url1 = "http://img.jojoft.com/" + str(n) + "/JOJO_" + str(t) + str(i) + str(m) + ".jpg"
                    titile1 = "第" + str(n) + "话" + str(t) + str(i) + str(m) + "页" + ".jpg"
                    titile.append(titile1)
                    url_list.append(url1)
                    url2 = "http://img.jojoft.com/" + str(n) + "/JOJO_" + str(t) + str(i) + str(m) + "-" + str(t) + str(
                        i) + str(m1) + ".jpg"
                    titile2 = "第" + str(n) + "话" + str(t) + str(i) + str(m) + "-" + str(t) + str(i) + str(
                        m1) + "页" + ".jpg"
                    titile.append(titile2)
                    url_list.append(url2)
                    url3 = "http://img.jojoft.com/" + str(n) + "/JOJO_" + str(t) + str(i) + str(m) + ".png"
                    titile3 = "第" + str(n) + "话" + str(t) + str(i) + str(m) + "页" + ".png"
                    titile.append(titile3)
                    url_list.append(url3)
                    url4 = "http://img.jojoft.com/" + str(n) + "/JOJO_" + str(t) + str(i) + str(m) + "-" + str(t) + str(
                        i) + str(m1) + ".png"
                    titile4 = "第" + str(n) + "话" + str(t) + str(i) + str(m) + "-" + str(t) + str(i) + str(
                        m1) + "页" + ".png"
                    titile.append(titile4)
                    url_list.append(url4)
    # 创建一个队列用来保存进程获取到的数据
    # print(url_list)
    q = Queue()
    # base_url = 'https://movie.douban.com/top250?start='
    # 构造所有ｕｒｌ

    # 保存进程
    Thread_list = []
    # 创建并启动线程
    for url2, titile1 in zip(url_list, titile):
        p = getimg(url2, q, titile1)
        p.start()
        Thread_list.append(p)

    # 让主线程等待子线程执行完成
    for i in Thread_list:
        i.join()

    # 让主线程等待子线程执行完成
    for i in Thread_list:
        i.join()

    while not q.empty():
        print q.get()


if __name__ == "__main__":
    start = time.time()
    main()
    print '[info]耗时：%s' % (time.time() - start)

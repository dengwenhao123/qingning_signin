import requests
import time
import json
# from datetime import datetime
# from bs4 import BeautifulSoup
# import re
# import os


def login(headers,data_person):
    login_url = "https://wxyqfk.zhxy.net/?yxdm=10623#/login"
    # 登陆
    s=requests.Session()
    s.post(login_url, data=data_person, headers=headers)
    # post登陆页面
    s.post("https://yqfkapi.zhxy.net/api/User/CheckUser")
    print("登陆成功")
    return s


def tiwen_daka(s,headers):
    try:
        for i in range(2):
            ti_wen_url = "https://wxyqfk.zhxy.net/?yxdm=10623#/temperatureReport"
            # 时间
            # ti = str(time.strftime("%Y-%m-%d %H:%M:%S", time.localtime()))  # 获取时间，每次post都要更新时间，格式化成20xx-03-20 11:45:39形式
            ti_for_title = str(time.strftime("%Y-%m-%d", time.localtime()))  # 获取时间，这个时间是放在SBRQ里面
            # 体温打卡数据,更改ID和UID
            data_tiWen = {
                "ID": "9070711",
                "SBRQ": ti_for_title + " 00:00:00",
                "UID": "1464417",
                "UType": "1",
                "WSTJSJ": ti_for_title + " 15:01:01",
                "WSTW": "36.5",
                "YXDM": "10623",  # YXDM都一样
                "ZCTJSJ": ti_for_title + " 15:01:01",
                "ZCTW": "36.8",
                "ZWTJSJ": ti_for_title+ " 15:01:01",
                "ZWTW": "36.5"
        }
            # 体温页面
            tiwen_res = s.post(ti_wen_url, headers=headers)
            # post体温数据
            s.post("https://yqfkapi.zhxy.net/api/ClockIn/SaveTem", data=data_tiWen, headers=headers)
        print("打卡成功")
    except:
        print("打卡失败")


if __name__ == '__main__':
    # headers
    with open("header.json","r+",encoding="utf-8") as f:
        h = f.read()
        headers = json.loads(h)
    # 个人数据
    with open("data_person.json","r+",encoding="utf-8") as f:
        data_person = f.read()
        data_person = json.loads(data_person)  # 个人信息的json数据

    # 1.登陆并填体温
    s = login(headers=headers,data_person=data_person)
    tiwen_daka(s,headers=headers)
url="https://sc.ftqq.com/SCU163238T43d504895170174cca0372e790709d93603f71ef8edf5.send?text=今日邓文豪体温已经上报成功！"
requests.post(url)





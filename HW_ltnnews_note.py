# -*- coding: utf-8 -*-
"""
Created on Mon Nov  7 13:04:53 2022

@author: USER
"""


##設定與連線
import requests
from bs4 import BeautifulSoup

myHead={"user-agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/107.0.0.0 Safari/537.36"}
urL="https://news.ltn.com.tw/list/breakingnews"

rQ=requests.get(urL,headers=myHead).text
souP=BeautifulSoup(rQ,"lxml")


#1
#定位
soupS=souP.find("ul","list")


for mySoup in soupS.find_all("li"):
    try:
    
        print(mySoup.find("span","time").text.strip())
        #print(mySoup.find("a","tit").text.strip())
        print(mySoup.h3.text.strip())
        print(mySoup.a["href"].strip()) ###
        print("-"*30)
    except:
        continue
    
    
    ###strip() 去除空白
    ##try /except / 避免中間有廣告造成中斷後無法抓到資料
    


# # 2
# #定位
# soupS=souP.find("div","whitecon boxTitle")

# #print(soupS)
# #找尋所需要的標籤
# for mySoup in soupS.find_all("li"):
#     # print(mySoup.text)
#     for mySoup in mySoup.find_all("a"):
#         print(mySoup.text.strip())   ##印出標題
#         print(mySoup["href"].strip())   ###印出屬性
#         print("-"*30)
#         # print(mySoup["title"])
 
  
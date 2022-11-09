# -*- coding: utf-8 -*-
"""


@author: USER
"""


##設定與連線
import requests
from bs4 import BeautifulSoup

myHead=
urL="https://news.ltn.com.tw/list/breakingnews"

rQ=requests.get(urL,headers=myHead).text
souP=BeautifulSoup(rQ,"lxml")



#定位
soupS=souP.find("ul","list")


for mySoup in soupS.find_all("li"):
    try:
    
        print(mySoup.find("span","time").text.strip())
        #print(mySoup.find("a","tit").text.strip())
        print(mySoup.h3.text.strip())
        print(mySoup.a["href"].strip()) 
        print("-"*30)
    except:
        continue
    
 
    

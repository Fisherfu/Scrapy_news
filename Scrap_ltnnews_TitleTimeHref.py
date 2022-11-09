
##自由時報政治版轉csv

import requests,csv,os
from bs4 import BeautifulSoup

os.chdir("")
myHead={""}
urL="https://news.ltn.com.tw/list/breakingnews/politics"

rQ=requests.get(urL,headers=myHead).text
souP=BeautifulSoup(rQ,"lxml")


#1
#定位
soupS=souP.find("ul","list")

#2. 串列
newS=[]
cc=1

#3. 取值
for mySoup in soupS.find_all("li"):
    try:
        
        timE=mySoup.find("span","time").text.strip()
        titlE=mySoup.h3.text.strip()
        urL=mySoup.a["href"].strip()
        print(timE)
        # list_BigSoup.append(mySoup.find("span","time").text.strip())
                #print(mySoup.find("a","tit").text.strip())
        print(titlE)
        # list_BigSoup.append(mySoup.h3.text.strip())
        print(urL) ###
        # list_BigSoup.append(mySoup.a["href"].strip())
        print(cc,"-"*30)
        cc=cc+1
        neW=[timE,titlE,urL]
        newS.append(neW)
    
    except:
        continue
    
#3.存取 csv 檔

csvFile2=open("ltnnews_report.csv","w",newline="",encoding="utf-8-sig")

writeR=csv.writer(csvFile2)
writeR.writerow(["時間","標題","連結"])

for rowL in newS:
    writeR.writerow([rowL[0],rowL[1],rowL[2]])

csvFile2.close()
    

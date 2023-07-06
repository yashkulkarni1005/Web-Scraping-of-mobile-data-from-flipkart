import pandas as pd
import requests
from bs4 import BeautifulSoup
product_name=[]
prices=[]
description=[]
reviews=[]


for i in range(2,10):
        
    url="https://www.flipkart.com/search?q=mobile+&otracker=search&otracker1=search&marketplace=FLIPKART&as-show=on&as=off&page="+str(i)

    r=requests.get(url)

    soup=BeautifulSoup(r.text,"lxml")

    box=soup.find("div",class_="_1YokD2 _3Mn1Gg")



    names=box.find_all("div",class_="_4rR01T")
    for i in names:
        product_name.append(i.text)

    # print(product_name)




    prices_data=box.find_all("div",class_="_30jeq3 _1_WHN1")
    for i in prices_data:
        prices.append(i.text)
    # print(product_name[10],prices[10])





    desc=box.find_all("ul",class_="_1xgFaf")

    for i in desc:
        description.append(i.text)
    # print(description)






    rev=box.find_all("div",class_="_3LWZlK")

    for i in rev:
        reviews.append(i.text)

    # print(reviews)

df=pd.DataFrame({"Product Name":product_name,"Prices":prices,"Description":description,"Reviews":reviews})

df.to_csv("flipkart_mobile_data.csv")





























    # np=soup.find("a",class_="_1LKTO3").get("href")
    # cnp="https://www.flipkart.com"+np
    # print(np)

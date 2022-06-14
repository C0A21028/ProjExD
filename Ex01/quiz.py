import random
import datetime
import re


def shutudai():
    qs = [["サザエの旦那の名前は？",["マスオ","ますお"]],
    ["カツオの妹の名前は？",["ワカメ","わかめ"]],
    ["タラオはカツオから見てどんな関係？",["甥","おい","甥っ子","おいっこ"]]]

    x1 = random.randint(0,len(qs)-1)
    qX = qs[x1][0]
    print("問題：")
    print(qX)
    return qs[x1]
    

def kaito():
    ans = input("回答を入力/")
    for i in q_and_a[1]:
        if i == ans:
            print("正解！")
            return
        
    print("出直してこい")

q_and_a = shutudai()
timeS = datetime.datetime.now()
kaito()
timeE = datetime.datetime.now()

print((timeE - timeS).seconds)

#完成しました



    
    
    








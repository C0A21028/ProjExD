import imp
import random
from datetime import datetime

Num_TarChar = int(input("対象の個数："))
Num_MisChar = int(input("欠損の個数："))

Num_Diff = Num_TarChar - Num_MisChar
MaxReTime = 5

def exal():
    count = 0
    alphabetList = ["A","B","C","D","E","F","G","H","I","J","K","L","M",
                "N","O","P","Q","R","S","T","U","V","W","X","Y","Z"]

    exalList = random.sample(alphabetList,Num_TarChar) #抽出した文字のリスト
    misList = random.sample(exalList,Num_Diff) #欠損させた文字のリスト

    exal_num = Num_MisChar
    times1 = 1

    print(f"対象文字：\n{exalList}")
    print(f"表示文字：\n{misList}")

    Num_ans = int(input("欠損文字はいくつあるでしょうか?："))
    if int(Num_ans) == int(Num_MisChar):
        print("正解です。それでは、具体的に欠損文字を１つずつ入力してください")
        while exal_num > 0:
            ans_alph = input(f"{times1}つ目の文字を入力してください：")
            times1 += 1

            if ans_alph in exalList:
                if ans_alph in misList:
                    continue
                else:
                    count += 1

            exal_num -= 1

        if count == Num_MisChar:
            print("正解です。おめでとうございます")

        else:
            print("不正解だよばかやろー")        


    else:
        print("不正解です。再チャレンジをしてください\n--------------------------------")
        

exal()

#たぶん完成しました


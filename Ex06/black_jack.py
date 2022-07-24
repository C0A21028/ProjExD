from os import scandir
import random
import tkinter.messagebox as tkm
import pygame as pg
import sys
import tkinter as tk

deck = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13] * 4
gara = ["CL","HT","SP","DI"]
jisyo = {"CL":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        "HT":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        "SP":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13],
        "DI":[1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]}

class Screen:
    def __init__(self,title,wh,image):
        pg.display.set_caption(title)
        self.sfc=pg.display.set_mode(wh)
        self.rct=self.sfc.get_rect()
        self.bgi_sfc=pg.image.load(image)
        self.bgi_rct=self.bgi_sfc.get_rect()
    def blit(self):
        self.sfc.blit(self.bgi_sfc,self.bgi_rct)

class huda:
    def __init__(self,hand:list,label:list,hito):
        self.sfc1=pg.image.load(f"./ex06/トランプ/{label[0]}/{hand[0]}_{label[0]}.png")
        self.sfc1=pg.transform.rotozoom(self.sfc1, 0, 0.15)
        self.rct1=self.sfc1.get_rect()
        self.y=0
        l=0
        if hito=='P':
            self.y=700
        else:
            self.y=100
            l=1
        self.rct1.center=(725,self.y)
        if l==1:
            self.sfc2=pg.image.load(f"./ex06/トランプ/card_back.png")
            self.sfc2=pg.transform.rotozoom(self.sfc2, 0, 0.27)
            
        else:
            self.sfc2=pg.image.load(f"./ex06/トランプ/{label[1]}/{hand[1]}_{label[1]}.png")
            self.sfc2=pg.transform.rotozoom(self.sfc2, 0, 0.15)
        self.rct2=self.sfc2.get_rect()
        self.rct2.center=(875,self.y)
    def blit(self,scr:Screen):
        scr.sfc.blit(scr.sfc,scr.rct)
    def update(self,scr:Screen):
        scr.sfc.blit(self.sfc1,self.rct1)
        scr.sfc.blit(self.sfc2,self.rct2)
        self.blit(scr)


class tuika:
    def __init__(self,hand,label,x,count):
        self.sfc=pg.image.load(f"./ex06/トランプ/{label[0]}/{hand[0]}_{label[0]}.png")
        self.sfc=pg.transform.rotozoom(self.sfc, 0, 0.15)
        self.rct=self.sfc.get_rect()
        if count==1:
            mod=x+160
        else:
            mod=x+75
        self.rct.center=(mod,700)
    def blit(self,scr:Screen):
        scr.sfc.blit(scr.sfc,scr.rct)
    def update(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)
        self.blit(scr)

class ura:
    def __init__(self,image):
        self.sfc=pg.image.load(image)
        self.sfc=pg.transform.rotozoom(self.sfc, 0, 0.27)
        self.rct=self.sfc.get_rect()
        self.rct.center=(1400,450)
    def blit(self,scr:Screen):
        scr.sfc.blit(self.sfc,self.rct)

def main():
    total1=0
    total2=0
    clock=pg.time.Clock()
    scr=Screen("black Jack",(1600,900),"./ex06/トランプ/CC.jpg!d")
    dealer_kigo,dealer_hand = deal()
    player_kigo,player_hand = deal()
    total1+=total(player_hand[0])+total(player_hand[1])
    total2+=total(dealer_hand[0])+total(dealer_hand[1])
    ur=ura("ex06/トランプ/card_back.png")
    print(player_kigo)
    kkt1=huda(player_hand,player_kigo,'P')
    kkt2=huda(dealer_hand,dealer_kigo,'D')
    count=0
    com=0
    m=0
    pk=0
    kkx=kkt1.rct2.centerx
    kkt=[]
    x1=kkt1.rct1.centerx
    while True:
        scr.blit()
        ur.blit(scr)
        for event in pg.event.get():
            if event.type==pg.QUIT:
                return
            if event.type==pg.KEYDOWN and event.key==pg.K_SPACE:
                m=1
            elif event.type==pg.KEYDOWN and event.key==pg.K_1:
                pk,ph=deal2()
                com+=1
                count=com
                total1+=total(ph[0])
                if count>=2:
                    count=2
        if m==1:
            kkt1.update(scr)
            kkt2.update(scr)
        if count>=1:
            kkt1.rct1.centerx-=10
            kkt1.rct2.centerx-=10
            if kkt1.rct1.centerx<=x1-75/2:
                kkt1.rct1.centerx=kkt1.rct1.centerx-75/2
                kkt1.rct2.centerx=kkt1.rct1.centerx+150
                kkt.append(tuika(ph,pk,kkx,count))
                for j in kkt:
                    kkx=j.rct.centerx
                    while True:
                        j.rct.centerx-=10
                        if j.rct.centerx<=kkx-75:
                            break
                x1=kkt1.rct1.centerx
                count=0
                if total1>21:
                    pk=1
        for i in kkt:
            i.update(scr)
        pg.display.update()
        clock.tick(1000)
        if pk==1:
            root = tk.Tk()
            root.withdraw()
            tkm.showinfo("game over","もう一度やりますか？")
            return


def deal():
    global gara,jisyo
    hand = []
    kis=[]
    for i in range(2):
        m=random.randint(0,3)
        ki=gara[m]
        ho=jisyo[ki]
        random.shuffle(ho)
        card = ho.pop()
        jisyo.update({ki:ho})
        kis.append(ki)
        hand.append(card)
    return kis,hand

def deal2():
    global gara,jisyo
    hand = []
    kis=[]
    m=random.randint(0,3)
    ki=gara[m]
    ho=jisyo[ki]
    random.shuffle(ho)
    card = ho.pop()
    jisyo.update({ki:ho})
    kis.append(ki)
    hand.append(card)
    return kis,hand

def total(hand):
    if hand >= 10:
        score = 10
    else:
        score=hand
    return score

def play_again():
    again = input("もう１度プレイしますか？ (Y/N): ")
    if again == "y" or again == "Y":
        # game()
        return
    else:
        print("お疲れ様でした！")
        exit()

def result(dealer_hand, player_hand):
    if total(player_hand) > total(dealer_hand):
        print(
            f"\nディーラーの合計は {total(dealer_hand)} あなたの合計は {total(player_hand)} です。\033[32mYOU WIN!\033[0m")
    elif total(dealer_hand) > total(player_hand):
        print(
            f"\nディーラーの合計は {total(dealer_hand)} あなたの合計は {total(player_hand)} です。\033[91mYOU LOSE...\033[0m")
"""
def game():
    dealer_hand = deal()
    player_hand = deal()
    print(f"ディーラーのカードは {dealer_hand[0]} です。")
    print(f"プレイヤーのカードは {player_hand} 合計が {total(player_hand)} です。")

    choice = 0

    while choice != quit:
        choice = input("ヒットしますか？ スタンドしますか？ (HIT/STAND): ").lower()
        if choice == "hit":
            hit(player_hand)
            print(
                f"\nあなたに {player_hand[-1]} が配られ、カードは {player_hand} 合計は {total(player_hand)} です。")
            if total(player_hand) > 21:
                print("あなたは 21 を超えてしまいました。\033[91mYOU LOSE...\033[0m")
                choice = quit

        elif choice == "stand":
            print(
                f"\nディーラーの２枚めのカードは {dealer_hand[1]} 合計は {total(dealer_hand)} です。")
            while total(dealer_hand) < 17:
                hit(dealer_hand)
                print(
                    f"ディーラーに {dealer_hand[-1]} が配られ、カードは {dealer_hand} 合計は {total(dealer_hand)} です。")
                if total(dealer_hand) > 21:
                    print("ディーラーは 21 を超えてしまいました。\033[32mYOU WIN!\033[0m")
                    choice = quit

            if total(dealer_hand) <= 21:
                result(dealer_hand, player_hand)
                choice = quit
"""

if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()

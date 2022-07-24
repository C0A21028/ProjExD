import tkinter.messagebox as tkm
import pygame as pg
import sys
import random
import tkinter as tk
class Screen:
    def __init__(self,title,wh,image):
        pg.display.set_caption(title)
        self.sfc=pg.display.set_mode(wh)
        self.rct=self.sfc.get_rect()
        self.bgi_sfc=pg.image.load(image)
        self.bgi_rct=self.bgi_sfc.get_rect()
    
    def blit(self):
        self.sfc.blit(self.bgi_sfc,self.bgi_rct)
class Bird:
    def __init__(self,image,size,xy):
        self.sfc=pg.image.load(image)
        self.sfc=pg.transform.rotozoom(self.sfc, 0, size)
        self.rct=self.sfc.get_rect()
        self.rct.center=xy
    def blit(self,scr:Screen):
        scr.sfc.blit(scr.sfc,scr.rct)
        #screen_sfc.blit(bgimg_sfc,bgimg_rct)
    def update(self,scr : Screen):
        move=[pg.K_UP,pg.K_DOWN,pg.K_LEFT,pg.K_RIGHT]
        l=10
        move2=[[-1*l,0],[l,0],[0,-1*l],[0,l]]
        key_states=pg.key.get_pressed()
        for a,m in enumerate(move):
            if key_states[m]:
                y,x=move2[a]
                self.rct.centery+=y 
                self.rct.centerx+=x
            if check_bound(self.rct,scr.rct)!=(1,1):
                for j,n in enumerate(move):
                    if key_states[n]:
                        y,x=move2[j]
                        self.rct.centery-=y 
                        self.rct.centerx-=x
        scr.sfc.blit(self.sfc,self.rct)
        self.blit(scr)
    def attack(self):
        return laser()
class bomb:
    def __init__(self,color,size,vxy,scr:Screen):
        self.sfc=pg.Surface((2*size,2*size)) #surfaceの空リストを作成
        self.sfc.set_colorkey((0,0,0))
        pg.draw.circle(self.sfc,color,(size,size),size) #rectの空リストを作成
        self.rct=self.sfc.get_rect()
        self.rct.centerx=random.randint(0,scr.rct.width)
        self.rct.centerx=random.randint(0,scr.rct.height)
        self.vx,self.vy = vxy    
    def blit(self,scr:Screen):
        scr.sfc.blit(scr.sfc,scr.rct)

    def update(self,scr:Screen):
        self.rct.move_ip(self.vx,self.vy)
        yoko,tate=check_bound(self.rct,scr.rct)
        self.vx*=yoko
        self.vy*=tate
        scr.sfc.blit(self.sfc,self.rct)

class laser:
    def __init__(self,image,chr:Bird,key):
        self.sfc=pg.image.load(image)
        self.sfc=pg.transform.rotozoom(self.sfc, 0, 0.1)
        self.rct=self.sfc.get_rect()
        if key==pg.K_2:
            self.rct.midleft=chr.rct.center
            self.key='right'
        if key==pg.K_1:
            self.rct.midright=chr.rct.center
            self.key='left'
    def blit(self,scr:Screen):
        scr.sfc.blit(scr.sfc,scr.rct)
    def update(self,scr:Screen):
        if self.key=='right':
            self.rct.centerx+=10
        else:
            self.rct.centerx-=10
        scr.sfc.blit(self.sfc,self.rct)
        self.blit(scr)
def main():
    clock=pg.time.Clock()
    #pg.display.set_caption("逃げろこうかとん")
    #screen_sfc=pg.display.set_mode((1600,900))
    #screen_rct=screen_sfc.get_rect()
    #bgimg_sfc=pg.image.load("./ex04/fig/pg_bg.jpg")
    #bgimg_rct=bgimg_sfc.get_rect()
    #screen_sfc.blit(bgimg_sfc,bgimg_rct)
    #pg.display.update()
    #clock.tick(0.5)
    scr=Screen("逃げろ！こうかとん",(1600,900),"./ex05/fig/pg_bg.jpg")
    #kkimg_sfc=pg.image.load("./ex04/fig/3.png")
    #kkimg_sfc=pg.transform.rotozoom(kkimg_sfc, 0, 2.0)
    #kkimg_rct=kkimg_sfc.get_rect()
    #kkimg_rct.center=900,400
    kkt=Bird("./ex05/fig/6.png",2.0,(900,400))
    #練習5
    #数を増やす
    bmimg_sfc=[] #surfaceの空リストを作成
    color=[[255,0,0],[0,255,0],[0,0,255],[0,255,255],[255,255,0],[255,0,255]] #色の設定
    for i in range(6):
    #    bmimg_sfc.append(pg.Surface((20,20)))   #Surfaceリストに追加
    #    pg.draw.circle(bmimg_sfc[i],(color[i][0],color[i][1],color[i][2]),(10,10),10) #colorから色を取得
    #    bmimg_rct.append(bmimg_sfc[i].get_rect())   #Rectリストに追加
    #    bmimg_rct[i].centerx=random.randint(0,screen_rct.width)
    #    bmimg_rct[i].centery=random.randint(0,screen_rct.height)
    #    vx.append(1) #vxリストに追加
    #    vy.append(1) #vyリストに追加
    #count=[0,0,0,0,0,0]#countリストを作成。中身は6個で全て0
    #bom=random.randint(0,5)#爆弾を設定
    #count[bom]=1#爆弾のcountを1に
    #bmimg_sfc[bom]=pg.image.load("./ex04/fig/bomb.png")#爆弾の画像を描画
    #bmimg_sfc[bom]=pg.transform.rotozoom(bmimg_sfc[bom], 0, 0.05)#画像の大きさを調整
    #bmimg_rct[bom]=bmimg_sfc[i].get_rect()#Rectリストを更新
    #while True:
        #screen_sfc.blit(bgimg_sfc,bgimg_rct)
    #   scr.blit()
    #    for event in pg.event.get():
    #        if event.type==pg.QUIT:
    #            return
        bkd=bomb(color[i],10,(+3,+3),scr)
        bmimg_sfc.append(bkd)
    beams=[]
    beam=None
    while True:
        scr.blit()
        #練習4
        #move=[pg.K_UP,pg.K_DOWN,pg.K_LEFT,pg.K_RIGHT]
        #move2=[[-2,0],[2,0],[0,-2],[0,2]]
        #key_states=pg.key.get_pressed()
        #for a,m in enumerate(move):
        #    if key_states[m]==True:
        #        y,x=move2[a]
        #        kkimg_rct.centery+=y 
        #        kkimg_rct.centerx+=x
        #    if check_bound(kkimg_rct,screen_rct)!=(1,1):
        #        for j,n in enumerate(move):
        #            if key_states[n]==True:
        #                y,x=move2[j]
        #                kkimg_rct.centery-=y 
        #                kkimg_rct.centerx-=x
        for event in pg.event.get():
            if event.type==pg.QUIT:
                return
            if event.type==pg.KEYDOWN and event.key==pg.K_1:
                beam=laser("./ex05/fig/beam2.png",kkt,event.key)
                beams.append(beam)
            if event.type==pg.KEYDOWN and event.key==pg.K_2:
                beam=laser("./ex05/fig/beam.png",kkt,event.key)
                beams.append(beam)
            if event.type==pg.KEYDOWN and event.key==pg.K_RIGHT:
                kx,ky=kkt.rct.center
                kkt=Bird("./ex05/fig/6_2.png",2.0,(kx,ky))
            if event.type==pg.KEYDOWN and event.key==pg.K_LEFT:
                kx,ky=kkt.rct.center
                kkt=Bird("./ex05/fig/6.png",2.0,(kx,ky))
                
        kkt.update(scr)
        if beam!=None:
            for i in beams:
                i.update(scr)
            
        #追加機能
        #screen_sfc.blit(kkimg_sfc,kkimg_rct)
        #for i in range(6):
        #    bmimg_rct[i].move_ip(vx[i],vy[i])
        #    screen_sfc.blit(bmimg_sfc[i],bmimg_rct[i])
        #    yoko,tate=check_bound(bmimg_rct[i],screen_rct)
        #    vx[i]*=yoko
        #    vy[i]*=tate
        #    if kkimg_rct.colliderect(bmimg_rct[i]):#接触したとき
        #    if kkt.rct.colliderect("爆弾インスタンスのrct"):
        #        bmimg_sfc[i].set_colorkey((color[i][0],color[i][1],color[i][2]))#中身の色を消す
        #        bmimg_rct.append(bmimg_sfc[i].get_rect())#bmimg_rctを更新
        #        count[i]=1#countのi番目を1にする
        #        if kkimg_rct.colliderect(bmimg_rct[bom]):#爆弾にあたったとき
        #            root = tk.Tk()
        #            root.withdraw()
        #            tkm.showinfo("ねえ今どんな気持ち？","Game Over")#コメントを表示
        #            return
        #        if (count[0]==1  and count[1]==1 and count[2]==1 and count[3]==1
        #            and count[4]==1 and count[5]==1):#爆弾以外のものをすべて取ったとき
        #            root = tk.Tk()
        #            root.withdraw()
        #            pg.display.update()
        #            tkm.showinfo("なかなかやるじゃん！","Game Clear")

        for j in bmimg_sfc:
            j.update(scr)
            if kkt.rct.colliderect(j.rct):
                root = tk.Tk()
                root.withdraw()
                tkm.showinfo("ドンマイ","ゲームオーバー")
                return

            for k in beams:
                if k!=None and k.rct.colliderect(j.rct):
                    beams.remove(k)
                    bmimg_sfc.remove(j)

        if len(beams)>=10:
            beams.pop(0)
        if len(bmimg_sfc)<=0:
            root = tk.Tk()
            root.withdraw()
            tkm.showinfo("おめでとう","ゲームクリア")
            return
        pg.display.update()
        clock.tick(1000)

def check_bound(rct,scr_rct):
    """
    [1]rct:こうかとん　or 爆弾のRect
    [2]src_rct:スクリーンのRect
    """
    yoko,tate=1,1
    if rct.left<scr_rct.left or rct.right>scr_rct.right:
        yoko=-1
    if rct.top<scr_rct.top or rct.bottom>scr_rct.bottom:
        tate=-1
    return yoko,tate
if __name__=="__main__":
    pg.init()
    main()
    pg.quit()
    sys.exit()





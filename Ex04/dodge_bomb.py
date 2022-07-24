import tkinter.messagebox as tkm
import pygame as pg
import sys
import random

def main():
    clock=pg.time.Clock()
    kkimg_rct=kkimg_sfc.get_rect()
    kkimg_rct.center=900,400

    bmimg_sfc=[]
    bmimg_rct=[]
    vx=[]
    vy=[]
    color=[[255,0,0],[0,255,0],[0,0,255],[0,255,255],[255,255,0],[255,0,255]]
    for i in range(6):
        bmimg_sfc.append(pg.Surface((20,20)))#Surface
        pg.draw.circle(bmimg_sfc[i],(color[i][0],color[i][1],color[i][2]),(10,10),10)
        bmimg_rct.append(bmimg_sfc[i].get_rect())#Rect
        bmimg_rct[i].centerx=random.randint(0,screen_rct.width)
        bmimg_rct[i].centery=random.randint(0,screen_rct.height)
        vx.append(1)
        vy.append(1)
    count=[0,0,0,0,0,0]
    bom=random.randint(0,5)
    count[bom]=1
    bmimg_sfc[bom]=pg.image.load("./ex04/fig/bomb.png")
    bmimg_sfc[bom]=pg.transform.rotozoom(bmimg_sfc[bom], 0, 0.05)
    bmimg_rct[bom]=bmimg_sfc[i].get_rect()

    while True:
        screen_sfc.blit(bgimg_sfc,bgimg_rct)

        for event in pg.event.get():
            if event.type==pg.QUIT:
                return
        #練習4
        move=[pg.K_UP,pg.K_DOWN,pg.K_LEFT,pg.K_RIGHT]
        move2=[[-2,0],[2,0],[0,-2],[0,2]]
        key_states=pg.key.get_pressed()

        for a,m in enumerate(move):
            if key_states[m]==True:
                y,x=move2[a]
                kkimg_rct.centery+=y 
                kkimg_rct.centerx+=x

            if check_bound(kkimg_rct,screen_rct)!=(1,1):
                for j,n in enumerate(move):
                    if key_states[n]==True:
                        y,x=move2[j]
                        kkimg_rct.centery-=y 
                        kkimg_rct.centerx-=x

        screen_sfc.blit(kkimg_sfc,kkimg_rct)
        for i in range(6):
            bmimg_rct[i].move_ip(vx[i],vy[i])
            screen_sfc.blit(bmimg_sfc[i],bmimg_rct[i])
            yoko,tate=check_bound(bmimg_rct[i],screen_rct)
            vx[i]*=yoko
            vy[i]*=tate
            if kkimg_rct.colliderect(bmimg_rct[i]):
                bmimg_sfc[i].set_colorkey((color[i][0],color[i][1],color[i][2]))
                bmimg_rct.append(bmimg_sfc[i].get_rect())
                count[i]=1
                if kkimg_rct.colliderect(bmimg_rct[bom]):
                    tkm.showinfo("警告","Game Over")
                    return
                if (count[0]==1  and count[1]==1 and count[2]==1 and count[3]==1
                    and count[4]==1 and count[5]==1):
                    tkm.showinfo("警告","Game Clear")
                    return
        pg.display.update()
        clock.tick(1000)

def check_bound(rct,scr_rct):
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

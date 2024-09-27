from importlib.resources import path
from tkinter.tix import Balloon
import pygame as pg
import os
import random
from pygame.sprite import Sprite
from pygame.sprite import Group
#全域變數
clock=pg.time.Clock()
speed=[random.randint(-5,5),5]
deadline=710
id=None
life=10
score=0

pg.init()

pg.display.set_caption('接球遊戲')

os.environ['SDL_VIDEO_WINDOW_POS']="%d,%d"%(0,32)
width,height=1280,720
screen=pg.display.set_mode((width,height))
path1=os.path.abspath('.')
ch=path1+'\\程式設計\\picture\\'
background_jpg=pg.image.load(ch+'background2.jpg')
pad=pg.image.load(ch+"pad.png").convert_alpha()
ball=pg.image.load(ch+"ball.png").convert_alpha()
bombbig=pg.image.load(ch+"ssrb.png").convert_alpha()
bomb2big=pg.image.load(ch+"bomb2.png").convert_alpha()
pausebtn=pg.image.load(ch+"pause.png").convert_alpha()
startbtn=pg.image.load(ch+"START2.png").convert_alpha()
bomboldbig=pg.image.load(ch+"bombold.png").convert_alpha()
heal=pg.transform.scale(pg.image.load(ch+"heal.png").convert_alpha(),(70,80))
background=pg.transform.scale(background_jpg,(width,height))
bomb=pg.transform.scale(bombbig,(70,80))
bomb2=pg.transform.scale(bomb2big,(70,80))
bombold=pg.transform.scale(bomboldbig,(90,100))
bombold2=pg.transform.scale(bomboldbig,(90,100))


back_rect=background.get_rect()

pad_rect=pad.get_rect()
ball_rect=ball.get_rect()
pad_rect.center=width/2,600
ball_rect.center=200+(1%3)*400,50+(1//3)*150

bomb_rect=bomb.get_rect()
bomb_rect.bottomleft=random.randint(0,width-bomb_rect.width),0
bomb2_rect=bomb2.get_rect()
bomb2_rect.bottomleft=random.randint(0,width-bomb2_rect.width),0
heal_rect=heal.get_rect()
heal_rect.bottomleft=random.randint(0,width-heal_rect.width),0

bombold_rect=bombold.get_rect()
bombold2_rect=bombold.get_rect()



pause_rect=pausebtn.get_rect()
pause_rect.topright=width,0

start_rect=startbtn.get_rect()
start_rect.center=width/2,height/2+150


#黑洞
blackhole=[]
blackhole_rect=[]
for i in range(6):
    blackhole.append(pg.image.load(ch+"blackhole.png").convert_alpha())
    blackhole_rect.append(blackhole[i].get_rect())
    blackhole_rect[i].center=200+(i%3)*400+40,50+(i//3)*150
r=blackhole_rect[0].width/2
def rebound1(bx,by,ix,iy,w,h=0):

    X=(speed[0]*(iy-by)/speed[1])+bx#X為假定的碰撞範圍
    if by+speed[1]>=iy and (ix-w/2<=X and X<=ix+w/2):
        playspeed=0.1
        speed[1]+=playspeed
        speed[1]*=-1
        speed[0]=random.randint(-5,5)
        return  True,speed
    else:
        return False,speed
def hits(bx,by,ix,iy,r):
    if (bx-ix)**2+(by-iy)**2<=r**2:
        return True
    else:
        return False

def rebound2(bx,by,ix,iy,w,h=0):
    X=(speed[0]*(iy-by)/speed[1])+bx        #X為假定的碰撞範圍
    if by+speed[1]>=iy and (ix-w/2<=X and X<=ix+w/2): 
        return  True
    else:
        return False

def pause(a):
    while a:
        clock.tick(30)
        scoretext = font2.render(f"score:{score}",True,(150,100,100))
        score_rect=scoretext.get_rect()
        score_rect.center=width/2,height/2

        screen.blit(background,back_rect)
        screen.blit(lifetext,life_rect)
        screen.blit(pad,pad_rect)
        screen.blit(startbtn,start_rect)
        screen.blit(scoretext,score_rect)
        pg.display.update()
        for event in pg.event.get():
            if event.type==pg.QUIT:
                operation=False
                pg.quit()
            if event.type==pg.MOUSEBUTTONDOWN:
                x,y=pg.mouse.get_pos()
                if y>=start_rect.top and y<=start_rect.bottom and x>=start_rect.left and x<=start_rect.right :
                    a=False

def restart(a):
    while a:
        clock.tick(30)
        scoretext = font2.render(f"score:{score}",True,(0,0,0))
        score_rect=scoretext.get_rect()
        score_rect.center=width/2,height/2
        #pygame 事件處理
        for event in pg.event.get():
            #正常關閉
            if event.type == pg.QUIT:
                pg.quit()
            if event.type == pg.MOUSEBUTTONDOWN:
                x,y = pg.mouse.get_pos()
                if y>=start_rect.top and y<=start_rect.bottom and x>=start_rect.left and x<=start_rect.right:
                    a=False
        screen.blit(background,back_rect)
        screen.blit(startbtn,start_rect)
        screen.blit(scoretext,score_rect)
        pg.display.update()
    




font=pg.font.SysFont("微軟正黑體",36)
font2 = pg.font.SysFont("微軟正黑體",60)

bnbnoin=True
bnbspeed=[0,0]
bnbnoin2=True
bnbspeed2=[0,0]
healnoin=True
healspeed=[0,0]

operation=True
while operation:
    clock.tick(60)
    lifetext=font.render(f"life:{life}",True,(0,0,0))
    life_rect=lifetext.get_rect()
    life_rect.top=pad_rect.bottom
    life_rect.centerx=pad_rect.centerx

    for event in pg.event.get():
        if event.type==pg.QUIT:
            pg.quit()
        if event.type==pg.MOUSEMOTION:
            x,y=pg.mouse.get_pos()
            pad_rect.centerx=x
        if event.type==pg.MOUSEBUTTONDOWN:
            x,y=pg.mouse.get_pos()
            if y>=pause_rect.top and y<=pause_rect.bottom and x>=pause_rect.left and x<=pause_rect.right :
                a=True
                pause(a)



    if pad_rect.right>=width:
        pad_rect.right=width
    if pad_rect.left<=0:
        pad_rect.left=0
    ball_rect=ball_rect.move(speed[0],speed[1])
    if ball_rect.left<=0:
        speed[0]=speed[0]*(-1)
        ball_rect.left=0
    if ball_rect.right>=width:
        speed[0]=speed[0]*(-1)
        ball_rect.right=width
    if ball_rect.top<=0:
        speed[1]=speed[1]*(-1)
        ball_rect.top=0
    if ball_rect.bottom>=deadline:
        ball_rect.center=width/2,height/2
        life-=1
    
    hit,speed=rebound1(ball_rect.centerx,ball_rect.centery,pad_rect.centerx,pad_rect.centery,pad_rect.width)
    if hit:
        ball_rect.bottom=pad_rect.top
        score+=100
    #黑洞碰撞
    for i in range(6):
        holehit=hits(ball_rect.centerx,ball_rect.centery,blackhole_rect[i].centerx,blackhole_rect[i].centery,r)
        if holehit:
            id=i
            a=random.randint(1,3)
            if a==1:
                speed[0]*=-1
            if a==2:
                speed[1]*=-1
            if a==3:
                speed[0]*=-1
                speed[1]*=-1
            b=random.randint(0,5)
            while b==id:
                b=random.randint(0,5)
            if speed[0]>=0 and speed[1]>0:
                ball_rect.topleft=blackhole_rect[b].bottomright
            if speed[0]>=0 and speed[1]<0:
                ball_rect.bottomleft=blackhole_rect[b].topright
            if speed[0]<=0 and speed[1]>0:
                ball_rect.topright=blackhole_rect[b].bottomleft
            if speed[0]<=0 and speed[1]<0:
                ball_rect.bottomright=blackhole_rect[b].topleft
    
    debomb=False
    debomb2=False
    probi=random.uniform(0,1000)
    if probi<=5 and bnbnoin:
        bnbspeed[1]=random.randint(2,5)
        bnbnoin=False
    bomb_rect=bomb_rect.move(bnbspeed)
    bnbhit=rebound2(bomb_rect.centerx,bomb_rect.centery,pad_rect.centerx,pad_rect.centery,pad_rect.width)
    if bnbhit:
        bnbnoin=True
        debomb=True
        bombold_rect.bottomleft=bomb_rect.bottomleft
        bomb_rect.bottomleft=random.randint(0,width-bomb_rect.width),0
        life-=2
    if bomb_rect.bottom>=deadline:
        bnbnoin=True
        bomb_rect.bottomleft=random.randint(0,width-bomb_rect.width),0


    probi2=random.uniform(0,1000)
    if probi2<=5 and bnbnoin2:
        bnbspeed2[1]=random.randint(2,5)
        bnbnoin2=False
    bomb2_rect=bomb2_rect.move(bnbspeed2)
    bnbhit2=rebound2(bomb2_rect.centerx,bomb2_rect.centery,pad_rect.centerx,pad_rect.centery,pad_rect.width)
    if bnbhit2:
        bnbnoin2=True
        debomb2=True
        bombold2_rect.bottomleft=bomb2_rect.bottomleft
        bomb2_rect.bottomleft=random.randint(0,width-bomb2_rect.width),0
        life-=2
    if bomb2_rect.bottom>=deadline:
        bnbnoin2=True
        bomb2_rect.bottomleft=random.randint(0,width-bomb2_rect.width),0




    healbi=random.uniform(0,1000)
    if healbi<=5 and healnoin:
        healspeed[1]=random.randint(2,5)
        healnoin=False
    heal_rect=heal_rect.move(healspeed)
    healhit=rebound2(heal_rect.centerx,heal_rect.centery,pad_rect.centerx,pad_rect.centery,pad_rect.width)
    if healhit:
        healnoin=True
        heal_rect.bottomleft=random.randint(0,width-heal_rect.width),0
        if life<=6:
            life+=4
    if heal_rect.bottom>=deadline:
        healnoin=True
        heal_rect.bottomleft=random.randint(0,width-heal_rect.width),0
    
    if life <=0:
        restart(True)
        score=0
        life=10

    screen.blit(background,back_rect)
    for i in range(6):
        screen.blit(blackhole[i],blackhole_rect[i])
    screen.blit(bomb,bomb_rect)
    screen.blit(bomb2,bomb2_rect)
    screen.blit(heal,heal_rect)
    if bnbnoin==True and debomb==True:
        screen.blit(bombold,bombold_rect)
    if bnbnoin2==True and debomb2==True:
        screen.blit(bombold2,bombold2_rect)
    screen.blit(ball,ball_rect)
    screen.blit(pad,pad_rect)
    screen.blit(lifetext,life_rect)
    screen.blit(pausebtn,pause_rect)
    pg.display.update()


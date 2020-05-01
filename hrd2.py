#!/usr/bin/python
# -*- coding: UTF-8 -*-
#hrd2 by zoujilin@sina.com @2020.4
from __future__ import print_function
#指定图像文件名称
cc_image_filename    = './image/cc.png' #曹操
gy_image_filename    = './image/gy.png' #关羽
zf_image_filename    = './image/zf.png'
zy_image_filename    = './image/zy.png'
mc_image_filename    = './image/mc.png'
hz_image_filename    = './image/hz.png'
b1_image_filename    = './image/b1.png'

 
import pygame
from pygame.locals import *
from sys import exit
import random
import time
from gameresource import GameResource
from settings import *

enable_print = 0

def print(*args, **kwargs):
    if enable_print:
        return __builtins__.print(*args, **kwargs)


class Person():
    def __init__(self, screen):
        self.screen = screen
        self.brush  = None
        self.step_num = 0
        self.image = [
                pygame.image.load(cc_image_filename).convert(),
                pygame.image.load(gy_image_filename).convert(),
                pygame.image.load(zf_image_filename).convert(),
                pygame.image.load(zy_image_filename).convert(),
                pygame.image.load(hz_image_filename).convert(),
                pygame.image.load(mc_image_filename).convert(),
                pygame.image.load(b1_image_filename).convert(),
                pygame.image.load(b1_image_filename).convert(),
                pygame.image.load(b1_image_filename).convert(),
                pygame.image.load(b1_image_filename).convert()                
            ]
      
        self.rect = [
                pygame.Rect(80 , 0  , 160, 160),  #cc
                pygame.Rect(80 , 160, 160,  80),  #gy
                pygame.Rect(0  , 0  , 80 , 160),      
                pygame.Rect(240, 0  , 80 , 160),      
                pygame.Rect(0  , 160, 80 , 160),      
                pygame.Rect(240, 160, 80 , 160),      
                pygame.Rect(80 , 240, 80 , 80 ),      
                pygame.Rect(160, 240, 80 , 80 ),      
                pygame.Rect(0  , 320, 80 , 80 ),      
                pygame.Rect(240, 320, 80 , 80 ),
            ]

        self.last_pos = [
                [0, 0],
                [0, 0],
                [0, 0],
                [0, 0],
                [0, 0],
                [0, 0],
                [0, 0],
                [0, 0],
                [0, 0],
                [0, 0],
            ]


        self.select = [ 0,0,0,0,0,0,0,0,0,0]

#  1  2  3  4
#  5  6  7  8
#  9 10 11 12
# 13 14 15 16
# 17 18 19 20
        
        self.grid   = [
                [ 2,  3,  6,  7, 8,8,2,2],  #cc start grid is 2 , and size is 2x2 #LT RT LB RB
                [10, 11, 10, 11, 4,4,2,2],  #gy start grid is 10, and size is 2x1 
                [ 1,  1,  5,  5, 8,8,1,1],  #zf start grid is 1 , and size is 1x2
                [ 4,  4,  8,  8, 8,8,1,1],  #zy start grid is 4 , and size is 1x2
                [ 9,  9, 13, 13, 8,8,1,1],  #hz start grid is 9 , and size is 1x2
                [12, 12, 16, 16, 8,8,1,1],  #mc start grid is 12, and size is 1x2
                [14, 14, 14, 14, 4,4,1,1],  #b1 start grid is 14, and size is 1x1
                [15, 15, 15, 15, 4,4,1,1],  #b2 start grid is 15, and size is 1x1
                [17, 17, 17, 17, 4,4,1,1],  #b3 start grid is 17, and size is 1x1
                [20, 20, 20, 20, 4,4,1,1],  #b4 start grid is 20, and size is 1x1     
            ]
        
        self.empty  = [18, 19] #empty grid 
     

    '''        
    def init(self):
        self.rect = [
                pygame.Rect(80 , 0  , 160, 160), #top-left and size
                pygame.Rect(80 , 160, 160,  80),
                pygame.Rect(0  , 0  , 80 , 160),      
                pygame.Rect(240, 0  , 80 , 160),      
                pygame.Rect(0  , 160, 80 , 160),      
                pygame.Rect(240, 160, 80 , 160),      
                pygame.Rect(80 , 240, 80 , 80 ),      
                pygame.Rect(160, 240, 80 , 80 ),      
                pygame.Rect(0  , 320, 80 , 80 ),      
                pygame.Rect(240 ,320, 80 , 80 ),
            ]
    '''
     
    def draw(self):
        self.screen.fill((0, 0, 0)) #fill black background
        for (i, img) in enumerate(self.image):
            #pygame.Rect(self.rect[i])
            self.screen.blit(img, self.rect[i]) #draw every rect with image


    def click_button(self, pos):
        for (i, rect) in enumerate(self.rect):
            if rect.collidepoint(pos): #test if a point is inside a rectangle
                self.select[i]   = 1   #点中的那个人物
                self.last_pos[i] = self.rect[i].topleft  
                #print('click No.%d person, its topleft %s,empty=%s' % (i, self.rect[i].topleft,self.empty))
                print(i, end=', ')
                return True
        return False


    def move_button(self, pos, rel):
        for (i, rect) in enumerate(self.rect): #遍历的数据对象
            if self.select[i] == 1:              
                #self.rect[i].move_ip(rel)
                #print('move No.%d person, its start grid is %s, its rel %s' % (i, self.grid[i][0],rel))
                #print('its start grid is %s' % self.grid[i][0])
                return True
        return False
    
    def move_up(self, i):
        print('\'U\'')
        grid  = self.grid[i]       
        empty = self.empty
        self.rect[i].move_ip(0,-80)
        self.grid[i]=[grid[0]-4, grid[1]-4, grid[2]-4, grid[3]-4, grid[4], grid[5], grid[6], grid[7]]
        for j in range(2):
            if grid[j+2]-grid[4]==empty[0] : self.empty[0]=grid[j+2]
            if grid[j+2]-grid[4]==empty[1] : self.empty[1]=grid[j+2]
        return True

    def move_down(self, i):
        print('\'D\'')
        grid  = self.grid[i]       
        empty = self.empty
        self.rect[i].move_ip(0,80)
        self.grid[i]=[grid[0]+4, grid[1]+4, grid[2]+4, grid[3]+4, grid[4], grid[5], grid[6], grid[7]]
        for j in range(2):
            if grid[j]+grid[5]==empty[0] : self.empty[0]=grid[j]
            if grid[j]+grid[5]==empty[1] : self.empty[1]=grid[j]
        return True                 	
                        	        
    def move_left(self, i):
        print('\'L\'')
        grid  = self.grid[i]       
        empty = self.empty
        self.rect[i].move_ip(-80,0)
        self.grid[i]=[grid[0]-1, grid[1]-1, grid[2]-1, grid[3]-1,grid[4], grid[5], grid[6], grid[7]]
        for j in range(2): 
            if grid[j*2+1]-grid[6]==empty[0] : self.empty[0]=grid[j*2+1]
            if grid[j*2+1]-grid[6]==empty[1] : self.empty[1]=grid[j*2+1]
        return True 

    def move_right(self, i):
        print('\'R\'')
        grid  = self.grid[i]       
        empty = self.empty
        self.rect[i].move_ip(80,0)    
        self.grid[i]=[grid[0]+1, grid[1]+1, grid[2]+1, grid[3]+1,grid[4], grid[5], grid[6], grid[7]]
        for j in range(2):
            if grid[j*2]+grid[7]==empty[0] : self.empty[0]=grid[j*2]
            if grid[j*2]+grid[7]==empty[1] : self.empty[1]=grid[j*2]       
        return True 
                         	        
    def up_mouse(self, pos): #update selected rect and empty
        for (i, rect) in enumerate(self.rect):
             if self.select[i] == 1:
                grid  = self.grid[i]
                u     = grid[4]
                b     = grid[5]
                l     = grid[6]
                r     = grid[7]               
                empty = self.empty
                xoffset= rect.topleft[0] - pos[0]
                yoffset= rect.topleft[1] - pos[1]
    
                #print('grid=%s %s %s %s, empty=%s %s\n offset==%s-%s,xoffset=%s,yoffset=%s' %(grid[0],grid[1],grid[2],grid[3],empty[0],empty[1],rect.topleft,pos,xoffset,yoffset))
                if(grid[0]-4 == empty[0] or grid[0]-4 == empty[1]) and (grid[1]-4 == empty[0] or grid[1]-4 == empty[1]) and yoffset>0 :
                    self.move_up(i)
                    '''
                    print(' up is empty')
                    self.rect[i].move_ip(0,-80)
                    self.grid[i]=[grid[0]-4, grid[1]-4, grid[2]-4, grid[3]-4, grid[4], grid[5], grid[6], grid[7]]
                    for j in range(2):
                        #print('empty[0]=%s grid[j]=%s j=%s' % (empty[0], grid[j], j))
                        if grid[j+2]-u==empty[0] : empty[0]=grid[j+2] #update empty
                        if grid[j+2]-u==empty[1] : empty[1]=grid[j+2]
                    '''    
                elif(grid[2]+4 == empty[0] or grid[2]+4 == empty[1]) and (grid[3]+4 == empty[0] or grid[3]+4 == empty[1]) and yoffset<-80:
                    self.move_down(i)
                    '''
                    print(' bottom is empty')
                    self.rect[i].move_ip(0,80)
                    self.grid[i]=[grid[0]+4, grid[1]+4, grid[2]+4, grid[3]+4, grid[4], grid[5], grid[6], grid[7]]
                    for j in range(2):
                        #print('empty[0]=%s grid[j]=%s j=%s' % (empty[0], grid[j], j))
                        if grid[j]+b==empty[0] : empty[0]=grid[j]
                        if grid[j]+b==empty[1] : empty[1]=grid[j]
                    '''
                elif(grid[0]-1 == empty[0] or grid[0]-1 == empty[1]) and (grid[2]-1 == empty[0] or grid[2]-1 == empty[1]) and xoffset>0:
                    self.move_left(i)
                    '''
                    print(' left is empty')
                    self.rect[i].move_ip(-80,0)
                    self.grid[i]=[grid[0]-1, grid[1]-1, grid[2]-1, grid[3]-1,grid[4], grid[5], grid[6], grid[7]]
                    for j in range(2): #left move, so right will be empty
                        #print('empty[0]=%s grid[j]=%s j=%s' % (empty[0], grid[j], j))
                        if grid[j*2+1]-l==empty[0] : empty[0]=grid[j*2+1]
                        if grid[j*2+1]-l==empty[1] : empty[1]=grid[j*2+1]
                    '''    
                elif(grid[1]+1 == empty[0] or grid[1]+1 == empty[1]) and (grid[3]+1 == empty[0] or grid[3]+1 == empty[1]) and xoffset<-80:  
                    self.move_right(i)
                    '''
                    print(' right is empty')
                    self.rect[i].move_ip(80,0)    
                    self.grid[i]=[grid[0]+1, grid[1]+1, grid[2]+1, grid[3]+1,grid[4], grid[5], grid[6], grid[7]]
                    for j in range(2):
                        #print('empty[0]=%s grid[j]=%s j=%s' % (empty[0], grid[j], j))
                        if grid[j*2]+r==empty[0] : empty[0]=grid[j*2]
                        if grid[j*2]+r==empty[1] : empty[1]=grid[j*2]
                    '''    
                #print('grid=%s %s %s %s, empty=%s %s, after MOVE' %(grid[0],grid[1],grid[2],grid[3],empty[0],empty[1]))
                

                #self.rect[i].topleft = self.last_pos[i] # back to old position 
                self.select[i]       = 0 
                return True
        return False   
        
             
    def auto_move(self):  
        print('AUTO MOVE')   
        def wait_and_update(self):
            self.draw()
            pygame.display.update()      
            pygame.time.wait(400)        
        for a in range(118):
            if MV_STEP[a][1]=='U' : 
            	  self.move_up(MV_STEP[a][0])
            elif MV_STEP[a][1]=='D' : 
            	  self.move_down(MV_STEP[a][0])
            elif MV_STEP[a][1]=='L' : 
            	  self.move_left(MV_STEP[a][0])
            elif MV_STEP[a][1]=='R' : 
            	  self.move_right(MV_STEP[a][0])     
            self.step_num = self.step_num + 1
            a = a + 1
            wait_and_update(self) 
        return True
        
    def step_forward_move(self):
        if(self.step_num<len(MV_STEP)) :  
            a = self.step_num    
            if MV_STEP[a][1]=='U' : 
            	  self.move_up(MV_STEP[a][0])
            elif MV_STEP[a][1]=='D' : 
            	  self.move_down(MV_STEP[a][0])
            elif MV_STEP[a][1]=='L' : 
            	  self.move_left(MV_STEP[a][0])
            elif MV_STEP[a][1]=='R' : 
            	  self.move_right(MV_STEP[a][0])           
            self.step_num = self.step_num + 1
   
   
    def step_back_move(self):  
        if(self.step_num>0) :  
            self.step_num = self.step_num - 1
            a = self.step_num    
            if MV_STEP[a][1]=='U' : 
            	  self.move_down(MV_STEP[a][0])
            elif MV_STEP[a][1]=='D' : 
            	  self.move_up(MV_STEP[a][0])
            elif MV_STEP[a][1]=='L' : 
            	  self.move_right(MV_STEP[a][0])
            elif MV_STEP[a][1]=='R' : 
            	  self.move_left(MV_STEP[a][0])

 
class HRD():
    def __init__(self):
        self.screen = pygame.display.set_mode((320, 400))
        pygame.display.set_caption("HRD 2.0")
        self.clock = pygame.time.Clock()
        self.person = Person(self.screen)
        self.resource = GameResource()
        self.resource.play_bg_music()
           
    def run(self):
        global enable_print
        self.screen.fill((0, 0, 0))
        while True:
            # max fps limit
            self.clock.tick(30)
            for event in pygame.event.get():
                if event.type == QUIT:
                    return
                elif event.type == KEYDOWN:
                    # press esc to clear screen
                    if event.key == K_ESCAPE:
                        enable_print = 1
                        print('ESC KEY') 
                        pygame.quit
                        exit()
                    elif event.key ==K_m:
                        self.resource.pause_bg_music()                      
                    elif event.key ==K_b:
                        self.person.step_back_move()                      
                    elif event.key ==K_f:
                        self.person.step_forward_move()                      
                    elif event.key ==K_a:
                        self.person.__init__(self.screen)                        
                        self.person.auto_move()                      
                    elif event.key ==K_UP:
                        enable_print = 1
                        self.person.__init__(self.screen)                        
                elif event.type == MOUSEBUTTONDOWN:
                    if  self.person.click_button(event.pos): #pos means coordinate when mouse.down
                        #print('mouse-down: click a person')
                        pass
                    else:
                        print('mouse-down: Not click a person')
                        #self.brush.start_draw(event.pos)
                elif event.type == MOUSEMOTION:
                    self.person.move_button(event.pos, event.rel) #rel代表相对距离
                    #print('mouse motion')
                    #self.brush.draw(event.pos)
                elif event.type == MOUSEBUTTONUP:
                    self.person.up_mouse(event.pos)
                    #print('mouse up')
                    #self.brush.end_draw()
 
            self.person.draw()
            pygame.display.update()
 
if __name__ == '__main__':
    app = HRD()
    app.run()
    


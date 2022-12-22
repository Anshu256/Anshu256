import pygame as pg
from pygame.locals import *
from random import shuffle,randrange

#colors
BLACK = (0,0,0)
WHITE = (255,255,255)

pg.init()

WIDTH, HEIGHT = 800, 600
DISPLAY = pg.display.set_mode((WIDTH,HEIGHT))

num_objs = 500

G = 6.67* 10**1 # its actually 10^-11 but we can use 10^1 since each obj is 10^6 kg and (10^6) ^2 = 10^12
rand_list = [[randrange(0,WIDTH),randrange(0,HEIGHT)] for _ in range(num_objs)]

'''
rand_list = [WHITE for i in range(num_objs)] + [BLACK for j in range(WIDTH*HEIGHT -num_objs)]
shuffle(rand_list)
rand_list = [rand_list[x*HEIGHT:(x+1)*HEIGHT+1] for x in range(WIDTH)]
'''

fpsClock = pg.time.Clock()
FPS = 30

calc_radius = 400

#pxarr = pg.PixelArray(DISPLAY)
#edit_pxarr = [[0 for _ in WIDTH] for _ in HEIGHT]

def calc_edit_per_pix(rand_list):
    #calculate effect from gravity in the surrounding area
    #previous motion will also be recognised

    #first, check which objects are in each others radius
    for i,obj_list in enumerate(objects_in_radius(rand_list,calc_radius)):
        for obj_i in obj_list:
            attraction = calc_gravity(i,obj_i)
            if attraction == -1:

                continue
            
            #moving obj_i to i
            attraction = abs(attraction)
            if rand_list[i][0] < rand_list[obj_i][0]:
                attraction*=-1

            slope = (rand_list[i][1]- rand_list[obj_i][1])/(rand_list[i][0]- rand_list[obj_i][0])
            y = slope*attraction/2
            rand_list[obj_i][0] += attraction
            rand_list[obj_i][1] += y

            #moving i to obj_i
            attraction = abs(attraction)
            if rand_list[obj_i][0] < rand_list[i][0]:
                attraction*=-1

            slope = (rand_list[obj_i][1]- rand_list[i][1])/(rand_list[obj_i][0]- rand_list[i][0])
            y = slope*attraction/2
            rand_list[i][0] += attraction
            rand_list[i][1] += y
            
            #rand_list[obj_i][0] %= WIDTH
            #rand_list[obj_i][1] %= HEIGHT
    return None

def objects_in_radius(rand_list,rad):
    if rad**2 > WIDTH*HEIGHT:
        yield rand_list 
    for o1_i,obj1 in enumerate(rand_list):
        obj_list = []
        for o2_i,obj2 in enumerate(rand_list[o1_i+1:]):
            o2_i += o1_i+1
            if ((obj1[0] + rad) > obj2[0]) and ((obj1[0] - rad) < obj2[0]):
                if ((obj1[1] + rad) > obj2[1]) and ((obj1[1] - rad) < obj2[1]):
                    obj_list.append(o2_i)
        yield obj_list

def calc_gravity(obj1_i,obj2_i):
    obj1 = rand_list[obj1_i]
    obj2 = rand_list[obj2_i]

    distance = ((obj1[0]-obj2[0])**2 + (obj1[1]-obj2[1])**2)**0.5
    if distance < 6 :
        rand_list[obj1_i][0] += 3
        rand_list[obj2_i][0] -= 3
        return -1
    try:
        gravity = G/(distance**2) #G* m*M/R**2 m=M=10^6 G=6.67*10^-11 thus, G effectively = 6,67 * 10^-11 * 10^12 = 66.7
    except ZeroDivisionError:
        gravity = 0
    return gravity

#def make_next_pos_list():
#    pass

while True:
    for event in pg.event.get():
        if event.type == QUIT:
            pg.quit()
            exit()

    DISPLAY.fill(BLACK)

    for pos in rand_list:
        x = round(pos[0])
        if 0 > x:
            x = 0
        elif x >= WIDTH:
            x = WIDTH -1

        y = round(pos[1])
        if 0 > y:
            y = 0
        elif y >= HEIGHT:
            y = HEIGHT-1
        
        pg.draw.circle(DISPLAY,WHITE,(x,y),3)
        #pxarr[x][y] = WHITE
        
    calc_edit_per_pix(rand_list)
    #make_next_pos_list()

    pg.display.update()
    fpsClock.tick(FPS)

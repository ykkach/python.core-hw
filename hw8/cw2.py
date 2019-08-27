import pygame
pygame.init()
screen = pygame.display.set_mode((500,500))
pygame.display.set_caption("Draw primitives")
clock = pygame.time.Clock()
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (125, 125, 125)
LIGHT_BLUE = (64, 128, 255)
GREEN = (0, 200, 64)
YELLOW = (225, 225, 0)
PINK = (230, 50, 230)
BLUE=(170, 186, 233)
PI=3.14
done = False
clock = pygame.time.Clock()

while not done:
    for event in pygame.event.get(): 
        if event.type == pygame.QUIT:
            done=True
    
      
    #pygame.draw.polygon(screen, WHITE, [[150, 10], [180, 50], [90, 90], [30, 30]],8)
    #pygame.draw.polygon(screen, WHITE, [[250, 110], [280, 150], [190, 190], [130, 130]])
    #pygame.draw.aalines(screen, WHITE, True, [[250, 110], [280, 150], [190, 190], [130, 130]])

    # r1 = pygame.Rect((150, 20, 100, 75))
 
    # pygame.draw.rect(screen, WHITE, (20, 20, 100, 75))
    # pygame.draw.rect(screen, YELLOW, r1, 8)
    # pygame.draw.ellipse(screen, GREEN, (10, 50, 280, 100))
    # pygame.draw.circle(screen, YELLOW, (100, 100), 50,5)
    # pygame.draw.circle(screen, PINK, (200, 100), 50)
    # pygame.draw.arc(screen, WHITE, (10, 50, 280, 100), 0, PI)
    # pygame.draw.arc(screen, PINK, (50, 30, 200, 150), PI, 2*PI, 3)

    screen.fill(BLUE)
    pygame.display.update()
    clock.tick(60)

    ######################################################################

# import pygame
# pygame.init()
# screen = pygame.display.set_mode((500,500))
# pygame.display.set_caption("My first game")
# #clock = pygame.time.Clock()

# x=50
# y=50
# width=40
# height=60
# vol=4


# run = True
# clock = pygame.time.Clock()

# while run:
#     pygame.time.delay(100)
    
#     for event in pygame.event.get(): 
#         if event.type == pygame.QUIT:
#             run=False

#     keys=pygame.key.get_pressed()
    
#     # if x not in range(500):
#     #     if x>500:
#     #         x-=vol
#     #     else:
#     #         x+=vol
#     # elif y not in range(500):
#     #     if y>500:
#     #         y-=vol
#     #     else:
#     #         y+=vol
#     # else:    
#     if keys[pygame.K_LEFT] and x>vol:
#         x=x-vol
#     if keys[pygame.K_RIGHT] and x<500-width-vol:
#         x=x+vol
#     if keys[pygame.K_UP] and y >vol:
#         y=y-vol
#     if keys[pygame.K_DOWN] and y<500-height-vol:
#         y=y+vol
    

#     # without trace
#     screen.fill((255,255,255))          
    
#     pygame.draw.rect(screen, (170,200,255), [x, y, width, height])
#     pygame.display.update()
#   #clock.tick(60)

############################################


import pygame

# Define some colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)

# Call this function so the Pygame library can initialize itself
pygame.init()
 
# Create an 800x600 sized screen
screen = pygame.display.set_mode([800, 600])
 
# This sets the name of the window
pygame.display.set_caption('Fly')
 
clock = pygame.time.Clock()

#обновляємо екран 
pygame.display.update()
 
# Set positions of graphics
background_position = [0, 0]
 
# Load and set up graphics.
#background_image = pygame.image.load("saturn_family1.jpg").convert()
player_image = pygame.image.load("D:\Lectures\My_lect_Python\Game\+\player.png").convert()

#Якщо в зображення не має прозорого слою, то щоб його встановити,
#необхідно використати метод set_colorkey() класу Surface:
player_image.set_colorkey(BLACK)
 
done = False
 
while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True            
 
    
# Get the current mouse position. This returns the position
    # as a list of two numbers.
#повертає поточну позицію мишки на екрані
    player_position = pygame.mouse.get_pos()
    x = player_position[0]
    y = player_position[1]
 
    # Copy image to screen:
#копіює картинку на екран
    screen.blit(player_image, [x, y])
 
#обновляємо екран
    pygame.display.flip()
 
    clock.tick(60)


pygame.quit()


###########################################


# import pygame
 
# FPS = 60
# W = 700  # ширина екрана
# H = 300  # висота екрана
# WHITE = (255, 255, 255)
# BLUE = (120, 150, 200)
# RIGHT = "to the right"
# LEFT = "to the left"
# STOP = "stop"
 
# pygame.init()
# sc = pygame.display.set_mode((W, H))
# clock = pygame.time.Clock()
 
# # координати і радіус круга
# x = W // 2
# y = H // 2
# r = 50
 
# motion = STOP
 
# while 1:
#     sc.fill(WHITE)
 
#     pygame.draw.circle(sc, BLUE, (x, y), r)
 
#     pygame.display.update()
 
#     for i in pygame.event.get():
#         if i.type == pygame.QUIT:
#             exit()
#         elif i.type == pygame.KEYDOWN:
#             if i.key == pygame.K_LEFT:
#                 motion = LEFT
#             elif i.key == pygame.K_RIGHT:
#                 motion = RIGHT
#         elif i.type == pygame.KEYUP:
#             if i.key in [pygame.K_LEFT, pygame.K_RIGHT]:
#                 motion = STOP
#     if x+r > W:
#         x = r
#     elif x-r < 0:
#         x = W - r
#     if motion == LEFT:
#         x -= 3
#     elif motion == RIGHT:
#         x += 3
    
 
#     clock.tick(FPS)

############################

# tkinter бібліотека для розробки графічного інтерфейсу

# from tkinter import *
# from random import randrange as rnd, choice
# import time
# # створюємо вікно
# root = Tk()

# root.geometry('800x600')

# # задаємо назву вікна

# root.title("Сaught the BALL")

# #створ. об'єкт класу canvas

# canv = Canvas(root,bg='white')

# #pack пакувальник, який дозволяє розміщати 
# #зображення одне за одним
# #fill=BOTH дозволяє заповнювати все доступне місце і по ширині і по висоті
# # expand=1 при розширенні вікна мітка завжди буде посередині 

# canv.pack(fill=BOTH,expand=1)
 
# colors = ['red','orange','yellow','green','blue']
# ###################################################
# def new_ball():
#     canv.delete(ALL)
#     x = rnd(100,700)
#     y = rnd(100,500)
#     r = rnd(30,50)
    
#     #(x-r,y-r)-координати верхнього лівого кута
#     #(x+r,y+r)- координати нижнього правого кута
#     #квадрата, в якому промальовується коло

#     canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
    
#     #root.after(1000,new_ball) 
#     # через 1000 мілісек викон.
#     # функцію  new_ball()
    
#     root.after(1000,new_ball)
# #######################################################     

# new_ball()
# mainloop()


##########################

# from tkinter import *
# from random import randrange as rnd, choice
# import time
# # створюємо вікно
# root = Tk()

# root.geometry('800x600')

# # задаємо назву вікна
# root.title("Сaught the BALL")
 
# canv = Canvas(root,bg='white')
# canv.pack(fill=BOTH,expand=1)
 
# colors = ['red','orange','yellow','green','blue']
# def new_ball():
#     global x,y,r
#     canv.delete(ALL)
#     x = rnd(100,700)
#     y = rnd(100,500)
#     r = rnd(30,50)
#     #виводити рахунок в консоль незручно
#     #зручніше його вивести на canvas
#     #використавши функцію canv.create_text()
#     canv.create_text(60,20,text="Score: "+str(points), font = 'Arial 20')
    
#     canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
#     root.after(1000,new_ball)
     
     
# def click(event):
#     global points
#     if (event.y - y)**2 + (event.x - x)**2 <= r**2:
#         points += 1
 
# points = 0
# new_ball()
# canv.bind('<Button-1>', click)
 
# mainloop()

##################3

# from tkinter import *
# from random import randrange as rnd, choice
# import time
# # створюємо вікно
# root = Tk()

# root.geometry('800x600')

# # задаємо назву вікна
# root.title("Сaught the BALL")
 
# canv = Canvas(root,bg='white')
# canv.pack(fill=BOTH,expand=1)
 
# colors = ['red','orange','yellow','green','blue']
# def new_ball():
#     global x,y,r,ball
#     canv.delete(ball)
#     x = rnd(100,700)
#     y = rnd(100,500)
#     r = rnd(30,50)
#     ball = canv.create_oval(x-r,y-r,x+r,y+r,fill = choice(colors), width=0)
#     root.after(1000,new_ball)

     
     
# def click(event):
#     global points, x, text
#     if (event.y - y)**2 + (event.x - x)**2 <= r**2:
#         points += 1
#         x = -1000
# #видалення круга при кліку
#         canv.delete(text)
#         canv.delete(ball)
#         text = canv.create_text(60,20,text="Score: " + str(points), font = 'Arial 20')
 

# #щоб не можна було «накручувати» очки, 
# # клікаючи багато разів по кругу, 
# # поки він не зникне

# #Після кліку круг не зникає і це не ok.
# #Можна видалити все 
# # canv.delete(ALL), 
# # але тоді буде видалятись і рахунок

# #краще дати імена всім графічним примітивам
# # (тексту text і кулі ball) і видаляти їх окремо один від одного:
 
# #щоб можна було видалити ball, треба перед викликом 
# #функції ball() намалювати цей ball
# ball = canv.create_oval(-100,0,0,0)
# text = canv.create_text(60,20,text="Score: " + str(0), font = 'Arial 20')
# points = 0
# new_ball()
# canv.bind('<Button-1>', click)


# mainloop()
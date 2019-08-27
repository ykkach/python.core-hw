
# import pygame
# WHITE = (255, 255, 255)
# BLACK = (0, 0, 0)
# BLUE = (159, 187, 205)


# pygame.init()
 
# gameDisplay = pygame.display.set_mode([800, 600])
# pygame.display.set_caption('hw1')
 
# clock = pygame.time.Clock()

# pygame.display.update()
# background_position = [0, 0]
 
# #background_image = pygame.image.load("saturn_family1.jpg").convert()
# player_image = pygame.image.load(r"C:\Users\Yaroslav\Pictures\Saved Pictures\images.png").convert()

# player_image.set_colorkey(WHITE)
 
# done = False
 
# while not done:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             done = True            
 
#     player_position = pygame.mouse.get_pos()
#     x = player_position[0]
#     y = player_position[1]
 
#     gameDisplay.blit(player_image, [x, y])
#     pygame.display.update()
#     gameDisplay.fill(BLUE)
#     clock.tick(60)


# pygame.quit()


# ______________________________________________________________________________________________


import pygame
 
FPS = 60
REZ = [800,600]
WHITE = (255, 255, 255)
BLUE = (120, 150, 200)
RIGHT = "to the right"
LEFT = "to the left"
STOP = "stop"
 
pygame.init()
gameDisplay = pygame.display.set_mode(REZ)
pygame.display.set_caption('hw2')
clock = pygame.time.Clock()
x = REZ[0] // 2
y = REZ[1] // 2
r = 50
 
motion = STOP
 
while 1:
    gameDisplay.fill(WHITE)
 
    pygame.draw.circle(gameDisplay, BLUE, (x, y), r)
 
    pygame.display.update()
 
    for i in pygame.event.get():
        if i.type == pygame.QUIT:
            exit()
        elif i.type == pygame.KEYDOWN:
            if i.key == pygame.K_LEFT:
                motion = LEFT
            elif i.key == pygame.K_RIGHT:
                motion = RIGHT
        elif i.type == pygame.KEYUP:
            if i.key in [pygame.K_LEFT, pygame.K_RIGHT]:
                motion = STOP
    if x-r > REZ[0]:
        x = -r
    elif x+r < 0:
        x = REZ[0] + r
    if motion == LEFT:
        x -= 3
    elif motion == RIGHT:
        x += 3
    
 
    clock.tick(FPS)



# ______________________________________________________________________________________________


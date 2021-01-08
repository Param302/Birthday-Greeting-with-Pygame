import pygame
import tkinter as tk

pygame.init()

win = pygame.display.set_mode((1640, 850))

pygame.display.set_caption('HAPPY BIRTHDAY MUMMY')

bg = pygame.image.load('background.jpg')

i = pygame.image.load('ICON.png')
pygame.display.set_icon(i)

# Loading the images
c = pygame.image.load('cake.png')

h = pygame.image.load('H.png')
a = pygame.image.load('A.png')
p = pygame.image.load('P.png')
p = pygame.image.load('P.png')
y = pygame.image.load('Y.png')

b = pygame.image.load('B.png')
i = pygame.image.load('I.png')
r = pygame.image.load('R.png')
t = pygame.image.load('T.png')
h = pygame.image.load('H.png')
d = pygame.image.load('D.png')
a = pygame.image.load('A.png')
y = pygame.image.load('Y.png')

m = pygame.image.load('M.png')
u = pygame.image.load('U.png')
m = pygame.image.load('M.png')
m = pygame.image.load('M.png')
y2 = pygame.image.load('Y2.png')

s1 = pygame.image.load('s1.png')
s2 = pygame.image.load('s2.png')
s3 = pygame.image.load('s3.png')
s4 = pygame.image.load('s4.png')
s5 = pygame.image.load('s5.png')

# Loading the music
music = pygame.mixer.music.load('hb.mp3')
pygame.mixer.music.play(-1)


run = True

# Setting up the images in a function called 'image()'
def image():
    win.blit(bg, (0, 0))

    win.blit(c, (525, 380))

    win.blit(h, (250, 40))
    win.blit(a, (335, 40))
    win.blit(p, (420, 40))
    win.blit(p, (505, 40))
    win.blit(y, (595, 42))

    win.blit(b, (760, 40))
    win.blit(i, (850, 40))
    win.blit(r, (910, 40))
    win.blit(t, (995, 40))
    win.blit(h, (1070, 40))
    win.blit(d, (1165, 35))
    win.blit(a, (1250, 35))
    win.blit(y, (1335, 35))

    win.blit(m, (460, 180))
    win.blit(u, (590, 180))
    win.blit(m, (720, 180))
    win.blit(m, (840, 180))
    win.blit(y2, (950, 180))

    win.blit(s3, (1250, 350))
    win.blit(s3, (100, 250))
    win.blit(s2, (1400, 100))
    win.blit(s4, (1100, 280))
    
while run: 
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    image()
    pygame.display.update()

    
pygame.quit()

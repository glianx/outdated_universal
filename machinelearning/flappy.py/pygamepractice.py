import pygame
import os
os.system('clear')

red = (255,0,0)
green = (0,255,0)
blue = (0,0,255)
white = (255,255,255)
black = (0,0,0)
grey = (100,100,100)
steelblue = (100,150,200)
lightsteelblue = (50,150,200)
tomatored = (255,70,70)

(width, height) = (800, 800) # Dimension of the window

screen = pygame.display.set_mode((width, height)) # Making of the screen
pygame.display.set_caption('Pygame Practice') # Name for the window
screen.fill(steelblue) #This syntax fills the background colour

pixAr = pygame.PixelArray(screen)
pixAr[10][20] = green
pygame.draw.line(screen, lightsteelblue, (100,200), (300,450),30)
pygame.draw.rect(screen, tomatored, (400,300,100,200)) #top right x and y, width, height
pygame.draw.circle(screen, white, (400,800), 75)
pygame.draw.polygon(screen, green, ((200,75),(76,125),(250,375),(400,25),(60,540)))


pygame.display.flip()


running = True
while running:
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      print('program quit')
      running = False
      pygame.quit()
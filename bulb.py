import pgzrun
import pygame
import time
from pygame.locals import *
pygame.init()

screen = pygame.display.set_mode((600, 600))
screen.fill(("white"))
pygame.display.set_caption("Light Bulb")

img = pygame.image.load("images/bulb.jpg")

img2 = pygame.image.load("images/light bulb.jpg")

pygame.display.update()

while True:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

    # img = pygame.image.load("images/bulb.jpg")
    image = pygame.transform.scale(img, (500, 600))
    screen.blit(image, (0, 0))

    pygame.display.update()
    time.sleep(2)

    # img2 = pygame.image.load("images/light bulb.jpg")
    image2 = pygame.transform.scale(img2, (500, 600))
    screen.blit(image2, (0, 0))

    pygame.display.update()
    time.sleep(2)
from tkinter import EventType, font
import pygame
from sys import exit

#Initialize game space
pygame.init()
screen = pygame.display.set_mode((800, 600))
pygame.display.set_caption('Platform')
clock = pygame.time.Clock()

#Background Image
bg = pygame.image.load('Images/space.webp').convert()

#Load player object
player = pygame.image.load('Images/player.png').convert_alpha()
player = pygame.transform.scale(player, (50, 50))
player_rect = player.get_rect(bottomright = (100, 500))
player_vel = 0
player_acc = 0

#Load obstacle object
tri = pygame.image.load('Images/tri.webp').convert_alpha()
tri = pygame.transform.scale(tri, (50, 100))
tri_rect = tri.get_rect(bottomright = (900, 500))

#Load ground objects
ground = pygame.image.load('Images/ground.png').convert_alpha()
ground = pygame.transform.scale(ground, (800, 100))
ground_xpos = 0
ground2 = pygame.image.load('Images/ground.png').convert_alpha()
ground2 = pygame.transform.scale(ground, (800, 100))
ground2_xpos = 800

#Load score
score = 0
score_font = pygame.font.Font('Pixel.ttf', 50)


exit = False
while not exit:
    #Incase 'x' button is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and player_rect.y == 450:
                player_vel = 15
                player_acc = 0.8
    screen.blit(bg, (0,0))

    #Code for the moving ground
    screen.blit(ground, (ground_xpos, 500))
    ground_xpos = ground_xpos-5
    screen.blit(ground2, (ground2_xpos, 500))
    ground2_xpos -= 5
    if(ground_xpos == -800):
        ground_xpos = 800
    elif(ground2_xpos == -800):
        ground2_xpos = 800

    #code for obstacle
    screen.blit(tri, tri_rect)
    tri_rect.x -= 5
    if(tri_rect.x == -100):
        tri_rect.x = 900
    
    #code for player
    player_rect.y -= player_vel
    player_vel -= player_acc
    if(player_rect.y >= 450):
        player_acc = 0
        player_vel = 0
        player_rect.y = 450

    screen.blit(player, player_rect)

    if player_rect.colliderect(tri_rect):
        exit = True
    if tri_rect.x == player_rect.x:
        score += 1
    
    #Render and display score
    score_display = score_font.render(str(score), False, 'Black')
    screen.blit(score_display, (750, 25))

    pygame.display.update() #update entire screen
    clock.tick(60)
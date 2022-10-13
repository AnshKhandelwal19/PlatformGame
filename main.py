from tkinter import CENTER, EventType, font
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
file = open('highscore.txt', 'r')
content = file.readlines()
if(len(content) == 0):
    highscore = 0
else:
    highscore = int(content[0])
file.close()

score = 0
score_font = pygame.font.Font('Pixel.ttf', 50)
highscore_font = pygame.font.Font('Pixel.ttf', 50)

#Intro screen fonts
game_font = pygame.font.Font('Pixel.ttf', 150)
game_display = game_font.render('Platform', False, 'Black')
game_display_rect = game_display.get_rect(center = (400, 200))

start_font = pygame.font.Font('Pixel.ttf', 75)
start_display = start_font.render('Start', False, 'Black')
start_rect = start_display.get_rect(center = (400, 300))


#Endgame Screen Fonts
game_over_font = pygame.font.Font('Pixel.ttf', 100)
game_over = game_over_font.render('Game Over', False, 'Black')
game_over_rect = game_over.get_rect(center = (400, 200))

play_again_font = pygame.font.Font('Pixel.ttf', 50)
play_again = play_again_font.render('Again', False, 'Black')
play_again_rect = play_again.get_rect(center = (300, 300))

quit_font = pygame.font.Font('Pixel.ttf', 50)
quit = quit_font.render('Quit', False, 'Black')
quit_rect = quit.get_rect(center = (500, 300))


#Intro Splash Screen
exit = False
while not exit:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        if event.type == pygame.MOUSEMOTION:
            if start_rect.collidepoint(event.pos):
                start_display = start_font.render('Start', False, 'White')
                start_rect = start_display.get_rect(center = (400, 300))
            else:
                start_display = start_font.render('Start', False, 'Black')
                start_rect = start_display.get_rect(center = (400, 300))
        if event.type == pygame.MOUSEBUTTONDOWN:
            if start_rect.collidepoint(event.pos):
                exit = True

    screen.blit(bg, (0,0))
    screen.blit(game_display, game_display_rect)
    screen.blit(start_display, start_rect)

    highscore_display = highscore_font.render('Highscore: ' + str(highscore), False, 'Black')
    highscore_rect = highscore_display.get_rect(center = (400, 400))
    screen.blit(highscore_display, highscore_rect)

    pygame.display.update()

gameOver = False
while True:
    #Incase 'x' button is pressed
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
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
        gameOver = True
        if(score > highscore):
            file = open('highscore.txt', 'w')
            file.write(str(score))
            file.close()

    if tri_rect.x == player_rect.x:
        score += 1
    
    #Render and display score
    score_display = score_font.render(str(score), False, 'Black')
    screen.blit(score_display, (750, 25))

    pygame.display.update() #update entire screen

    while gameOver:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit()
            if event.type == pygame.MOUSEMOTION:
                if play_again_rect.collidepoint(event.pos):
                    play_again = start_font.render('Again', False, 'White')
                    play_again_rect = play_again.get_rect(center = (300, 300))
                else:
                    play_again = play_again_font.render('Again', False, 'Black')
                    play_again_rect = play_again.get_rect(center = (300, 300))
                if quit_rect.collidepoint(event.pos):
                    quit = start_font.render('Quit', False, 'White')
                    quit_rect = quit.get_rect(center = (500, 300))
                else:
                    quit = quit_font.render('Quit', False, 'Black')
                    quit_rect = quit.get_rect(center = (500, 300))

            if event.type == pygame.MOUSEBUTTONDOWN:
                if play_again_rect.collidepoint(event.pos):
                    gameOver = False
                    tri_rect = tri.get_rect(bottomright = (900, 500))
                elif quit_rect.collidepoint(event.pos):
                    exit()

        screen.blit(bg, (0,0))
        screen.blit(game_over, game_over_rect)
        screen.blit(play_again, play_again_rect)
        screen.blit(quit, quit_rect)

        highscore_display = highscore_font.render('High: ' + str(highscore), False, 'Black')
        highscore_rect = highscore_display.get_rect(center = (300, 400))
        score_display = score_font.render('Score: ' + str(score), False, 'Black')
        score_rect = score_display.get_rect(center = (500, 400))
        screen.blit(highscore_display, highscore_rect)
        screen.blit(score_display, score_rect)

        pygame.display.update()

    clock.tick(60)


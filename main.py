import pygame
from util import * 
from models.Head import Head

pygame.init()

SCREEN_WIDTH = 600
SCREEN_HEIGTH = 600
CELL_SIZE = 10
speed = 30
direction = "up"
bg = (255,200,150)

screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGTH))
pygame.display.set_caption("Snake")

player_rect = pygame.Rect(SCREEN_WIDTH // 2, SCREEN_HEIGTH // 2, CELL_SIZE, CELL_SIZE)
player = Head(player_rect, pygame)
food = pygame.Rect((random_position_width(SCREEN_WIDTH), random_position_heigth(SCREEN_HEIGTH), CELL_SIZE, CELL_SIZE))
clock = pygame.time.Clock()

def draw_screen():
    screen.fill(bg)

def hit_border():
    pass

def check_food_collision():
    global food
    if player.rect.colliderect(food):
        food = pygame.Rect(random_position_width(SCREEN_WIDTH), random_position_heigth(SCREEN_HEIGTH), CELL_SIZE, CELL_SIZE)
        increase_speed()


def grow_tail():
    pass

def place_new_food():
    pass

def increase_speed():
    global speed
    speed += 3

run = True
while run:

    clock.tick(speed)
    
    draw_screen()

    pygame.draw.rect(screen, (255, 0, 0), player)
    pygame.draw.rect(screen, (0, 255, 0), food)
    

    key = pygame.key.get_pressed()

    if key[pygame.K_a] == True:
        direction = "left"
    elif key[pygame.K_d] == True:
        direction = "right"
    elif key[pygame.K_w] == True:
        direction = "up"
    elif key[pygame.K_s] == True:
        direction = "down"

    player.move(direction)
    check_food_collision()
    

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    pygame.display.update()
            
pygame.quit()
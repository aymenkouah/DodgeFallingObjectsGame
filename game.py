# Made by: Kouah Mohammed Aymen
# Computer science student at "National Computer science Engineering School, Algiers (ESI)"
# E-mail: jm_kouah@esi.dz
# Github: https://github.com/aymenkouah
# Requires installing "pygame"
# https:\\pygame.org
# Open the read_me file for more info about the game and the playing method

#pay good attention as there is a small trick that allows you to collect points without having to do much dodging(not at all in fact)


import pygame
import sys
import random

pygame.init()

scr_width = 600
scr_height = 600


screen = pygame.display.set_mode((scr_width, scr_height))


rect_color = (0, 255, 0)
bg_color = (0, 0, 0)
rect_pos = [300, scr_height - 100, 50, 50]
enemy_color = (255, 0, 0)
enemy_pos = [random.randint(0, scr_width-50), 0, 50, 50]
game_over = False
clock = pygame.time.Clock()
enemy_list = [enemy_pos]
score = 0
initial = 1


def detect_col(rect_pos, enemy_pos):
    px = rect_pos[0]
    py = rect_pos[1]

    if abs(px - enemy_pos[0]) < 50 and abs(py - enemy_pos[1]) < 50:
        return True
    else:
        return False


def drop_enem(enemy_list):
    delay = random.random()
    if len(enemy_list) < 11 and delay < 0.4:
        enemy_list.append([50*random.randint(0, scr_width/50), 0, 50, 50])


def draw_enem(enemy_list):
    for enemy in enemy_list:
        pygame.draw.rect(screen, enemy_color, enemy)


def enem_pos(enemy_list, score):
    ind = -1
    for enem in enemy_list:
        ind += 1
        if enem[1] <= scr_height and enem[1] >= 0:
            enem[1] += 10
        else:
            enemy_list.pop(ind)
            score = score + 1
    return score


while not (game_over):

    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            sys.exit()

        if event.type == pygame.KEYDOWN:
            x_pos = rect_pos[0]
            y_pos = rect_pos[1]
            if event.key == pygame.K_LEFT:
                x_pos -= 50
            elif event.key == pygame.K_RIGHT:
                x_pos += 50
            rect_pos[0] = x_pos
            rect_pos[1] = y_pos

    screen.fill(bg_color)

    pygame.draw.rect(screen, rect_color, rect_pos)

    drop_enem(enemy_list)
    score = enem_pos(enemy_list, score)
    draw_enem(enemy_list)

    clock.tick(20 + score*0.2)
    pygame.draw.polygon(screen, (255, 255, 255), [
                        (140, 160), (140, 200), (1060, 200), (1060, 160)])
    pygame.display.update()

    for item in enemy_list:
        if detect_col(rect_pos, item):
            game_over = True
            break


print(f"your score is : {score} ")

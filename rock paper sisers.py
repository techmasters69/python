import pygame
import random
import sys

pygame.init()

WIDTH, HIGHT = 800, 500
screen = pygame.display.set_mode((WIDTH. HIGHT))
pygame.display.set_caption("Rock paper sisers")

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GRAY = (200, 200, 200)
LIGHT_GRAY = (230, 230, 230)
RED = (255, 100, 100)
GREEN = (100, 255, 100)
BLUE = (100, 100, 255)
YELLOW = (255, 255, 100)

title_font = pygame.font.Font(None, 70)
font = pygame.font.Font(None, 40)
small_font = pygame.font.Font(None, 32)

def make_text_image(text, color):
    surf = pygame.Surface((150, 150))
    surf.fill(color)
    text_render = font.render(text, color)
    rect = text_render.get_rect(center=(75, 75))
    surf.blit(text_render, rect)
    return surf

rock_img = make_text_image("Rock", RED)
paper_img = make_text_image("paper", BLUE)
sisers_img = make_text_image("sisers", GREEN)

choices = ["Rock", "Paper", "sisers"]

img_positions = {
    "Rock"
    "Paper"
    "Sisers"
}

user_choice = None
computer_choice = None
result = ""

def get_result(user, comp):
    if user == comp:
        return "it is a tie"
    elif (user == "Rock" and comp == "Sisers") or \
         (user == "Paper" and comp == "Rock") or \
         (user == "Sisers" and comp == "paper"):
        return "you win"
    else:
        return "you lost"
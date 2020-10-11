# The SUDOKU GAME

import pygame
from solver import solve, valid
import time
pygame.font.init()

class Grid:
    board = [
        [7,8,0,4,0,0,1,2,0],
        [6,0,0,0,7,5,0,0,9],
        [0,0,0,6,0,1,0,7,8],
        [0,0,7,0,4,0,2,6,0],
        [0,0,1,0,5,0,9,3,0],
        [9,0,4,0,6,0,0,0,5],
        [0,7,0,3,0,0,0,1,2],
        [1,2,0,0,0,7,4,0,0],
        [0,4,9,2,0,6,0,0,7]
    ]

    def __init__(self, rows, cols, width, heigth):
        pass

    def update_model(self):
        pass

    def place(self, val):
        pass

    def sketch(self, val):
        pass

    def draw(self, win):
        pass

    def select(self, row, col):
        pass

    def clear(self):
        pass

    def click(self, pos):
        pass

    def is_finished(self):
        pass

class Cube:
    def __init__(self, value, row, col, width, height):
        pass

    def draw(self, win):
        pass

    def set(self, val):
        pass

    def set_temp(self, val):
        pass

def redraw_window(win, board, time, strikes):
    pass

def format_time(secs):
    pass

def main():
    pass

main()
pygame.quit()
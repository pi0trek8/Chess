import pygame
import config

class Piece:
    def __init__(self, type, row, col, is_white, image):
        self.square = config.board[row][col]
        self.type = type
        self.is_white = is_white
        self.graphic = pygame.image.load(image).convert_alpha()
    
    def move(self, square):
        self.square = square
        
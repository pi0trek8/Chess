import pygame

class Piece:
    def __init__(self, type, square, color, image):
        self.square = square
        self.type = type
        self.color = color
        self.graphic = pygame.image.load(image).convert_alpha()
    
    def move(self, square):
        self.square = square

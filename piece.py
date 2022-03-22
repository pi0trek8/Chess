import pygame
import config
import chessboard

class Piece:
    def __init__(self, type, row, col, is_white, image):
        self.square = config.board[row][col]
        self.rect = pygame.rect.Rect(col*config.SQUARE_SIZE+config.OFFSET, row*config.SQUARE_SIZE+config.OFFSET, config.SQUARE_SIZE, config.SQUARE_SIZE)
        self.type = type
        self.is_white = is_white
        self.graphic = pygame.image.load(image).convert_alpha()
        self.drag = False
    
    def move(self, square):
        self.square = square

    def put_down(self, event):
        square = chessboard.square_clicked(event)
        self.move(square)
        
    def move(self, square):
        if square.piece == None:
            self.square.piece = None
            square.piece = self
            self.square = square
            self.rect.x = square.rect.x
            self.rect.y = square.rect.y
        else:
            self.rect.x = self.square.rect.x
            self.rect.y = self.square.rect.y
        #TODO
        #elif killable(self, square.piece)...
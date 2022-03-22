import pygame
import config
import time

class Square:
    def __init__(self, x, y, size, is_white, piece):
        self.size = size
        self.x_start = x * self.size # Position of square's top left corner 
        self.y_start = y * self.size
        self.rect = pygame.rect.Rect(self.x_start + config.OFFSET , self.y_start + config.OFFSET, size, size)
        self.is_white = is_white  # White or black boolean
        self.piece = piece

# Loop over 8 rows and columns creating Square object for each square on the board
# inverting boolean to keep alternating square colors
# returns 2d list of squares
def init_board(square_size):
    board =[]
    is_white = False
    for y in range(8):
        board_row = []
        is_white = not is_white
        for x in range(8):
            board_row.append(Square(x, y, square_size, is_white, None))
            is_white = not is_white
        board.append(board_row)

    return board

# Loop over each square, create surface in square color and copy it to window at square coordinates
def draw_board(window, board):
    window.fill((0,0,0))
    for row in board:
        for square in row:
            surf = pygame.Surface((square.size, square.size))

            if square.is_white:
                #color of white square
                surf.fill((240, 240, 240))
            else:
                #color of black square
                surf.fill((20, 20, 20))

            window.blit(surf, (square.x_start, square.y_start)) # Paste colored square to the board window

def draw_pieces(window, board):  # Copy piece image onto the window surface
    for row in board:
        for square in row:        
            if square.piece != None:
                piece = square.piece
                window.blit(piece.graphic, (piece.rect.x, piece.rect.y))

def square_clicked(event):
    for row in config.board:
        for square in row:
            if square.rect.collidepoint(event.pos):
                return square
    return None

def piece_clicked(event):
    for row in config.board:
        for square in row:
            if square.piece != None:
                if square.piece.rect.collidepoint(event.pos):
                    return square.piece
    return None

def show_squares():
    for num, row in enumerate(config.board):
        for square in row:
            pygame.draw.rect(config.WINDOW, (0,240,0), square.rect)
            pygame.display.update()
            time.sleep(0.07)

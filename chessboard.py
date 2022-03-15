import pygame

class Square:
    def __init__(self, x, y, size, is_white, piece):
        self.size = size
        self.x_start = x * self.size # Position of square's top left corner 
        self.y_start = y * self.size
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
    for row in board:
        for square in row:
            surf = pygame.Surface((square.size, square.size))

            if square.is_white:
                surf.fill((240, 240, 240))
            else:
                surf.fill((20, 20, 20))

            if square.piece != None:
                surf.blit(square.piece.graphic, (0,0)) # Copy piece image onto the square surface

            window.blit(surf, (square.x_start, square.y_start))
    pygame.display.update()
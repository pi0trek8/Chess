import pygame
import chessboard
import piece

def init_global():
    # Initialize global constants
    global WINDOW, BOARD_WINDOW, BOARD_WIDTH, BOARD_HEIGHT, SQUARE_SIZE, FPS
    WIDTH, HEIGHT = 820, 820
    BOARD_WIDTH, BOARD_HEIGHT = 800, 800
    SQUARE_SIZE = 100
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT)) # Display surface(screen)
    BOARD_WINDOW = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT)) # Chessboard surface
    FPS = 60 # Designated framerate

    # Initialize global variables
    side_to_move = "w"
    half_clock = 0

# Create 2d list of Squares in board global variable
def init_board(): 
    global board
    board = chessboard.init_board(SQUARE_SIZE) # Leave part of the window outside the board
import pygame
import chessboard
import piece

def init_global():
    # Initialize global variables
    global WINDOW, BOARD_WINDOW, BOARD_WIDTH, BOARD_HEIGHT, FPS
    WIDTH, HEIGHT = 820, 820
    BOARD_WIDTH, BOARD_HEIGHT = 800, 800
    WINDOW = pygame.display.set_mode((WIDTH, HEIGHT)) # Display surface(screen)
    BOARD_WINDOW = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT)) # Chessboard surface
    FPS = 60 # Designated framerate


# Create 2d list of Squares in board global variable
def init_board(): 
    global board
    board = chessboard.init_board(BOARD_WIDTH, BOARD_HEIGHT) # Leave part of the window outside the board

# Initialize the pieces on correct squares of the board
#TODO load pieces at FEN stated locations
def init_pieces():
    black = 0
    white = 1
    a_pawn = piece.Piece("pawn", board[2][2], white, 'graphics/pawn_white.png')
    board[2][2].piece = a_pawn
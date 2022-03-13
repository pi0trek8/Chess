import pygame
import chessboard

# Initialize global variables
WIDTH, HEIGHT = 820, 820
BOARD_WIDTH, BOARD_HEIGHT = 800, 800
WINDOW = pygame.display.set_mode((WIDTH, HEIGHT)) # Display surface(screen)
BOARD_WINDOW = pygame.Surface((BOARD_WIDTH, BOARD_HEIGHT))

FPS = 60 # Designated framerate

# Update screen window
def draw_window():
    chessboard.draw_board(BOARD_WINDOW, board) # Update screen
    WINDOW.fill((150,150,150)) # Color margin(background) space
    WINDOW.blit(BOARD_WINDOW, (10, 10))

# Create 2d list of Squares in board global variable
def init_board(): 
    global board
    board = chessboard.init_board(BOARD_WIDTH, BOARD_HEIGHT) # Leave part of the window outside the board

def main():
    clock = pygame.time.Clock() # Clock to keep framerate stable
    init_board()

    run = True
    while run:
        clock.tick(FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()
    
    pygame.quit() # Quit program after game loop terminates


if __name__ == "__main__":
    main()
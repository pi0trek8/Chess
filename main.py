import pygame
import config, fen, chessboard

# Update screen window
def draw_window():
    chessboard.draw_board(config.BOARD_WINDOW, config.board) # Update screen
    config.WINDOW.fill((150,150,150)) # Color margin(background) space
    config.WINDOW.blit(config.BOARD_WINDOW, (10, 10))

def main():
    clock = pygame.time.Clock() # Clock to keep framerate stable
    config.init_global()
    config.init_board()
    fen.load_state()

    run = True
    while run:
        clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

        draw_window()
    
    pygame.quit() # Quit program after game loop terminates


if __name__ == "__main__":
    main()
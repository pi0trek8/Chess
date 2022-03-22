import pygame
import config, fen, chessboard

# Update screen window
def draw_window():
    chessboard.draw_board(config.BOARD_WINDOW, config.board) # Update screen
    config.WINDOW.fill((150,150,150)) # Color margin(background) space
    config.WINDOW.blit(config.BOARD_WINDOW, (10, 10))
    chessboard.draw_pieces(config.WINDOW, config.board)
    pygame.display.update()

def main():
    clock = pygame.time.Clock() # Clock to keep framerate stable
    config.init_global()
    config.init_board()
    fen.load_state()
    #fen.load_state("8/8/8/3p4/4P3/8/8/8")

    run = True
    piece = None
    while run:
        clock.tick(config.FPS)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False

            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    piece = chessboard.piece_clicked(event)
                    if piece is not None:
                        piece.drag = True
                        mouse_x, mouse_y = event.pos
                        offset_x = piece.rect.x - mouse_x
                        offset_y = piece.rect.y - mouse_y
                            
            elif event.type == pygame.MOUSEBUTTONUP:
                if event.button == 1:
                    if piece is not None:
                        piece.drag = False
                        piece.put_down(event)

            elif event.type == pygame.MOUSEMOTION:
                if piece != None:
                    if piece.drag:
                        mouse_x, mouse_y = event.pos
                        piece.rect.x = mouse_x + offset_x
                        piece.rect.y = mouse_y + offset_y
        draw_window()
    
    pygame.quit() # Quit program after game loop terminates


if __name__ == "__main__":
    main()
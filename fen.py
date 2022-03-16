import string
import config
import piece

# Load the pieces on correct squares of the board
#TODO load pieces at FEN stated locations
def load_state(fen_string: string='rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1'):

    sections = fen_string.split()
    rows = sections[0].split('/')

    for row_num, row in enumerate(rows):
        col_num = 0
        for x in row:
            is_white = x.isupper()
            if x.isalpha():
                match x:
                    case 'p':
                        config.board[row_num][col_num].piece = piece.Piece("pawn", row_num, col_num, is_white, 'graphics/pawn_black.png')
                    case 'P':
                        config.board[row_num][col_num].piece = piece.Piece("pawn", row_num, col_num, is_white, 'graphics/pawn_white.png')
                    case 'r':
                        config.board[row_num][col_num].piece = piece.Piece("pawn", row_num, col_num, is_white, 'graphics/rook_black-1.png')
                    case 'R':
                        config.board[row_num][col_num].piece = piece.Piece("rook", row_num, col_num, is_white, 'graphics/rook_white-1.png')
                    case 'b':
                        config.board[row_num][col_num].piece = piece.Piece("pawn", row_num, col_num, is_white, 'graphics/bishop_black-1.png')
                    case 'B':
                        config.board[row_num][col_num].piece = piece.Piece("pawn", row_num, col_num, is_white, 'graphics/bishop_white-1.png')
                    case 'n':
                        config.board[row_num][col_num].piece = piece.Piece("pawn", row_num, col_num, is_white, 'graphics/knight_black.png')
                    case 'N':
                        config.board[row_num][col_num].piece = piece.Piece("pawn", row_num, col_num, is_white, 'graphics/knight_white.png')
                    case 'k':
                        config.board[row_num][col_num].piece = piece.Piece("pawn", row_num, col_num, is_white, 'graphics/king_black.png')
                    case 'K':
                        config.board[row_num][col_num].piece = piece.Piece("pawn", row_num, col_num, is_white, 'graphics/king_white.png')
                    case 'q':
                        config.board[row_num][col_num].piece = piece.Piece("pawn", row_num, col_num, is_white, 'graphics/queen_black.png')
                    case 'Q':
                        config.board[row_num][col_num].piece = piece.Piece("pawn", row_num, col_num, is_white, 'graphics/queen_white.png')
                col_num += 1
            elif x.isnumeric():
                print(int(x)==8)
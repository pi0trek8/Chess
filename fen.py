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
                        config.board[row_num][col_num].piece = piece.Piece("rook", row_num, col_num, is_white, 'graphics/rook_black-1.png')
                    case 'R':
                        config.board[row_num][col_num].piece = piece.Piece("rook", row_num, col_num, is_white, 'graphics/rook_white-1.png')
                    case 'b':
                        config.board[row_num][col_num].piece = piece.Piece("bishop", row_num, col_num, is_white, 'graphics/bishop_black-1.png')
                    case 'B':
                        config.board[row_num][col_num].piece = piece.Piece("bishop", row_num, col_num, is_white, 'graphics/bishop_white-1.png')
                    case 'n':
                        config.board[row_num][col_num].piece = piece.Piece("knight", row_num, col_num, is_white, 'graphics/knight_black.png')
                    case 'N':
                        config.board[row_num][col_num].piece = piece.Piece("knight", row_num, col_num, is_white, 'graphics/knight_white.png')
                    case 'k':
                        config.board[row_num][col_num].piece = piece.Piece("king", row_num, col_num, is_white, 'graphics/king_black.png')
                    case 'K':
                        config.board[row_num][col_num].piece = piece.Piece("king", row_num, col_num, is_white, 'graphics/king_white.png')
                    case 'q':
                        config.board[row_num][col_num].piece = piece.Piece("queen", row_num, col_num, is_white, 'graphics/queen_black.png')
                    case 'Q':
                        config.board[row_num][col_num].piece = piece.Piece("queen", row_num, col_num, is_white, 'graphics/queen_white.png')
                col_num += 1
            elif x.isnumeric():
                col_num += int(x)
    
    #config.side_to_move = sections[1]

    #TODO Castling ability
    #TODO en passant target square
    #TODO fix half clock when last move avilable
    if "last move.capture" or "lastmove.pawnmove":
        config.half_clock = 0
    else:
        config.half_clock += 1

    #TODO move counter

def state_fen():
    fen_string = ""

    for row in config.board:
        for square in row:
            match square.piece.type:
                case "pawn":
                    if square.piece.is_white:
                        fen_string += 'P'
                    else:
                        fen_string += 'p'
                case "rook":
                    if square.piece.is_white:
                        fen_string += 'R'
                    else:
                        fen_string += 'r'
                case "knight":
                    if square.piece.is_white:
                        fen_string += 'N'
                    else:
                        fen_string += 'n'
                case "bishop":
                    if square.piece.is_white:
                        fen_string += 'B'
                    else:
                        fen_string += 'b'
                case "king":
                    if square.piece.is_white:
                        fen_string += 'K'
                    else:
                        fen_string += 'k'
                case "queen":
                    if square.piece.is_white:
                        fen_string += 'Q'
                    else:
                        fen_string += 'q'
        fen_string += '/'
    fen_string += ' '
    
    #TODO
    #If lastmove.is_white:
    #   fen_string += 'w'
    #else:
    #   fen_string += 'b'

    #TODO casting ability
    #TODO en passant target square

    fen_string += string(config.half_clock)
    fen_string += ' '

    #TODO
    #fen_string += string(config.move_counter)
    #fen_string += ' '
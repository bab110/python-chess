import chess

# file = chess.square_file(chess.H5)
# print(file)

# rank = chess.square_rank(chess.H5)
# print(rank)

# distance = chess.square_distance(-1, chess.A1)
# print(distance)

board = chess.Board()
board.chess960 = True
print(board.unicode())

type = board.pieces(chess.KNIGHT, chess.BLACK)
print(type)
print(chess.Board().legal_moves)
print(board.find_move(chess.E2, chess.E3))

board = chess.Board("1rbqkbnr/pppp1Qpp/2n5/4p3/2B1P3/8/PPPP1PPP/1rbqkbnr b KQk - 0 4")
print(board.is_game_over())
outcome = board.outcome()
print(outcome)
if outcome:
    if outcome.winner == chess.WHITE:
        print("white won")
    elif outcome.winner == chess.BLACK:
        print("black won")
    else:
        print("draw")
else:
    print("game not yet over")
    
squares = chess.SquareSet(chess.C1)
print(squares)

board = chess.Board("3k4/4P3/8/8/8/8/3P4/3K3R w K - 0 1")
print(board.unicode())
type = board.pieces(chess.PAWN, chess.WHITE)
print(type)

piece_type = board.piece_type_at(chess.E7)
print(piece_type)

print(board.find_move(chess.E7, chess.E8))

print(board.is_legal(chess.Move.from_uci("g7g8p")))
board.push

print(chess.Board().legal_moves)

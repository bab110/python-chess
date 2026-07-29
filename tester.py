import chess

file = chess.square_file(chess.H5)
print(file)

rank = chess.square_rank(chess.H5)
print(rank)

distance = chess.square_distance(chess.H5, chess.H8)
print(distance)

board = chess.Board()
type = board.pieces(chess.QUEEN, chess.BLACK)
print(type)

board = chess.Board("7K/7P/7k/8/6q1/8/8/8 w - - 0 1")
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
print(board.unicode())

piece_type = board.piece_type_at(chess.C4)
print(piece_type)

print(board.is_legal(chess.Move.from_uci("g7g8p")))
board.push

print(chess.Board().legal_moves)

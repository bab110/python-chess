import chess

distance = chess.square_distance(chess.A1, chess.H3)
print(distance)

board = chess.Board()
type = board.pieces(chess.QUEEN, chess.BLACK)
print(type)
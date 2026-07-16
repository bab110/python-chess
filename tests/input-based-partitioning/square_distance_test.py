import chess

def test_square_distance():
    assert chess.square_distance(chess.A1, chess.A1) == 0
    assert chess.square_distance(chess.A1, chess.H8) == 7
    assert chess.square_distance(chess.A1, chess.E4) == 4
    assert chess.square_distance(chess.D4, chess.E5) == 1
    assert chess.square_distance(chess.B2, chess.C3) == 1
    assert chess.square_distance(chess.G7, chess.H8) == 1
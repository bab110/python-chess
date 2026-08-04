import chess
import unittest

class FindMoveTest(unittest.TestCase):
    
    def setUp(self):
        self.board = chess.Board()
    
    # Test: IDM-FM-01
    # Description: Test a valid legal move in standard chess.
    def test_find_move_legal(self):
        self.assertEqual(self.board.find_move(chess.E2, chess.E3), chess.Move.from_uci("e2e3"))
    
    # Test: IDM-FM-02
    # Description: Test normal, illegal move in chess960.
    def test_find_move_illegal(self):
        self.board.chess960 =  True
        with self.assertRaises(chess.IllegalMoveError):
            self.board.find_move(chess.E2, chess.F2)
        
    # Test: IDM-FM-03
    # Description: Test a valid legal castling move in standard chess.
    def test_find_move_legal_castling(self):
        board = chess.Board("4k3/1P6/8/8/8/8/3P4/4K2R w K - 0 1")
        self.assertEqual(board.find_move(chess.E1, chess.G1), chess.Move.from_uci("e1g1"))
    
    # Test: IDM-FM-04
    # Description: Test an illegal castling move in chess960.
    def test_find_move_illegal_castling(self):
        board = chess.Board("4k3/1P6/8/8/8/8/3P4/4K2R w K - 0 1")
        board.chess960 =  True
        with self.assertRaises(chess.IllegalMoveError):
                self.board.find_move(chess.E1, chess.G1)
    
    # Test: IDM-FM-05
    # Description: Test a valid legal move where pawn moves to back rank and is promoted in standard chess.
    def test_find_move_legal_promotion(self):
        board = chess.Board("3k4/4P3/8/8/8/8/3P4/3K3R w K - 0 1")
        self.assertEqual(board.find_move(chess.E7, chess.E8), chess.Move.from_uci("e7e8q"))
    
    # Test: IDM-FM-06
    # Description: Test a valid illegal move where pawn moves to back rank in chess960.
    def test_find_move_illegal_promotion(self):
        board = chess.Board("3k4/8/4P3/8/8/8/3P4/3K3R w K - 0 1")
        board.chess960 = True
        self.assertEqual(board.find_move(chess.E6, chess.E7), chess.Move.from_uci("e6e7"))
        with self.assertRaises(chess.IllegalMoveError):
                self.board.find_move(chess.E7, chess.F8)
    
    # Test: IDM-FM-07
    # Description: Test a valid legal move where promotion is specified to Rook in chess960.
    def test_find_move_legal_rook(self):
        board = chess.Board("3k4/4P3/8/8/8/8/3P4/3K3R w K - 0 1")
        board.chess960 = True
        self.assertEqual(board.find_move(chess.E7, chess.E8, chess.ROOK), chess.Move.from_uci("e7e8r"))
    
    # Test: IDM-FM-08
    # Description: Test an illegal move where promotion is specified to Rook in standard chess.
    def test_find_move_illegal_rook(self):
        board = chess.Board("3k4/8/4P3/8/8/8/3P4/3K3R w K - 0 1")
        with self.assertRaises(chess.IllegalMoveError):
            self.board.find_move(chess.E6, chess.E7, chess.ROOK)
    
    # Test: IDM-FM-09
    # Description: Test an invalid previous square input that is below 0 in standard chess.
    def test_find_move_invalid_from_square_below(self):
        with self.assertRaises(chess.IllegalMoveError):
            self.board.find_move(-1, chess.A1)
    
    # Test: IDM-FM-10
    # Description: Test an invalid previous square input that is greater than 63 in chess960.
    def test_find_move_invalid_from_square_greater(self):
        self.board.chess960 = True
        with self.assertRaises(IndexError):
            self.board.find_move(64, chess.H8)

    # # Test: IDM-FM-11
    # # Description: Test an invalid to_square input that is below 0 in standard chess.
    def test_find_move_invalid_to_square_below(self):
        with self.assertRaises(chess.IllegalMoveError):
            self.board.find_move(chess.A1, -1)
    
    # # Test: IDM-FM-12
    # # Description: Test an invalid to_square input that is greater than 63 in chess960.
    def test_find_move_invalid_to_square_greater(self):
        self.board.chess960 = True
        with self.assertRaises(IndexError):
            self.board.find_move(chess.H8, 64)
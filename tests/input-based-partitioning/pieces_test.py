import chess
import unittest

class PiecesTest(unittest.TestCase):
    
    def setUp(self):
        self.board = chess.Board()
    
    # Test: IDM-PC-01
    # Description: Test that white pawns are present in multiple squares.
    def test_piece_pawn_white_multiple(self):
        self.assertEqual(self.board.pieces(chess.PAWN, chess.WHITE), chess.SquareSet(chess.BB_RANK_2))
        
    # Test: IDM-PC-02
    # Description: Test that black knight is present on exactly one square.
    def test_piece_knight_black_one(self):
        board = chess.Board("r1bqkb1r/pppp1Qpp/5n2/4p3/2B1P3/8/PPPP2PP/RNB1K2R b KQkq - 0 4")
        self.assertEqual(board.pieces(chess.KNIGHT, chess.BLACK), chess.SquareSet(chess.BB_F6))
    
    # Test: IDM-PC-03
    # Description: Test that white bishops are absent from the board.
    def test_piece_bishop_white_none(self):
        board = chess.Board("r1bqkb1r/pppp1Qpp/5n2/4p3/4P3/8/PPP3PP/RN2K2R b KQkq - 0 4")
        self.assertEqual(board.pieces(chess.BISHOP, chess.WHITE), chess.SquareSet(chess.BB_EMPTY))
    
    # Test: IDM-PC-04
    # Description: Test that black rooks are present in multiple squares.
    def test_piece_rook_black_multiple(self):
        self.assertEqual(self.board.pieces(chess.ROOK, chess.BLACK), chess.SquareSet([chess.A8, chess.H8]))
    
    # Test: IDM-PC-05
    # Description: Test that white queen is present on exactly one square.
    def test_piece_queen_white_one(self):
        self.assertEqual(self.board.pieces(chess.QUEEN, chess.WHITE), chess.SquareSet(chess.BB_D1))
    
    # Test: IDM-PC-06
    # Description: Test that black king is present on exactly one square.
    def test_piece_king_black_one(self):
        self.assertEqual(self.board.pieces(chess.KING, chess.BLACK), chess.SquareSet(chess.BB_E8))
    
    # Test: IDM-PC-07
    # Description: Test that black pawns are absent from the board.
    def test_piece_pawn_black_none(self):
        board = chess.Board("r1bqkb1r/8/5n2/8/4P3/8/PPP3PP/RN1QK2R b KQkq - 0 4")
        self.assertEqual(board.pieces(chess.PAWN, chess.BLACK), chess.SquareSet(chess.BB_EMPTY))
    
    # Test: IDM-PC-08
    # Description: Test that white knights are present in multiple squares.
    def test_piece_knight_white_multiple(self):
        self.assertEqual(self.board.pieces(chess.KNIGHT, chess.WHITE), chess.SquareSet([chess.B1, chess.G1]))
    
    # Test: IDM-PC-09
    # Description: Test that black bishop is present on exactly one square.
    def test_piece_bishop_black_one(self):
        board = chess.Board("r1bqk2r/8/5n2/8/4P3/8/PPP3PP/RN1QK2R b KQkq - 0 4")
        self.assertEqual(board.pieces(chess.BISHOP, chess.BLACK), chess.SquareSet(chess.BB_C8))
    
    # Test: IDM-PC-10
    # Description: Test that white rooks are absent from the board.
    def test_piece_rook_white_none(self):
        board = chess.Board("r1bqk2r/8/5n2/8/4P3/8/PPP3PP/1N1QK3 b KQkq - 0 4")
        self.assertEqual(board.pieces(chess.ROOK, chess.WHITE), chess.SquareSet(chess.BB_EMPTY))
    
    # Test: IDM-PC-11
    # Description: Test that black queen is present on multiple squares.
    def test_piece_queen_black_multiple(self):
        board = chess.Board("rqbqk2r/8/5n2/8/4P3/8/PPP3PP/1N1QK3 b KQkq - 0 4")
        self.assertEqual(board.pieces(chess.QUEEN, chess.BLACK), chess.SquareSet([chess.B8, chess.D8]))
    
    # Test: IDM-PC-12
    # Description: Test that white king is absent on the board.
    def test_piece_king_white_none(self):
        board = chess.Board("rqbqk2r/8/5n2/8/4P3/8/PPP3PP/1N1Q4 b KQkq - 0 4")
        self.assertEqual(board.pieces(chess.KING, chess.WHITE), chess.SquareSet(chess.BB_EMPTY))
    
    # Test: IDM-PC-13
    # Description: Test an invalid input for piece type with valid color.
    def test_piece_invalid_piece_white(self):
        with self.assertRaises(AssertionError):
            self.board.pieces(7, chess.WHITE)
    
    # Test: IDM-PC-14
    # Description: Test a valid piece type with an invalid color.
    def test_piece_pawn_invalid_color(self):
        with self.assertRaises(IndexError):
            self.board.pieces(chess.PAWN, 2)
    
    # Test: IDM-PC-15
    # Description: Test both an invalid piece type and invalid color.
    def test_piece_invalid(self):
        with self.assertRaises(AssertionError):
            self.board.pieces("pawn", "black")
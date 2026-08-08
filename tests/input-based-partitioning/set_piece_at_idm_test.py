import unittest
import chess
from chess import BaseBoard

class TestBaseBoardSP(unittest.TestCase):
    """
    Test suite for BaseBoard.set_piece_at using Input Domain Modeling.
    Naming Scheme: IDM-SP-[TestCaseNumber]
    """

    def setUp(self):
        """Initializes a fresh BaseBoard before every test case for isolation."""
        self.board = BaseBoard()

    def test_IDM_SP_01(self):
        """IDM-SP-01: Test placing a piece on an empty interior square."""
        self.board.clear_board()
        piece = chess.Piece(chess.QUEEN, chess.WHITE)
        self.board.set_piece_at(chess.D4, piece)
        self.assertEqual(self.board.piece_at(chess.D4), piece)

    def test_IDM_SP_02(self):
        """IDM-SP-02: Test removing a piece from an occupied interior square."""
        self.board.clear_board()
        piece = chess.Piece(chess.QUEEN, chess.WHITE)
        self.board.set_piece_at(chess.D4, piece)
        self.board.set_piece_at(chess.D4, None)
        self.assertIsNone(self.board.piece_at(chess.D4))

    def test_IDM_SP_03(self):
        """IDM-SP-03: Test placing a promoted piece on an empty interior square."""
        self.board.clear_board()
        piece = chess.Piece(chess.QUEEN, chess.WHITE)
        self.board.set_piece_at(chess.D4, piece, promoted=True)
        self.assertEqual(self.board.piece_at(chess.D4), piece)
        self.assertTrue(self.board.promoted & (1 << chess.D4))

    def test_IDM_SP_04(self):
        """IDM-SP-04: Test replacing a piece of the opposite color on a corner square."""
        self.board.clear_board()
        black_piece = chess.Piece(chess.ROOK, chess.BLACK)
        white_piece = chess.Piece(chess.QUEEN, chess.WHITE)
        self.board.set_piece_at(chess.A1, black_piece)
        self.board.set_piece_at(chess.A1, white_piece)
        self.assertEqual(self.board.piece_at(chess.A1), white_piece)

    def test_IDM_SP_05(self):
        """IDM-SP-05: Test replacing a piece of the same color on an edge square."""
        self.board.clear_board()
        pawn = chess.Piece(chess.PAWN, chess.WHITE)
        queen = chess.Piece(chess.QUEEN, chess.WHITE)
        self.board.set_piece_at(chess.A2, pawn)
        self.board.set_piece_at(chess.A2, queen)
        self.assertEqual(self.board.piece_at(chess.A2), queen)

    def test_IDM_SP_06(self):
        """IDM-SP-06: Test an invalid square index below 0."""
        piece = chess.Piece(chess.QUEEN, chess.WHITE)
        with self.assertRaises((IndexError, ValueError)):
            self.board.set_piece_at(-100, piece)

    def test_IDM_SP_07(self):
        """IDM-SP-07: Test an invalid square index above 63."""
        piece = chess.Piece(chess.QUEEN, chess.WHITE)
        with self.assertRaises((IndexError, ValueError)):
            self.board.set_piece_at(64, piece)

    def test_IDM_SP_08(self):
        """IDM-SP-08: Test replacing an existing piece with a promoted piece."""
        self.board.clear_board()
        black_piece = chess.Piece(chess.ROOK, chess.BLACK)
        white_piece = chess.Piece(chess.QUEEN, chess.WHITE)
        self.board.set_piece_at(chess.D4, black_piece)
        self.board.set_piece_at(chess.D4, white_piece, promoted=True)
        self.assertEqual(self.board.piece_at(chess.D4), white_piece)
        self.assertTrue(self.board.promoted & (1 << chess.D4))

if __name__ == "__main__":
    unittest.main()

import unittest
import chess
from chess import BaseBoard

class TestBaseBoardPN(unittest.TestCase):
    """
    Test suite for BaseBoard.is_pinned using Input Domain Modeling.
    Naming Scheme: IDM-PN-[TestCaseNumber]
    """

    def setUp(self):
        """Initializes a fresh BaseBoard before every test case for isolation."""
        self.board = BaseBoard()

    def test_IDM_PN_01(self):
        """IDM-PN-01: Test a valid interior square that is absolutely pinned."""
        self.board.clear_board()
        self.board.set_piece_at(chess.E1, chess.Piece(chess.KING, chess.WHITE))
        self.board.set_piece_at(chess.E2, chess.Piece(chess.PAWN, chess.WHITE))
        self.board.set_piece_at(chess.E3, chess.Piece(chess.ROOK, chess.BLACK))
        self.assertTrue(self.board.is_pinned(chess.WHITE, chess.E2))

    def test_IDM_PN_02(self):
        """IDM-PN-02: Test a valid interior square with no opponent slider on the line."""
        self.board.clear_board()
        self.board.set_piece_at(chess.E1, chess.Piece(chess.KING, chess.WHITE))
        self.board.set_piece_at(chess.E2, chess.Piece(chess.PAWN, chess.WHITE))
        self.assertFalse(self.board.is_pinned(chess.WHITE, chess.E2))

    def test_IDM_PN_03(self):
        """IDM-PN-03: Test a valid interior square where the slider is blocked by another piece."""
        self.board.clear_board()
        self.board.set_piece_at(chess.E1, chess.Piece(chess.KING, chess.WHITE))
        self.board.set_piece_at(chess.E2, chess.Piece(chess.PAWN, chess.WHITE))
        self.board.set_piece_at(chess.E3, chess.Piece(chess.BISHOP, chess.WHITE))
        self.board.set_piece_at(chess.E4, chess.Piece(chess.ROOK, chess.BLACK))
        self.assertFalse(self.board.is_pinned(chess.WHITE, chess.E2))

    def test_IDM_PN_04(self):
        """IDM-PN-04: Test an invalid color input."""
        with self.assertRaises(IndexError):
            self.board.is_pinned(2, chess.E2)

    def test_IDM_PN_05(self):
        """IDM-PN-05: Test an invalid square index."""
        with self.assertRaises((IndexError, ValueError)):
            self.board.is_pinned(chess.WHITE, 64)

    def test_IDM_PN_06(self):
        """IDM-PN-06: Test behavior when the king of the specified color is absent."""
        self.board.clear_board()
        self.board.set_piece_at(chess.E2, chess.Piece(chess.PAWN, chess.WHITE))
        self.board.set_piece_at(chess.E3, chess.Piece(chess.ROOK, chess.BLACK))
        self.assertFalse(self.board.is_pinned(chess.WHITE, chess.E2))

    def test_IDM_PN_07(self):
        """IDM-PN-07: Test a valid corner square that cannot be absolutely pinned."""
        self.board.clear_board()
        self.board.set_piece_at(chess.A1, chess.Piece(chess.PAWN, chess.BLACK))
        self.board.set_piece_at(chess.B2, chess.Piece(chess.KING, chess.BLACK))
        self.board.set_piece_at(chess.C3, chess.Piece(chess.BISHOP, chess.WHITE))
        self.assertFalse(self.board.is_pinned(chess.BLACK, chess.A1))

    def test_IDM_PN_08(self):
        """IDM-PN-08: Test a valid edge square that is absolutely pinned."""
        self.board.clear_board()
        self.board.set_piece_at(chess.E8, chess.Piece(chess.KING, chess.BLACK))
        self.board.set_piece_at(chess.D8, chess.Piece(chess.PAWN, chess.BLACK))
        self.board.set_piece_at(chess.A8, chess.Piece(chess.ROOK, chess.WHITE))
        self.assertTrue(self.board.is_pinned(chess.BLACK, chess.D8))

if __name__ == "__main__":
    unittest.main()

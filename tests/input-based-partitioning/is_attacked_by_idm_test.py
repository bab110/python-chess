import unittest
import chess
from chess import BaseBoard

class TestBaseBoardAT(unittest.TestCase):
    """
    Test suite for BaseBoard.is_attacked_by using Input Domain Modeling.
    Naming Scheme: IDM-AT-[TestCaseNumber]
    """

    def setUp(self):
        """Initializes a fresh BaseBoard before every test case for isolation."""
        self.board = BaseBoard()

    def test_IDM_AT_01(self):
        """IDM-AT-01: Test white knight attacking an interior square."""
        self.board.clear_board()
        self.board.set_piece_at(chess.F3, chess.Piece(chess.KNIGHT, chess.WHITE))
        self.assertTrue(self.board.is_attacked_by(chess.WHITE, chess.D4))

    def test_IDM_AT_02(self):
        """IDM-AT-02: Test black rook attacking an edge square but blocked."""
        self.board.clear_board()
        self.board.set_piece_at(chess.A1, chess.Piece(chess.ROOK, chess.BLACK))
        self.board.set_piece_at(chess.A2, chess.Piece(chess.PAWN, chess.WHITE))
        self.assertFalse(self.board.is_attacked_by(chess.BLACK, chess.A3))

    def test_IDM_AT_03(self):
        """IDM-AT-03: Test a corner square with no attackers."""
        self.board.clear_board()
        self.assertFalse(self.board.is_attacked_by(chess.WHITE, chess.A1))

    def test_IDM_AT_04(self):
        """IDM-AT-04: Test an invalid color input."""
        with self.assertRaises(IndexError):
            self.board.is_attacked_by(2, chess.D4)

    def test_IDM_AT_05(self):
        """IDM-AT-05: Test an invalid square index."""
        with self.assertRaises((IndexError, ValueError)):
            self.board.is_attacked_by(chess.WHITE, 64)

    def test_IDM_AT_06(self):
        """IDM-AT-06: Test X-ray attack using the occupied parameter."""
        self.board.clear_board()
        self.board.set_piece_at(chess.A1, chess.Piece(chess.ROOK, chess.WHITE))
        self.board.set_piece_at(chess.A2, chess.Piece(chess.PAWN, chess.WHITE))
        
        self.assertFalse(self.board.is_attacked_by(chess.WHITE, chess.A3))
        
        xray_mask = self.board.occupied ^ (1 << chess.A2)
        self.assertTrue(self.board.is_attacked_by(chess.WHITE, chess.A3, occupied=xray_mask))

    def test_IDM_AT_07(self):
        """IDM-AT-07: Test multiple attackers on an interior square."""
        self.board.clear_board()
        self.board.set_piece_at(chess.F6, chess.Piece(chess.KNIGHT, chess.BLACK))
        self.board.set_piece_at(chess.C6, chess.Piece(chess.KNIGHT, chess.BLACK))
        self.assertTrue(self.board.is_attacked_by(chess.BLACK, chess.D5))

    def test_IDM_AT_08(self):
        """IDM-AT-08: Test a white pawn attacking an interior square."""
        self.board.clear_board()
        self.board.set_piece_at(chess.E3, chess.Piece(chess.PAWN, chess.WHITE))
        self.assertTrue(self.board.is_attacked_by(chess.WHITE, chess.D4))

if __name__ == "__main__":
    unittest.main()

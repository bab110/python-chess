import unittest
import chess
from chess import BaseBoard

class TestBaseBoardPM(unittest.TestCase):
    """
    Test suite for BaseBoard.pieces_mask using Input Domain Modeling.
    Naming Scheme: IDM-PM-[TestCaseNumber]
    """

    def setUp(self):
        """Initializes a fresh BaseBoard before every test case for isolation."""
        self.board = BaseBoard()

    def test_IDM_PM_01(self):
        """IDM-PM-01: Test white pawns present in multiple squares."""
        mask = self.board.pieces_mask(chess.PAWN, chess.WHITE)
        self.assertEqual(bin(mask).count('1'), 8)

    def test_IDM_PM_02(self):
        """IDM-PM-02: Test black knights present in multiple squares."""
        mask = self.board.pieces_mask(chess.KNIGHT, chess.BLACK)
        self.assertEqual(bin(mask).count('1'), 2)

    def test_IDM_PM_03(self):
        """IDM-PM-03: Test white bishops present in multiple squares."""
        mask = self.board.pieces_mask(chess.BISHOP, chess.WHITE)
        self.assertEqual(bin(mask).count('1'), 2)

    def test_IDM_PM_04(self):
        """IDM-PM-04: Test black rooks present in multiple squares."""
        mask = self.board.pieces_mask(chess.ROOK, chess.BLACK)
        self.assertEqual(bin(mask).count('1'), 2)

    def test_IDM_PM_05(self):
        """IDM-PM-05: Test white queen present on exactly one square."""
        mask = self.board.pieces_mask(chess.QUEEN, chess.WHITE)
        self.assertEqual(bin(mask).count('1'), 1)

    def test_IDM_PM_06(self):
        """IDM-PM-06: Test black king present on exactly one square."""
        mask = self.board.pieces_mask(chess.KING, chess.BLACK)
        self.assertEqual(bin(mask).count('1'), 1)

    def test_IDM_PM_07(self):
        """IDM-PM-07: Test white king absent from the board."""
        self.board.remove_piece_at(chess.E1)
        mask = self.board.pieces_mask(chess.KING, chess.WHITE)
        self.assertEqual(mask, 0)

    def test_IDM_PM_08(self):
        """IDM-PM-08: Test black queen present on exactly one square."""
        mask = self.board.pieces_mask(chess.QUEEN, chess.BLACK)
        self.assertEqual(bin(mask).count('1'), 1)

    def test_IDM_PM_09(self):
        """IDM-PM-09: Test an invalid piece type with a valid color."""
        with self.assertRaises(AssertionError):
            self.board.pieces_mask(99, chess.WHITE)

    def test_IDM_PM_10(self):
        """IDM-PM-10: Test a valid piece type with an invalid color."""
        with self.assertRaises(IndexError):
            self.board.pieces_mask(chess.PAWN, 2)

if __name__ == "__main__":
    unittest.main()

import unittest
import chess
from chess import BaseBoard

class TestBaseBoardRP(unittest.TestCase):
    """
    Test suite for BaseBoard.remove_piece_at using Input Domain Modeling.
    Naming Scheme: IDM-RP-[TestCaseNumber]
    """

    def setUp(self):
        """Initializes a fresh BaseBoard before every test case for isolation."""
        self.board = BaseBoard()

    def test_IDM_RP_01(self):
        """IDM-RP-01: Test removing a piece from an occupied interior square."""
        self.board.clear_board()
        piece = chess.Piece(chess.QUEEN, chess.WHITE)
        self.board.set_piece_at(chess.D4, piece)
        removed = self.board.remove_piece_at(chess.D4)
        self.assertEqual(removed, piece)
        self.assertIsNone(self.board.piece_at(chess.D4))

    def test_IDM_RP_02(self):
        """IDM-RP-02: Test removing a piece from an empty interior square."""
        self.board.clear_board()
        removed = self.board.remove_piece_at(chess.D4)
        self.assertIsNone(removed)

    def test_IDM_RP_03(self):
        """IDM-RP-03: Test removing a piece from an occupied corner square."""
        self.board.clear_board()
        piece = chess.Piece(chess.ROOK, chess.BLACK)
        self.board.set_piece_at(chess.A1, piece)
        removed = self.board.remove_piece_at(chess.A1)
        self.assertEqual(removed, piece)
        self.assertIsNone(self.board.piece_at(chess.A1))

    def test_IDM_RP_04(self):
        """IDM-RP-04: Test removing a piece from an occupied edge square."""
        self.board.clear_board()
        piece = chess.Piece(chess.PAWN, chess.WHITE)
        self.board.set_piece_at(chess.A2, piece)
        removed = self.board.remove_piece_at(chess.A2)
        self.assertEqual(removed, piece)
        self.assertIsNone(self.board.piece_at(chess.A2))

    def test_IDM_RP_05(self):
        """IDM-RP-05: Test removing a piece from an empty corner square."""
        self.board.clear_board()
        removed = self.board.remove_piece_at(chess.A1)
        self.assertIsNone(removed)

    def test_IDM_RP_06(self):
        """IDM-RP-06: Test an invalid square index below 0."""
        with self.assertRaises((IndexError, ValueError)):
            self.board.remove_piece_at(-100)

    def test_IDM_RP_07(self):
        """IDM-RP-07: Test an invalid square index above 63."""
        with self.assertRaises((IndexError, ValueError)):
            self.board.remove_piece_at(64)

if __name__ == "__main__":
    unittest.main()

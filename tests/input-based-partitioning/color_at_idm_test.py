import unittest
import chess
from chess import BaseBoard

class TestBaseBoardCA(unittest.TestCase):
    """
    Test suite for BaseBoard.color_at using Input Domain Modeling.
    Naming Scheme: IDM-CA-[TestCaseNumber]
    """

    def setUp(self):
        """Initializes a fresh BaseBoard before every test case for isolation."""
        self.board = BaseBoard()

    def test_IDM_CA_01(self):
        """IDM-CA-01: Valid interior square occupied by a white piece."""
        self.board.set_piece_at(chess.D4, chess.Piece(chess.PAWN, chess.WHITE))
        self.assertEqual(self.board.color_at(chess.D4), chess.WHITE)

    def test_IDM_CA_02(self):
        """IDM-CA-02: Valid interior square occupied by a black piece."""
        self.board.set_piece_at(chess.D4, chess.Piece(chess.PAWN, chess.BLACK))
        self.assertEqual(self.board.color_at(chess.D4), chess.BLACK)

    def test_IDM_CA_03(self):
        """IDM-CA-03: Valid interior square that is empty."""
        self.board.remove_piece_at(chess.D4)
        self.assertIsNone(self.board.color_at(chess.D4))

    def test_IDM_CA_04(self):
        """IDM-CA-04: Valid corner square occupied by a white piece."""
        self.assertEqual(self.board.color_at(chess.A1), chess.WHITE)

    def test_IDM_CA_05(self):
        """IDM-CA-05: Valid edge square occupied by a black piece."""
        self.board.set_piece_at(chess.A2, chess.Piece(chess.PAWN, chess.BLACK))
        self.assertEqual(self.board.color_at(chess.A2), chess.BLACK)

    def test_IDM_CA_06(self):
        """IDM-CA-06: Valid corner square that is empty."""
        self.board.remove_piece_at(chess.A1)
        self.assertIsNone(self.board.color_at(chess.A1))

    def test_IDM_CA_07(self):
        """IDM-CA-07: Invalid square index above 63."""
        with self.assertRaises((IndexError, ValueError)):
            self.board.color_at(64)

    def test_IDM_CA_08(self):
        """IDM-CA-08: Invalid square index below 0."""
        with self.assertRaises((IndexError, ValueError)):
            self.board.color_at(-100)

if __name__ == "__main__":
    unittest.main()

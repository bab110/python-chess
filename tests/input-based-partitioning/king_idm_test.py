import unittest

import chess
from chess import BaseBoard


class TestBaseBoardKG(unittest.TestCase):
    """
    Test suite for BaseBoard.king using Input Domain Modeling.
    Naming Scheme: IDM-KG-[TestCaseNumber]
    """

    def setUp(self):
        """Initializes a fresh BaseBoard before every test case for isolation."""
        self.board = BaseBoard()

    def test_IDM_KG_01(self):
        """IDM-KG-01: Test finding the unique white king on a standard board."""
        self.assertEqual(self.board.king(chess.WHITE), chess.E1)

    def test_IDM_KG_02(self):
        """IDM-KG-02: Test finding the unique black king on a standard board."""
        self.assertEqual(self.board.king(chess.BLACK), chess.E8)

    def test_IDM_KG_03(self):
        """IDM-KG-03: Test behavior when no kings of the specified color exist."""
        self.board.remove_piece_at(chess.E1)
        self.assertIsNone(self.board.king(chess.WHITE))

    def test_IDM_KG_04(self):
        """IDM-KG-04: Test behavior when multiple kings of the specified color exist."""

        self.board.set_piece_at(chess.D4, chess.Piece(chess.KING, chess.WHITE))
        self.assertIsNone(self.board.king(chess.WHITE))

    def test_IDM_KG_05(self):
        """IDM-KG-05: Test behavior when the only king present is a promoted king."""
        # Per documentation in BaseBoard.king, this test should pass. However this fails due to  _effective_promoted sending `BB_EMPTY`.
        self.board.clear_board()
        self.board.set_piece_at(
            chess.E1, chess.Piece(chess.KING, chess.WHITE), promoted=True
        )

        self.assertIsNone(self.board.king(chess.WHITE))

    def test_IDM_KG_06(self):
        """IDM-KG-06: Test an invalid color input."""
        with self.assertRaises(IndexError):
            self.board.king(2)


if __name__ == "__main__":
    unittest.main()

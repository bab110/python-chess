import unittest

import chess
from chess import BaseBoard


class TestBaseBoardPT(unittest.TestCase):
    """
    Test suite for BaseBoard.piece_type_at using Input Domain Modeling.
    Naming Scheme: IDM-PT-[TestCaseNumber]
    """

    def setUp(self):
        """Initializes a fresh BaseBoard before every test case for isolation."""
        self.board = BaseBoard()

    def test_IDM_PT_01(self):
        """IDM-PT-01: Valid corner square occupied by a rook."""
        self.assertEqual(self.board.piece_type_at(chess.A1), chess.ROOK)

    def test_IDM_PT_02(self):
        """IDM-PT-02: Valid interior square that is empty."""
        self.assertIsNone(self.board.piece_type_at(chess.D4))

    def test_IDM_PT_03(self):
        """IDM-PT-03: Invalid square index above 63."""
        with self.assertRaises((IndexError, ValueError)):
            self.board.piece_type_at(64)

    def test_IDM_PT_04(self):
        """IDM-PT-04: Invalid square index below 0."""
        with self.assertRaises((IndexError, ValueError)):
            self.board.piece_type_at(-100)

    def test_IDM_PT_05(self):
        """IDM-PT-05: Valid edge square occupied by a pawn."""
        self.board.set_piece_at(chess.A2, chess.Piece(chess.PAWN, chess.WHITE))
        self.assertEqual(self.board.piece_type_at(chess.A2), chess.PAWN)

    def test_IDM_PT_06(self):
        """IDM-PT-06: Valid interior square occupied by a knight."""
        self.board.set_piece_at(chess.D4, chess.Piece(chess.KNIGHT, chess.WHITE))
        self.assertEqual(self.board.piece_type_at(chess.D4), chess.KNIGHT)

    def test_IDM_PT_07(self):
        """IDM-PT-07: Valid interior square occupied by a bishop."""
        self.board.set_piece_at(chess.D4, chess.Piece(chess.BISHOP, chess.WHITE))
        self.assertEqual(self.board.piece_type_at(chess.D4), chess.BISHOP)

    def test_IDM_PT_08(self):
        """IDM-PT-08: Valid interior square occupied by a queen."""
        self.board.set_piece_at(chess.D4, chess.Piece(chess.QUEEN, chess.WHITE))
        self.assertEqual(self.board.piece_type_at(chess.D4), chess.QUEEN)

    def test_IDM_PT_09(self):
        """IDM-PT-09: Valid interior square occupied by a king."""
        self.board.set_piece_at(chess.D4, chess.Piece(chess.KING, chess.WHITE))
        self.assertEqual(self.board.piece_type_at(chess.D4), chess.KING)

    def test_IDM_PT_10(self):
        """IDM-PT-10: Valid corner square that is empty."""
        self.board.remove_piece_at(chess.A1)
        self.assertIsNone(self.board.piece_type_at(chess.A1))


if __name__ == "__main__":
    unittest.main()

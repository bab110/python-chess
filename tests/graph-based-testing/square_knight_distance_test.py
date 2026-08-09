import chess
import unittest

class SquareKnightDistanceTest(unittest.TestCase):
    
    # Test: GBT-SD-01
    # Description: Square a is next to square b horizontally, with a being bigger than b. 
    # Test path: 1 → 2 → 3
    def test_square_knight_distance_one(self):
        self.assertEqual(chess.square_knight_distance(chess.A1, chess.B1), 3)
            
    
    # Test: GBT-SD-02
    # Description: Square a is two squares diagonally away from square b, with square a being bigger than b. 
    # Test path: 1 → 2 → 4 → 5
    def test_square_knight_distance_two(self):
        self.assertEqual(chess.square_knight_distance(chess.E5, chess.C3), 4)
        
    # Test: GBT-SD-03
    # Description: Square a is one square diagonally away from square b and square a or square b is a corner square.
    # Test path: 1 → 2 → 4 → 6 → 7 → 8
    def test_square_knight_distance_three(self):
        self.assertEqual(chess.square_knight_distance(chess.B2, chess.A1), 4)
        self.assertEqual(chess.square_knight_distance(chess.H8, chess.G7), 4)
        
    # Test: GBT-SD-04
    # Description: Square a is one square diagonally away from square b.
    # Test path: 1 → 2 → 4 → 6 → 7 → 9
    def test_square_knight_distance_four(self):
        self.assertEqual(chess.square_knight_distance(chess.G7, chess.F6), 2)
        
    # Test: GBT-SD-05
    # Description: Square b is a smaller rank or file than that of square a.
    # Test path: 1 → 2 → 4 → 6 → 7 → 9
    def test_square_knight_distance_five(self):
        self.assertEqual(chess.square_knight_distance(chess.E8, chess.C1), 5)
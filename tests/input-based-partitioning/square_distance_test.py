import chess
import unittest

class SquareDistanceTest(unittest.TestCase):
    
    # Test: IDM-SD-01
    # Description: Test both a valid Square a and Square b with default
    def test_square_distance(self):
        self.assertEqual(chess.square_distance(chess.A1, chess.H8), 7)
        self.assertEqual(chess.square_distance(0, 63), 7)
    
    # Test: IDM-SD-02
    # Description: Test an invalid Square a that is below 0 
    def test_square_distance_invalid_low_a(self):
        self.assertEqual(chess.square_distance(-1, chess.A1), 7)
        self.assertEqual(chess.square_distance(-1, 0), 7)
        
    # Test: IDM-SD-03
    # Description: Test an invalid Square a that is above chess.H8 or 63
    def test_square_distance_invalid_high_a(self):
        self.assertEqual(chess.square_distance(64, chess.H8), 7)
        with self.assertRaises(AttributeError):
            chess.square_distance(chess.H9, chess.H8)

    # Test: IDM-SD-04
    # Description: Test an invalid Square b that is below 0
    def test_square_distance_invalid_low_b(self):
        self.assertEqual(chess.square_distance(chess.A1, -1), 7)
        self.assertEqual(chess.square_distance(0, -1), 7)
        
    # Test: IDM-SD-05
    # Description: Test an invalid Square b that is above chess.H8 or 63
    def test_square_distance_invalid_high_b(self):
        self.assertEqual(chess.square_distance(chess.H8, 64), 7)
        with self.assertRaises(AttributeError):
            chess.square_distance(chess.H8, chess.H9)
            
    # Test: IDM-SD-06
    # Description: Test a valid Square a and Square b where they have the same square
    def test_square_distance_same_square(self):
        self.assertEqual(chess.square_distance(chess.D4, chess.D4), 0)
        self.assertEqual(chess.square_distance(27, 27), 0)
       
    
    # Test: IDM-SD-07
    # Description: Test a valid Square a and Square b where they have the same rank
    def test_square_distance_same_rank(self):
        self.assertEqual(chess.square_distance(chess.A1, chess.H1), 7)
        self.assertEqual(chess.square_distance(0, 7), 7)
           
    
    # Test: IDM-SD-08
    # Description: Test a valid Square a and Square b where they have the same file
    def test_square_distance_same_file(self):
        self.assertEqual(chess.square_distance(chess.A1, chess.A8), 7)
        self.assertEqual(chess.square_distance(0, 56), 7)
           
    
    # Test: IDM-SD-09
    # Description: Test a valid Square a and Square b where dx > dy
    def test_square_distance_dx_greater(self):
        self.assertEqual(chess.square_distance(chess.A1, chess.H3), 7)
        self.assertEqual(chess.square_distance(0, 23), 7)
           

    # Test: IDM-SD-10
    # Description: Test a valid Square a and Square b where dx < dy
    def test_square_distance_dy_greater(self):
        self.assertEqual(chess.square_distance(chess.A1, chess.C8), 7)
        self.assertEqual(chess.square_distance(0, 58), 7)
    
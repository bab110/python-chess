import chess

class LandmarkTour():
    
    # Test Case: EXP-LM-01
    # Description: Setup chess board, pushed the move “e2e4”, peeked at the last move, then popped the last move.
    
    # Setup the chess board
    board = chess.Board()
    
    print("Initial board:")
    print(board)
    
    move1 = chess.Move.from_uci("e2e4")
    board.push(move1)
    
    print("After push 1, peek:", board.peek())
    
    print("Pop:", board.pop())
    
    print("Current board:")
    print(board)
    
    # Test Case: EXP-LM-02
    # Description: Pushed the move “e2e4”, peeked at last move, pushed move “e7e5”, peeked at last move, popped the last move, peeked at last move, then popped the last move.
    
    board.push(move1)
    print("After push 1, peek:", board.peek())
    
    move2 = chess.Move.from_uci("e7e5")
    
    board.push(move2)
    print("After push 2, peek:", board.peek())
    
    print("Board after moves:")
    print(board)
    
    print("Pop:", board.pop())
    print("After pop, peek:", board.peek())
    
    print("Pop again:", board.pop())
    
    print("Current board:")
    print(board)
    
    # Test Case: EXP-LM-03
    # Description: Setup chess board, pushed the move “c3c4”, pushed the move “b5c4”, checked the board for capture, pushed the move “d2c4”, check the board for capture, pushed the move “b8a6”, pushed the move “c4a5”, check the board for capture, popped the last move, peeked after pop, popped the last move, then peeked after pop.
    
    board = chess.Board("rn1qrbk1/2pb1pp1/3p1n1p/pp1Pp3/4P3/1BP2N1P/PP1N1PP1/R1BQR1K1 w KQkq - 0 1")
    
    print("Current board:")
    print(board)
    
    move4 = chess.Move.from_uci("c3c4")
    board.push(move4)
    
    move4 = chess.Move.from_uci("b5c4")
    board.push(move4)
    
    print("First Capture Move:")
    print(board)
    
    move5 = chess.Move.from_uci("d2c4")
    board.push(move5)
    
    print("Second Capture Move:")
    print(board)
    
    move6 = chess.Move.from_uci("b8a6")
    board.push(move6)
    
    move7 = chess.Move.from_uci("c4a5")
    board.push(move7)
    
    print("Third Capture Move:")
    print(board)
    
    print("Pop:", board.pop())
    print("After pop, peek:", board.peek())
    
    print("Pop again:", board.pop())
    print("After pop, peek:", board.peek())
    
    print("Current Board:")
    print(board)
    
    
    # Test Case: EXP-LM-04
    # Description: Setup chess board, pushed the move “f4e5”, pushed the move “g2g1q”, peeked at last move, pop the last move, then peek after pop.
    
    print("Test Case: EXP-LM-04")
    board = chess.Board("r1bqkb1r/pppp1p1p/2n2n2/6B1/3P1P2/2P5/PP2Q1p1/RN2KB1R w KQkq - 0 1")
    
    print("Current Board:")
    print(board)
    
    move8 = chess.Move.from_uci("f4e5")
    board.push(move8)
    
    move8 = chess.Move.from_uci("g2g1q")
    board.push(move8)
    
    print("After push, peek:", board.peek())
    
    print("Current Board:")
    print(board)
    
    print("Pop:", board.pop())
    print("After pop, peek:", board.peek())
    
    print("Current Board:")
    print(board)
    
    # Test Case: EXP-LM-05
    # Description: Setup chess board, pop the last move, then peek the last move.
    
    board = chess.Board()
    
    # Raises: IndexError when the move stack is empty
    
    # print("Pop:", board.pop())
    # print("After pop, peek:", board.peek())
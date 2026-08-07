Feature: As a developer, I want the engine to verify that a move is legal

Scenario Outline: Verify that a given move is legal for the given board state
    Given The board state is "<board_FEN>"
    When The given uci move is "<uci_string>"
    Then The move should be evaluated as "<legality>"

    Examples: Scenario Table

        | fen                                                                 | uci_move | is_legal |
        | rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1            | e2e4     | legal    |
        | rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR w KQkq - 0 1            | e2e5     | illegal  |
        | 4k3/8/8/8/8/4r3/4K3/8 w - - 0 1                                     | e2e3     | illegal  |
        | r1bqk1nr/pppp1ppp/2n5/4p3/1b2P3/5N2/PPPP1PPP/RNBQKB1R w KQkq - 2 4  | f3e5     | illegal  |
        | 4k3/8/4r3/8/4K3/4P3/8/8 w - - 0 1                                   | e3e4     | illegal  |  
        | r3k2r/8/8/8/8/8/8/R3K2R w KQkq - 0 1                                | e1g1     | illegal  |
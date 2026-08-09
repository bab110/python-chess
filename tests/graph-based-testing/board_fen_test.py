import chess


def test_gbt_bf_01():
    """
    GBT-BF-01

    Objective:
        Cover the branch where:
        - piece does not exist (N5 = No)
        - square is not on file H (N17 = No)

    Expected behavior:
        The function encounters an empty square,
        increments the empty counter, and continues
        processing without entering the piece-handling logic.
    """

    board = chess.Board.empty()

    result = board.board_fen()

    # Entire board is empty
    expected = "8/8/8/8/8/8/8/8"

    assert result == expected


def test_gbt_bf_02():
    """
    GBT-BF-02

    Objective:
        Cover the branch where:
        - piece exists (N5 = Yes)
        - no pending empty squares (N7 = No)
        - promoted is None (N10 = Yes)
        - square is not promoted (N15 = No)
        - square is not on file H (N17 = No)

    Expected behavior:
        The piece symbol is appended directly to the FEN
        without flushing an empty count or adding a
        promotion marker.
    """

    board = chess.Board.empty()

    # Place a white rook on A8 (first square visited)
    board.set_piece_at(chess.A8, chess.Piece(chess.ROOK, chess.WHITE))

    result = board.board_fen()

    expected = "R7/8/8/8/8/8/8/8"

    assert result == expected


def test_gbt_bf_03():
    """
    GBT-BF-03

    Objective:
        Cover the branch where:
        - empty squares are accumulated before a piece (N7 = Yes)
        - the empty count is flushed (N8)
        - promoted is None (N10 = Yes)
        - the piece is marked as promoted (N15 = Yes)
        - promotion marker '~' is appended (N16)

    Expected behavior:
        The FEN should contain:
        - '1' for the empty A8 square
        - 'Q' for the queen on B8
        - '~' indicating the piece is promoted
    """

    board = chess.Board.empty()

    # Place a queen on B8
    board.set_piece_at(chess.B8, chess.Piece(chess.QUEEN, chess.WHITE))

    # Mark B8 as promoted
    board.promoted = chess.BB_SQUARES[chess.B8]

    result = board.board_fen(promoted=board.promoted)

    expected = "1Q~6/8/8/8/8/8/8/8"

    assert result == expected


def test_gbt_bf_04():
    """
    GBT-BF-04

    Objective:
        Cover the branch where:
        - promoted is not None (N10 = No)
        - promoted evaluates to True (N11 = Yes)
        - self.promoted is used as the promotion mask (N13)
        - current square is not promoted (N15 = No)

    Expected behavior:
        The piece symbol is appended to the FEN,
        but no promotion marker ('~') is added because
        the square is not included in board.promoted.
    """

    board = chess.Board.empty()

    # Place a white rook on A8
    board.set_piece_at(chess.A8, chess.Piece(chess.ROOK, chess.WHITE))

    # No squares marked as promoted
    board.promoted = chess.BB_EMPTY

    result = board.board_fen(promoted=True)

    expected = "R7/8/8/8/8/8/8/8"

    assert result == expected


def test_gbt_bf_05():
    """
    GBT-BF-05

    Objective:
        Cover the branch where:
        - promoted is not None (N10 = No)
        - promoted evaluates to False (N11 = No)
        - BB_EMPTY is used as the promotion mask (N14)
        - current square is not considered promoted (N15 = No)

    Expected behavior:
        Even though the piece is marked as promoted on the board,
        no '~' marker should be added because promoted=False causes
        the function to use BB_EMPTY as the promotion mask.
    """

    board = chess.Board.empty()

    # Place a white queen on A8
    board.set_piece_at(chess.A8, chess.Piece(chess.QUEEN, chess.WHITE))

    # Mark A8 as promoted
    board.promoted = chess.BB_SQUARES[chess.A8]

    result = board.board_fen(promoted=False)

    expected = "Q7/8/8/8/8/8/8/8"

    assert result == expected


def test_gbt_bf_06():
    """
    GBT-BF-06

    Objective:
        Cover the branch where:
        - current square is on file H (N17 = Yes)
        - there are pending empty squares (N18 = Yes)
        - empty count is flushed (N19)
        - square is not H1 (N20 = Yes)
        - rank separator '/' is appended (N21)

    Expected behavior:
        When the loop reaches H8, the accumulated count of
        eight empty squares is flushed and a rank separator
        is appended.
    """

    board = chess.Board.empty()

    result = board.board_fen()

    expected = "8/8/8/8/8/8/8/8"

    assert result == expected


def test_gbt_bf_07():
    """
    GBT-BF-07

    Objective:
        Cover the branch where:
        - current square is on file H (N17 = Yes)
        - there are no pending empty squares (N18 = No)
        - square is not H1 (N20 = Yes)
        - rank separator '/' is appended (N21)

    Expected behavior:
        When processing H8, there are no pending empty
        squares to flush because the preceding seven
        empty squares have already been emitted as part
        of the rank representation. The function should
        append the '/' rank separator.
    """

    board = chess.Board.empty()

    # Place a rook on H8 (end of first rank processed)
    board.set_piece_at(chess.H8, chess.Piece(chess.ROOK, chess.WHITE))

    result = board.board_fen()

    expected = "7R/8/8/8/8/8/8/8"

    assert result == expected


def test_gbt_bf_08():
    """
    GBT-BF-08

    Objective:
        Cover the branch where:
        - current square is on file H (N17 = Yes)
        - there are no pending empty squares (N18 = No)
        - current square is H1 (N20 = No)

    Expected behavior:
        When processing H1, the function should not append
        a '/' because H1 is the last square on the board.
    """

    board = chess.Board.empty()

    # Place a rook on H1 (last square processed)
    board.set_piece_at(chess.H1, chess.Piece(chess.ROOK, chess.WHITE))

    result = board.board_fen()

    expected = "8/8/8/8/8/8/8/7R"

    assert result == expected


def test_gbt_bf_09():
    """
    GBT-BF-09

    Objective:
        Cover the loop termination and return path:
        - no more squares remain to process (N3 = No)
        - return statement executes (N22)
        - function exits (N24)

    Expected behavior:
        After all squares have been processed, the
        function returns the generated board FEN string.
    """

    board = chess.Board()

    result = board.board_fen()

    expected = "rnbqkbnr/pppppppp/8/8/8/8/PPPPPPPP/RNBQKBNR"

    assert result == expected
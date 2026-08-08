import chess
from behave import given, when, then

@given('the board state is "{board_FEN}"')
def the_board_state_is_set(context, board_FEN):
    context.board_FEN = board_FEN.strip()
    context.board = chess.Board(context.board_FEN)

@when('the uci move given is "{uci_string}"')
def the_uci_string_is_checked(context, uci_string):
    try:
        context.move = chess.Move.from_uci(uci_string)
        context.is_valid_syntax = True
    except ValueError:
        context.move = None
        context.is_valid_syntax = False

@then('the move should be evaluated as "{legality}"')
def the_legality_is_evaluated(context, legality):

    # Checking a valid move that was given
    if legality == "legal":
        assert context.is_valid_syntax, "UCI string syntax is invalid"
        assert context.move in context.board.legal_moves, f"Move {context.move.uci()} should be legal"
    else:  # Checking invalid move that was given
        if context.is_valid_syntax:
            assert context.move not in context.board.legal_moves, f"Move {context.move.uci()} should be illegal"
        else:
            # An invalid syntax UCI string is inherently illegal
            assert True
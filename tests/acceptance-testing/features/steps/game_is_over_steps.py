import chess
from behave import given, when, then


@given('the_user_has_created_a_board')
def the_user_has_created_a_board(context):
    context.board = chess.Board()

@when('the board state is "{baseboard}"')
def the_board_state_is(context, baseboard):
    context.board = chess.Board(baseboard)
    
@when('the game state is checked')
def the_game_state_is_checked(context):
    context.is_game_over = context.board.is_game_over()
    
@then('game over should return true')
def game_over_returns_true(context):
    assert context.is_game_over == True
    
@then('game over should return false')
def game_over_returns_false(context):
    assert context.is_game_over == False
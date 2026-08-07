import chess
from behave import given, when, then

@given('the engine is waiting for a uci move string')
def step_impl(context):
    pass

@when('the given uci move is "{uci_string}"')
def the_uci_string_is_checked(context, uci_string):
    context.raised_exception = None
    
    try:
        context.string_validation = chess.Move.from_uci(uci_string).uci()
    except Exception as e:
        context.raised_exception = e

@then('the validated uci string should be "{correct_uci_string}"')
def the_uci_string_matches_expected(context, correct_uci_string):
    assert context.string_validation == correct_uci_string

@then('a "{exception_name}" error should be raised')
def uci_parser_returns_error(context, exception_name):
    # verify that an exception was caught
    assert context.raised_exception is not None, "Expected an error to be raised, but none was."

    # verify the class name matches the expected error
    actual_exception_name = context.raised_exception.__class__.__name__
    assert actual_exception_name == exception_name, \
        f"Expected {exception_name}, but got {actual_exception_name} instead."
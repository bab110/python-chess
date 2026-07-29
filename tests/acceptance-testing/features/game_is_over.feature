Feature: Check Game Is Over

Scenario: Game is over by checkmate
    Given the_user_has_created_a_board
    When the board state is "1rbqkbnr/pppp1Qpp/2n5/4p3/2B1P3/8/PPPP1PPP/RNB1K1NR b KQk - 0 4"
    And the game state is checked
    Then game over should return true

Scenario: Game is over by stalemate
    Given the_user_has_created_a_board
    When the board state is "7K/7P/7k/8/6q1/8/8/8 w - - 0 1"
    And the game state is checked
    Then game over should return true

Scenario: Game is not over
    Given the_user_has_created_a_board
    When the board state is "8/6P1/2p5/1Pqk4/6P1/2P1RKP1/4P1P1/8 w - - 0 1"
    And the game state is checked
    Then game over should return false

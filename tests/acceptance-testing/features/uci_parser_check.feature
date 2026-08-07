Feature: As a developer, I want the engine to support the Universal Chess Interface (UCI) protocol for chess move validation

Scenario: The parser is provided the valid uci string: b5c7
    Given the engine is waiting for a uci move string
    When the given uci move is "b5c7"
    Then the validated uci string should be "b5c7"

Scenario: The parser is provided the valid uci string: e7e8q
    Given the engine is waiting for a uci move string
    When the given uci move is "e7e8q"
    Then the validated uci string should be "e7e8q"

Scenario: The parser is provided the valid uci string: P@e4
    Given the engine is waiting for a uci move string
    When the given uci move is "P@e4"
    Then the validated uci string should be "P@e4"

Scenario: The parser is provided the valid uci string: B@f4
    Given the engine is waiting for a uci move string
    When the given uci move is "B@f4"
    Then the validated uci string should be "B@f4"

Scenario: The parser is provided the valid uci string: 0000
    Given the engine is waiting for a uci move string
    When the given uci move is "0000"
    Then the validated uci string should be "0000"

Scenario: The parser is fed the invalid uci string: "N"
    Given the engine is waiting for a uci move string
    When the given uci move is "N"
    Then a "InvalidMoveError" error should be raised

Scenario: The parser is fed the invalid uci string: "z1g3"
    Given the engine is waiting for a uci move string
    When the given uci move is "z1g3"
    Then a "InvalidMoveError" error should be raised

Scenario: The parser is fed the invalid uci string: "Q@g9"
    Given the engine is waiting for a uci move string
    When the given uci move is "Q@g9"
    Then a "InvalidMoveError" error should be raised
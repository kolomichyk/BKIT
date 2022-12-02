Feature Scenario Outline
    This function solve biquatratic equsion

    Scenario Outline: Solve the equation
    Given The A coff <A>
    And The B coff <B>
    And The C coff <C>
    When Solve the equation
    Then Get count <D> roots

    Examples:
    | A | B | C | D |

    | 4 | 0 | 3 | 0 |
    | 1 | 1 | 0 | 1 |
    | 3 | -5 | -28 | 2 |
    | 1 | -9 | 0 | 3 |
    | 1 | -73 | 576 | 4 |

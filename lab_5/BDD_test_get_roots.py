from main import get_roots
from pytest_bdd import scenarios, given, when, then, parsers

scenarios("test_equation.feature")

@given(parsers.parse("The A coff {A:d}"), target_fixture = "cofA")
def t_root_input_A(A):
    return A

@given(parsers.parse("The B coff {B:d}"), target_fixture = "cofB")
def t_root_input_B(B):
    return B

@given(parsers.parse("The C coff {C:d}"), target_fixture = "cofC")
def t_root_input_C(C):
    return C

@when(parsers.parse("Solve the equation"), target_fixture = "resl")
def t_root_solve(cofA, cofB, cofC):
    return get_roots(cofA, cofB, cofC)

@then(parsers.parse("Get count {result:d} roots"))
def t_tehn(resl, result):
    assert result == len(resl)
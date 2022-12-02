from input import input_func

def test_input_function():
    a = input_func.get_coef(1, 'Введите коэффициент А:')
    b = input_func.get_coef(2, 'Введите коэффициент B:')
    c = input_func.get_coef(3, 'Введите коэффициент C:')
    assert (a,b,c) == (4, 1 ,2) 
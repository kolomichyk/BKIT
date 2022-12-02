import sys

def get_coef(index, prompt):
    try:
        # Пробуем прочитать коэффициент из командной строки
        coef_str = sys.argv[index]
    except:
        # Вводим с клавиатуры
        print(prompt)
        coef_str = input()
    # Переводим строку в действительное число
    flag = True
    while flag:
        try:
            float(coef_str)
            flag = False
        except:
            coef_str = input()
    coef = float(coef_str)
    return coef

# Если сценарий запущен из командной строки
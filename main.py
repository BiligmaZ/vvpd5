import math

# Constants
ITERATIONS = 10

def maclaurin_cos(x):
    """
    Вычисляет косинус через ряд Маклорена.

    Подробное описание:
    Используется разложение косинуса в ряд Маклорена до заданного количества итераций.

    Аргументы:
    x (float): Угол в радианах.

    Возвращает:
    float: Приблизительное значение косинуса угла.

    Исключения:
    ValueError: Если x выходит за пределы допустимых значений.

    Примеры использования:
    maclaurin_cos(math.pi / 3)
    0.5
    """
    if not isinstance(x, (int, float)):
        raise ValueError("Аргумент должен быть числом.")

    result = 0
    for n in range(ITERATIONS):
        term = ((-1)**n * x**(2*n)) / math.factorial(2*n)
        result += term
    return result

def maclaurin_power(x, m):
    """
    Вычисляет (1 + x)^m через ряд Маклорена.

    Подробное описание:
    Используется разложение (1 + x)^m в ряд Маклорена до заданного количества итераций.

    Аргументы:
    x (float): Значение x.
    m (float): Показатель степени m.

    Возвращает:
    float: Приблизительное значение (1 + x)^m.

    Исключения:
    ValueError: Если x или m некорректны.

    Примеры использования:
    maclaurin_power(0.5, 2)
    2.25
    """
    if not isinstance(x, (int, float)) or not isinstance(m, (int, float)):
        raise ValueError("Аргументы должны быть числами.")

    result = 1
    for n in range(1, ITERATIONS):
        term = (math.prod([m - k + 1 for k in range(1, n + 1)]) * x**n) / math.factorial(n)
        result += term
    return result

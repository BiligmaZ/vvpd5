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
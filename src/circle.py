import math


def area(r):
    '''Возвращает площадь круга с радиусом r.

    Параметры:
        r (int|float): число r - радиус круга.
    
    Возвращаемое значение:
        float: площадь круга.

    Пример вызова:
        >>> area(5)
        78.53981633974483
        >>> area(2.5)
        19.634954084936208
    '''
    
    if isinstance(r, bool):
        raise TypeError("Радиус должен быть числом, а не булевым значением")
    if not isinstance(r, (int, float)):
        raise TypeError("Радиус должен быть числом")
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return math.pi * r * r


def perimeter(r):
    '''Возвращает длину окружности радиусом r.

    Параметры:
        r (int|float): число r - радиус круга.
    
    Возвращаемое значение:
        float: длина окружности.
    
    Пример вызова:
        >>> perimeter(5)
        31.41592653589793
        >>> perimeter(2.5)
        15.707963267948966
    '''
    
    if isinstance(r, bool):
        raise TypeError("Радиус должен быть числом, а не булевым значением")
    if not isinstance(r, (int, float)):
        raise TypeError("Радиус должен быть числом")
    if r < 0:
        raise ValueError("Радиус не может быть отрицательным")
    return 2 * math.pi * r
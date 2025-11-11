def area(a, h): 
    '''Возвращает площадь треугольника с основанием a и высотой h.

    Параметры:
        a (int|float): число a - длина основания треугольника.
        h (int|float): число h - высота треугольника, проведенная к основанию a.
    
    Возвращаемое значение:
        float: площадь треугольника.

    Пример вызова:
        >>> area(5, 4)
        10.0
        >>> area(3.5, 2)
        3.5
    '''

    if isinstance(a, bool) or isinstance(h, bool):
        raise TypeError("Основание и высота должны быть числами, а не булевыми значениями")
    if not isinstance(a, (int, float)) or not isinstance(h, (int, float)):
        raise TypeError("Основание и высота должны быть числами")
    if a < 0 or h < 0:
        raise ValueError("Основание и высота треугольника не могут быть отрицательными")
    return a * h / 2 


def perimeter(a, b, c): 
    '''Возвращает периметр треугольника со сторонами a, b, c.

    Параметры:
        a (int|float): число a - длина первой стороны треугольника.
        b (int|float): число b - длина второй стороны треугольника.
        c (int|float): число c - длина третьей стороны треугольника.
    
    Возвращаемое значение:
        int|float: периметр треугольника.
    
    Пример вызова:
        >>> perimeter(3, 4, 5)
        12
        >>> perimeter(2.5, 3.5, 4)
        10.0
    '''
    
    if isinstance(a, bool) or isinstance(b, bool) or isinstance(c, bool):
        raise TypeError("Стороны должны быть числами, а не булевыми значениями")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)) or not isinstance(c, (int, float)):
        raise TypeError("Все стороны должны быть числами")
    if (a < 0 or b < 0 or c < 0):
        raise ValueError("Стороны треугольника не могут быть отрицательными")
    if (a + b <= c or a + c <= b or b + c <= a):
        raise ValueError("Сумма любых двух сторон должна быть больше третьей")
    return a + b + c
def area(a, b): 
    '''Возвращает площадь прямоугольника со сторонами a и b.

    Параметры:
        a (int|float): число a - первая сторона прямоугольника.
        b (int|float): число b - вторая сторона прямоугольника.
    
    Возвращаемое значение:
        int|float: площадь прямоугольника.
    
    Пример вызова:
        >>> area(5, 10)
        50
        >>> area(2.5, 4.0)
        10.0
    '''

    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Стороны должны быть числами, а не булевыми значениями")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Стороны должны быть числами")
    if a < 0 or b < 0:
        raise ValueError("Стороны прямоугольника не могут быть отрицательными")
    return a * b


def perimeter(a, b): 
    '''Возвращает периметр прямоугольника со сторонами a и b.

    Параметры:
        a (int|float): число a - первая сторона прямоугольника.
        b (int|float): число b - вторая сторона прямоугольника.
    
    Возвращаемое значение:
        int|float: периметр прямоугольника.
    
    Пример вызова:
        >>> perimeter(5, 10)
        30
        >>> perimeter(2.5, 4.0)
        13.0
    '''
    
    if isinstance(a, bool) or isinstance(b, bool):
        raise TypeError("Стороны должны быть числами, а не булевыми значениями")
    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("Стороны должны быть числами")
    if a < 0 or b < 0:
        raise ValueError("Стороны прямоугольника не могут быть отрицательными")
    return 2 * (a + b)
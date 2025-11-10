def area(a):
    '''Возвращает площадь квадрата со стороной a.

    Параметры:
        a (int|float): число а - сторона квадрата.
    
    Возвращаемое значение:
        int|float: площадь квадрата.
    
    Пример вызова:
        >>> area(5)
        25
        >>> area(3.5)
        12.25
    '''
    
    if isinstance(a, bool):
        raise TypeError("Сторона должна быть числом, а не булевым значением")
    if not isinstance(a, (int, float)):
        raise TypeError("Сторона должна быть числом")
    if a < 0:
        raise ValueError("Сторона квадрата не может быть отрицательной")
    return a * a


def perimeter(a):
    '''Возвращает периметр квадрата со стороной a.

    Параметры:
        a (int|float): число а - сторона квадрата.
    
    Возвращаемое значение:
        int|float: периметр квадрата.
    
    Пример вызова:
        >>> perimeter(5)
        20
        >>> perimeter(3.5)
        14.0
    '''
    
    if isinstance(a, bool):
        raise TypeError("Сторона должна быть числом, а не булевым значением")
    if not isinstance(a, (int, float)):
        raise TypeError("Сторона должна быть числом")
    if a < 0:
        raise ValueError("Сторона квадрата не может быть отрицательной")
    return 4 * a
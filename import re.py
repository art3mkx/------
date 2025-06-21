import re

def is_palindrome(s):
    # Проверка на None и нестроковые типы (кроме чисел)
    if s is None:
        return False
    if not isinstance(s, (str, int, float)):
        return False
    
    # Преобразование числа в строку
    if isinstance(s, (int, float)):
        s = str(s)
    
    # Удаление всех небуквенно-цифровых символов и приведение к нижнему регистру
    cleaned = re.sub(r'[^a-zA-Zа-яА-Я0-9]', '', s).lower()
    
    # Проверка на пустую строку после очистки
    if not cleaned:
        return False
    
    # Сравнение строки с её обратной версией
    return cleaned == cleaned[::-1]
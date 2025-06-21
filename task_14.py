class EvenNumbers:
    def __init__(self, n):
        """
        Инициализирует итератор четных чисел
        :param n: количество четных чисел для генерации
        """
        if not isinstance(n, int) or n < 0:
            raise ValueError("n должно быть целым неотрицательным числом")
        self.n = n
        self.current = 0
        self.count = 0
    
    def __iter__(self):
        """Возвращает сам объект как итератор"""
        return self
    
    def __next__(self):
        """Возвращает следующее четное число"""
        if self.count >= self.n:
            raise StopIteration
        
        result = self.current
        self.current += 2
        self.count += 1
        return result
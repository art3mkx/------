class Dessert:
    def __init__(self, name=None, calories=None):
        self._name = name
        self._calories = calories
    
    @property
    def name(self):
        return self._name
    
    @name.setter
    def name(self, value):
        self._name = value
    
    @property
    def calories(self):
        return self._calories
    
    @calories.setter
    def calories(self, value):
        self._calories = value
    
    def is_healthy(self):
        try:
            return self._calories is not None and float(self._calories) < 200
        except (TypeError, ValueError):
            return False
    
    def is_delicious(self):
        return True
class Calculator:
    def __init__(self):
        # Initialize a private attribute to 0
        self._current_val = 0
    
    def add(self, x, y):
        self._current_val = x + y
        return self._current_val
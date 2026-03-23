class Human:
    def __init__(self, age, name):
        self._age = age  # "Protected" attribute
        self._name = name
    
    def _internal_method(self):  # "Protected" method
        return f"Internal: {self._name} is {self._age}"
        
    def __repr__(self):
        return f"Human(age={self._age}, name='{self._name}')" 
        
h = Human(15, 'BJ')

print(h)
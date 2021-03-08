from exceptions import InvalidNumberException


class Adder():
    DISALLOED_NUMBERS = [
        13, 14, 17, 18, 19
    ]

    def __init__(self, numbers=[]):
        self._numbers = numbers
    
    @property
    def numbers(self):
        return self._numbers

    def insert(self, number: int):
        if not isinstance(number, int):
            raise InvalidNumberException(number)

        self._numbers.append(number)

    def compute(self):
        result = 0
        for number in self._numbers: 
            if int(number) not in self.DISALLOED_NUMBERS:
                result = result + number
        
        return result

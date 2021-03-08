class InvalidNumberException(Exception):
    def __init__(self, number, message="Number is not a valid number. Only integers are allowed"):
        self.number = number
        self.message = "{0} {1}".format(number, message)
        super().__init__(self.message)



class InvalidInputException(Exception):
    def __init__(self, value, message="Invalid data."):
        self.value = number
        self.message = "{0} {1}".format(number, message)
        super().__init__(self.message)


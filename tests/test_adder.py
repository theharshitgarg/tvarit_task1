from commandline_parser.operations import Adder


def test_addition():
    numbers = [1, 3, 5]
    adder = Adder(numbers)
    assert adder.compute() == 9

    numbers = [10, 30, 50]
    adder = Adder(numbers)
    assert adder.compute() == 90


def test_15_16_addition():
    numbers = [1, 16, 15]
    adder = Adder(numbers)
    assert adder.compute() == 32

    numbers = [15, 15, 15]
    adder = Adder(numbers)
    assert adder.compute() == 45


def test_prohibited_numbers():
    numbers = [17, 13, 14]
    adder = Adder(numbers)
    assert adder.compute() == 0

    numbers = [17, 13, 19]
    adder = Adder(numbers)
    assert adder.compute() == 0

    numbers = [13, 13, 13]
    adder = Adder(numbers)
    assert adder.compute() == 0


def test_allowed_prohibited_mix_numbers():
    numbers = [15, 16, 14]
    adder = Adder(numbers)
    assert adder.compute() == 31

    numbers = [115, 120, 100]
    adder = Adder(numbers)
    assert adder.compute() == 335

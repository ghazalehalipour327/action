import pytest

def func(x):
    return x + 1


def test_answer():
    assert func(3) == 4


class TestClass:
    def test_one(self):
        x = "this"
        assert "h" in x

class TestClassDemoInstance:
    value = 0

    def test_one(self):
        self.value = 1
        assert self.value == 1

    def test_two(self):
        assert self.value == 0


# pytest test_fff.py::test_answer
# pytest test_fff.py::TestClass
# pytest test_fff.py::TestClassDemoInstance::test_one


def sum_numbers(a, b):
    return a + b

def multiply_numbers(a, b):
    return a * b


def test_sum_numbers():
    assert sum_numbers(2, 3) == 5
    assert sum_numbers(-1, 1) == 0

def test_multiply_numbers():
    assert multiply_numbers(2, 3) == 6
    assert multiply_numbers(-1, 1) == -1


class Calculator:
    def __init__(self):
        self.result = 0

    def add(self, num):
        self.result += num

    def subtract(self, num):
        self.result -= num

    def multiply(self, num):
        self.result *= num

    def divide(self, num):
        if num != 0:
            self.result /= num
        else:
            raise ValueError("Cannot divide by zero.")



def test_calculator_add():
    calc = Calculator()
    calc.add(5)
    assert calc.result == 5

def test_calculator_subtract():
    calc = Calculator()
    calc.subtract(3)
    assert calc.result == -3

def test_calculator_multiply():
    calc = Calculator()
    calc.multiply(4)
    assert calc.result == 0

def test_calculator_divide():
    calc = Calculator()
    calc.divide(2)
    assert calc.result == 0.0

def test_calculator_divide_by_zero():
    calc = Calculator()
    try:
        calc.divide(0)
    except ValueError as e:
        assert str(e) == "Cannot divide by zero."


def divide_numbers(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero.")
    return a / b


def test_divide_numbers():
    assert divide_numbers(10, 2) == 5

    with pytest.raises(ValueError) as exc_info:
        divide_numbers(10, 0)

    assert str(exc_info.value) == "Cannot divide by zero."


def divid(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b

# Pytest example to test the division function
def test_divide():
    assert divid(10, 2) == 5
    with pytest.raises(ValueError):
        divid(10, 0)


################################################

from unittest.mock import patch
from unittest import mock

def get_value():
    # Simulates getting a value from an external source
    return 5

def sum_values():
    value = get_value()
    return value + 10


def test_sum_values():
    with patch('test_fff.get_value', return_value=7):
        result = sum_values()
    assert result == 17

################################################

def summation(a, b):
    return a + b


def test_summation():
    with mock.patch('test_fff.summation') as mocked_summation:
        mocked_summation.return_value = 10
        result = summation(2, 3)
        assert result == 10

################################################

def multiplication(a, b):
    return a * b


def test_multiplication():
    with mock.patch('test_fff.multiplication') as mocked_multiplication:
        mocked_multiplication.return_value = 15
        result = multiplication(3, 5)
        assert result == 15

################################################

def multiplication(a, b):
    return a * b


def test_multiplication():
    with mock.patch('test_fff.multiplication') as mocked_multiplication:
        mocked_multiplication.side_effect  = lambda x, y: x * y
        result = multiplication(3, 5)
        assert result == mocked_multiplication.side_effect(3, 5)

#mocked_function.side_effect = ValueError('Invalid argument')
#mocked_function.return_values = [1, 2, 3]

################################################

class MathClass:
    def summation(self, a, b):
        return a + b


def test_summation():
    math_obj = MathClass()
    with mock.patch.object(math_obj, 'summation') as mocked_summation:
        mocked_summation.return_value = 10
        result = math_obj.summation(2, 3)
        assert result == 10

################################################

class User:
    def __init__(self, name):
        self.name = name

    def greet(self):
        return f"Hello, {self.name}!"



def test_greet():
    with mock.patch('test_fff.User') as MockUser:
        instance = MockUser.return_value
        instance.greet.return_value = "Mocked greeting"

        user = User("John")
        result = user.greet()

        assert result == "Mocked greeting"

##########################################################
##########################################################
##########################################################
##########################################################

#Fixtures

@pytest.fixture
def setup_fixture():
    # Setup operations or initialization code
    data = [1, 2, 3, 4, 5]
    return data

def test_fixture_example(setup_fixture):
    # Test using the fixture
    assert len(setup_fixture) == 5
    assert setup_fixture[0] == 1

#############################################################
@pytest.fixture
def reverse_string():
    original_string = "Hello, World!"
    reversed_string = original_string[::-1]
    return reversed_string

def test_reverse(reverse_string):
    assert reverse_string == "!dlroW ,olleH"

#############################################################

class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

@pytest.fixture
def create_person():
    person = Person("John Doe", 25)
    return person

def test_person_name(create_person):
    assert create_person.name == "John Doe"

def test_person_age(create_person):
    assert create_person.age == 25

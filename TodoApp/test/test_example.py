import pytest

def test_equal():
    assert 1 == 1

def test_is_instance():
    assert isinstance("hello", str)

def test_is_boolean():
    validated = True
    assert validated is True
    assert ('HELLO' == 'NO') is False

def test_type():
    assert type(1) is int
    assert type("hello") is str
    assert type([1, 2, 3]) is list
    assert type((1, 2, 3)) is tuple
    assert type({1, 2, 3}) is set
    assert type({"a": 1, "b": 2}) is dict

def test_greater_and_less_then():
    assert 5 > 3
    assert 2 < 4
    assert 3 >= 3
    assert 5 <= 10

def test_list():
    numbers = [1, 2, 3, 4, 5]
    any_list = [False, False]
    assert 1 in numbers
    assert 7 not in numbers
    assert all(numbers)
    assert not all(any_list)

class Student:
    def __init__(self, first_name: str, last_name: str, major: str, years: int):
        self.first_name = first_name
        self.last_name = last_name
        self.major = major
        self.years = years

@pytest.fixture
def default_student():
    return Student("John", "Doe", "Computer Science", 2)

def test_student_initialization(default_student):
    assert default_student.first_name == "John"
    assert default_student.last_name == "Doe"
    assert default_student.major == "Computer Science"
    assert default_student.years == 2
       
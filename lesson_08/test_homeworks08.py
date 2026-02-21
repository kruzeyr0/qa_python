import pytest
from homework_08 import Student
from homework_09 import Romb
from homework_07 import sum_of_two_numbers, avg, reverse, longest_word
from homework_11 import sum_of_numbers



def test_sum_of_two_numbers():
    assert sum_of_two_numbers(5, 10) == 15
    assert sum_of_two_numbers(-5, 10) == 5

def test_sum_of_two_numbers_zero_values():
    assert sum_of_two_numbers(0, 0) == 0

def test_sum_of_two_numbers_negative_values():
    assert sum_of_two_numbers(-2.5, -2.5) == -5.0

def test_sum_of_two_numbers_float_values():
    assert sum_of_two_numbers(2.5, 2.5) == 5.0

def test_sum_of_two_numbers_invalid_types():
    with pytest.raises(TypeError):
        sum_of_two_numbers("5", 10)



#########################################################################################

def test_avg():
    assert avg(1, 2, 3, 4, 5) == 3.0

def test_avg_zero_values():
    assert avg(0, 0, 0) == 0.0

def test_avg_negative_values():
    assert avg(-1, -2, -3) == -2.0

#########################################################################################

def test_reverse():
    assert reverse("Hello, world!") == "!dlrow ,olleH"

def test_reverse_empty_string():
    assert reverse("") == ""

def test_reverse_single_character():
    assert reverse("a") == "a"

##########################################################################################

def test_longest_word():
    assert longest_word(["cat", "dog", "elephant", "giraffe"]) == "elephant"

def test_longest_word_with_input():
    assert longest_word("Enter words: cat dog elephant giraffe".split()) == "elephant"

def test_longest_word_with_equal_length_words():
    assert longest_word(["a", "ab", "abc"]) == "abc"

def test_longest_word_with_empty_list():
    assert longest_word([]) == ""

###########################################################################################

def test_student_info():
    student = Student(first_name="Andrii", last_name="Katrych", age=33, avg_score=90)

    info = student.get_student_info()

    assert info["avg_score"] == 90

###########################################################################################

def test_rom_valid_angles():
    romb = Romb()
    romb.angle_a = 60
    assert romb.angle_b == 120

###########################################################################################

def test_sum_of_numbers_valid():
    assert sum_of_numbers(["1,2,3"]) == [6]


def test_sum_of_numbers_with_error():
    assert sum_of_numbers(["qwerty"]) == ["Не можу це зробити!"]

    
# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import next_palindrome as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "m"
    module_0.next_palindrome(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    var_0 = module_0.next_palindrome(list_0)
    float_0 = 220.7436
    module_0.next_palindrome(float_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.next_palindrome(none_type_0)


def test_case_3():
    int_0 = 8
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.next_palindrome(list_0)
    var_1 = module_0.next_palindrome(var_0)


def test_case_4():
    int_0 = 9
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.next_palindrome(list_0)
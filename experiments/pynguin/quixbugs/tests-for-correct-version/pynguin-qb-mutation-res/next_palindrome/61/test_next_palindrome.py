# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import next_palindrome as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xd2\x08"
    module_0.next_palindrome(bytes_0)


def test_case_1():
    set_0 = set()
    var_0 = module_0.next_palindrome(set_0)
    var_1 = module_0.next_palindrome(var_0)
    int_0 = 9
    list_0 = [int_0, int_0, int_0, int_0]
    var_2 = module_0.next_palindrome(var_1)
    var_3 = module_0.next_palindrome(list_0)
    var_4 = module_0.next_palindrome(var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.next_palindrome(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"p\t"
    module_0.next_palindrome(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.next_palindrome(list_0)
    set_0 = set()
    var_1 = module_0.next_palindrome(var_0)
    var_2 = module_0.next_palindrome(set_0)
    int_0 = 9
    list_1 = [list_0, int_0, int_0, list_0]
    module_0.next_palindrome(list_1)


def test_case_5():
    int_0 = 9
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.next_palindrome(list_0)
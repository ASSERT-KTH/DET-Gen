# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import next_palindrome as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xa0"
    module_0.next_palindrome(bytes_0)


def test_case_1():
    list_0 = []
    var_0 = module_0.next_palindrome(list_0)
    var_1 = module_0.next_palindrome(var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.next_palindrome(none_type_0)


def test_case_3():
    int_0 = 9
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.next_palindrome(list_0)
    var_1 = module_0.next_palindrome(var_0)


def test_case_4():
    int_0 = 9
    list_0 = [int_0, int_0, int_0, int_0]
    var_0 = module_0.next_palindrome(list_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    set_0 = set()
    int_0 = 9
    var_0 = module_0.next_palindrome(set_0)
    var_1 = module_0.next_palindrome(set_0)
    bool_0 = True
    dict_0 = {int_0: var_0, bool_0: int_0}
    var_2 = module_0.next_palindrome(dict_0)
    var_3 = module_0.next_palindrome(var_0)
    var_4 = module_0.next_palindrome(var_0)
    var_5 = module_0.next_palindrome(var_4)
    var_6 = module_0.next_palindrome(dict_0)
    none_type_0 = None
    module_0.next_palindrome(none_type_0)
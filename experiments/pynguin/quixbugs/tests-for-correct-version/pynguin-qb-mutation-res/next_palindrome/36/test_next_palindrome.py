# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import next_palindrome as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x9fCO@\xde\x14\x18\x90_R\t\xf7\xca^\xac\xba"
    module_0.next_palindrome(bytes_0)


def test_case_1():
    list_0 = []
    var_0 = module_0.next_palindrome(list_0)


def test_case_2():
    list_0 = []
    var_0 = module_0.next_palindrome(list_0)
    var_1 = module_0.next_palindrome(var_0)


def test_case_3():
    set_0 = set()
    var_0 = module_0.next_palindrome(set_0)
    var_1 = module_0.next_palindrome(var_0)
    var_2 = module_0.next_palindrome(var_0)
    var_3 = module_0.next_palindrome(var_2)
    var_4 = module_0.next_palindrome(var_0)
    var_5 = module_0.next_palindrome(var_4)
    var_6 = module_0.next_palindrome(var_2)
    var_7 = module_0.next_palindrome(var_2)
    var_8 = module_0.next_palindrome(var_3)
    var_9 = module_0.next_palindrome(var_4)


def test_case_4():
    int_0 = 237
    list_0 = [int_0]
    var_0 = module_0.next_palindrome(list_0)
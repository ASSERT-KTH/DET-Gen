# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import next_palindrome as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "qPcS6%"
    module_0.next_palindrome(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ""
    var_0 = module_0.next_palindrome(str_0)
    var_1 = module_0.next_palindrome(str_0)
    var_2 = module_0.next_palindrome(var_0)
    var_3 = module_0.next_palindrome(var_0)
    none_type_0 = None
    module_0.next_palindrome(none_type_0)


def test_case_2():
    bytes_0 = b""
    var_0 = module_0.next_palindrome(bytes_0)
    var_1 = module_0.next_palindrome(var_0)
    var_2 = module_0.next_palindrome(var_1)
    var_3 = module_0.next_palindrome(var_2)
    var_4 = module_0.next_palindrome(var_0)
    var_5 = module_0.next_palindrome(var_3)
    var_6 = module_0.next_palindrome(var_2)
    var_7 = module_0.next_palindrome(var_0)
    var_8 = module_0.next_palindrome(var_4)
    var_9 = module_0.next_palindrome(var_8)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b""
    var_0 = module_0.next_palindrome(bytes_0)
    var_1 = module_0.next_palindrome(var_0)
    var_2 = module_0.next_palindrome(bytes_0)
    var_3 = module_0.next_palindrome(var_0)
    var_4 = module_0.next_palindrome(var_0)
    var_5 = module_0.next_palindrome(var_4)
    var_6 = module_0.next_palindrome(var_5)
    var_7 = module_0.next_palindrome(var_0)
    var_8 = module_0.next_palindrome(var_0)
    var_9 = module_0.next_palindrome(var_8)
    var_10 = module_0.next_palindrome(var_0)
    var_11 = module_0.next_palindrome(var_2)
    var_12 = module_0.next_palindrome(var_7)
    var_13 = module_0.next_palindrome(var_8)
    var_14 = module_0.next_palindrome(var_5)
    var_15 = module_0.next_palindrome(var_12)
    var_16 = module_0.next_palindrome(var_0)
    var_17 = module_0.next_palindrome(var_10)
    var_18 = module_0.next_palindrome(var_2)
    bool_0 = True
    module_0.next_palindrome(bool_0)
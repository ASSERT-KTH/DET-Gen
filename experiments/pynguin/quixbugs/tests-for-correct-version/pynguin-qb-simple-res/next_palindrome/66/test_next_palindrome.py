# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import next_palindrome as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "dZo)$k3,7=g6\t<\\O;2"
    module_0.next_palindrome(str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b""
    var_0 = module_0.next_palindrome(bytes_0)
    var_1 = module_0.next_palindrome(bytes_0)
    object_0 = module_1.object()
    module_0.next_palindrome(object_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 5971
    module_0.next_palindrome(int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b""
    var_0 = module_0.next_palindrome(bytes_0)
    var_1 = module_0.next_palindrome(bytes_0)
    object_0 = module_1.object()
    var_2 = module_0.next_palindrome(var_0)
    module_0.next_palindrome(object_0)


def test_case_4():
    int_0 = -725
    list_0 = [int_0]
    var_0 = module_0.next_palindrome(list_0)


def test_case_5():
    bytes_0 = b""
    var_0 = module_0.next_palindrome(bytes_0)
    var_1 = module_0.next_palindrome(var_0)
    var_2 = module_0.next_palindrome(var_0)
    var_3 = module_0.next_palindrome(var_1)
    var_4 = module_0.next_palindrome(var_3)
    var_5 = module_0.next_palindrome(var_0)
    var_6 = module_0.next_palindrome(var_0)
    var_7 = module_0.next_palindrome(var_4)
    var_8 = module_0.next_palindrome(var_3)
    var_9 = module_0.next_palindrome(var_3)
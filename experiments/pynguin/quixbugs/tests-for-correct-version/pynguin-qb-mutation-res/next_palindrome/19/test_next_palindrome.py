# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import next_palindrome as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "SO"
    module_0.next_palindrome(str_0)


def test_case_1():
    tuple_0 = ()
    var_0 = module_0.next_palindrome(tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    object_0 = module_1.object()
    module_0.next_palindrome(object_0)


def test_case_3():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.next_palindrome(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    set_0 = set()
    var_0 = module_0.next_palindrome(set_0)
    var_1 = module_0.next_palindrome(set_0)
    var_2 = module_0.next_palindrome(set_0)
    object_0 = module_1.object()
    none_type_0 = None
    var_3 = module_0.next_palindrome(var_0)
    var_4 = module_0.next_palindrome(var_0)
    module_0.next_palindrome(none_type_0)


def test_case_5():
    dict_0 = {}
    var_0 = module_0.next_palindrome(dict_0)
    var_1 = module_0.next_palindrome(var_0)
    var_2 = module_0.next_palindrome(var_0)
    var_3 = module_0.next_palindrome(var_2)
    var_4 = module_0.next_palindrome(var_1)
    var_5 = module_0.next_palindrome(var_4)
    var_6 = module_0.next_palindrome(var_1)
    var_7 = module_0.next_palindrome(var_4)
    var_8 = module_0.next_palindrome(var_0)
    var_9 = module_0.next_palindrome(var_7)
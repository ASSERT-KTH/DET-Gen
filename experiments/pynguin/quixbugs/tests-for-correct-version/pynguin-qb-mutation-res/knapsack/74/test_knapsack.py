# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import knapsack as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x92\xaf\xf5[\x92\xf2\xb6{\xe8\xbb\x16Q\xd6\x9e\x90\x1c\xe3O\x8b"
    module_0.knapsack(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    tuple_0 = ()
    str_0 = "N I&eoR\\g(hycd\n"
    var_0 = module_0.knapsack(str_0, tuple_0)
    assert var_0 == 0
    module_0.knapsack(var_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    tuple_0 = ()
    var_0 = module_0.knapsack(tuple_0, tuple_0)
    assert var_0 == 0
    dict_0 = {var_0: var_0, tuple_0: var_0, tuple_0: var_0}
    tuple_1 = (dict_0, var_0)
    module_0.knapsack(var_0, tuple_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    bytes_0 = b""
    tuple_0 = (list_0, bytes_0)
    module_0.knapsack(bool_0, tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = True
    list_0 = [bool_0, bool_0]
    bytes_0 = b"$\xde"
    tuple_0 = (list_0, bytes_0)
    var_0 = module_0.knapsack(bool_0, tuple_0)
    assert var_0 == 1
    module_0.knapsack(var_0, var_0)
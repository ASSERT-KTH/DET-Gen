# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import minimum_spanning_tree as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    dict_0 = {bool_0: bool_0}
    module_0.minimum_spanning_tree(dict_0)


def test_case_1():
    bytes_0 = b""
    var_0 = module_0.minimum_spanning_tree(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    object_0 = module_1.object()
    module_0.minimum_spanning_tree(object_0)


def test_case_3():
    bool_0 = False
    tuple_0 = (bool_0, bool_0)
    dict_0 = {tuple_0: tuple_0}
    var_0 = module_0.minimum_spanning_tree(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "L5"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.minimum_spanning_tree(dict_0)
    bytes_0 = b"`\xca\x1f\xa3\xfd* \x94g\x96\xda\xabsx\x116\xee"
    list_0 = [bytes_0, bytes_0]
    module_0.minimum_spanning_tree(list_0)
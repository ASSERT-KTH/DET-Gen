# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import minimum_spanning_tree as module_0


def test_case_0():
    list_0 = []
    var_0 = module_0.minimum_spanning_tree(list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xe4\xa7\xe5\xf1\xe5[\xbf\xa3\xe3\xaf\x96\xa2\xc9o&\xae\x80\xf8"
    module_0.minimum_spanning_tree(bytes_0)


def test_case_2():
    str_0 = "b\t"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.minimum_spanning_tree(dict_0)


def test_case_3():
    str_0 = "@@"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.minimum_spanning_tree(dict_0)
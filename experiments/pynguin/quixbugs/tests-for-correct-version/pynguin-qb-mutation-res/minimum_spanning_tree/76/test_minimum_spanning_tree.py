# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import minimum_spanning_tree as module_0


def test_case_0():
    str_0 = "Nq"
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.minimum_spanning_tree(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xae\x1e\xd8\xd9{h\xab\xc4\xf6\xc4R\x97\x9b\xb9\x87\xf7"
    module_0.minimum_spanning_tree(bytes_0)


def test_case_2():
    str_0 = "//"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.minimum_spanning_tree(dict_0)
# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_paths as module_0


def test_case_0():
    str_0 = ""
    var_0 = module_0.shortest_paths(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x8e\xfb\x88U\xb5\x1a\xb3\x01\x1e\xbc\xac\xb7\x1e\xb6\xaf\n"
    module_0.shortest_paths(bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.shortest_paths(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "(:"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0, str_0: str_0}
    module_0.shortest_paths(str_0, dict_0)
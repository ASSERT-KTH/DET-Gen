# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1235 as module_0


def test_case_0():
    bool_0 = False
    str_0 = "Im9\t`RoRe?b"
    list_0 = [bool_0, bool_0, str_0, bool_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    bytes_0 = b"\xa1\xd4\xe9\xbaAb\xb0R"
    dict_0 = {bool_0: set_0, bool_0: set_0, bytes_0: set_0}
    var_0 = module_0.func(*dict_0)
    module_0.func()

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2096 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


def test_case_1():
    bool_0 = True
    set_0 = {bool_0, bool_0}
    var_0 = module_0.func(*set_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.func(*none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "2"
    bytes_0 = b"i6Z\x8aW\x973"
    list_0 = [str_0, str_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    module_0.func()

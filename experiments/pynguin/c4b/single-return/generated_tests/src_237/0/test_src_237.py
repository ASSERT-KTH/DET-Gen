# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_237 as module_0


def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"J\x0c\xd2\xfe\xe8\x99\xddX\x94\x9e,\x02\xe4\xa0\x08T\x82\xf0*"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 67599
    module_0.func()

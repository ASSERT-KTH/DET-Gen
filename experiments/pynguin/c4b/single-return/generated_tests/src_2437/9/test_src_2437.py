# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2437 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "=2 J-)7ZB0Eb+("
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == 0
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "\r&#Wt\n=v*i\nrV_pb"
    dict_0 = {str_0: str_0, str_0: str_0}
    var_0 = module_0.func(*dict_0)
    assert var_0 == 1
    module_0.func()

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1907 as module_0


def test_case_0():
    str_0 = "aF,@!;AoC8boypb/)8V"
    var_0 = module_0.func(*str_0)
    assert var_0 == "YES"


#@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "9P;^WW5:!\\XRtFvp2w"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
#    module_0.func()


def test_case_3():
    str_0 = "ypdi,5oBBU"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
    var_1 = module_0.func(*list_0)
    assert var_1 == "NO"

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_528 as module_0


def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Sheldon"


#@pytest.mark.xfail(strict=True)
def test_case_1():
    float_0 = -269.0
#    module_0.func(*float_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xab\x05k\x96\x05\xbbx@\xa8-\xa0\xa2"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "Sheldon"
#    module_0.func(*var_0)

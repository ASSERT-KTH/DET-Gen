# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2626 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xeb\xb5\xa3\xd2\x8f\x17\xf4\x92\xf5/\xb7"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 117
#    module_0.func()


def test_case_1():
    int_0 = -1211
    set_0 = {int_0}
    var_0 = module_0.func(*set_0)
    assert var_0 == 0


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()

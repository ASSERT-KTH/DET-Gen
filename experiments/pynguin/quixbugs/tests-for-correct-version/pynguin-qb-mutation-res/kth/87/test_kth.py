# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import kth as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 1422.393
    bytes_0 = b"\x9e\x92\xfd\xe2\x83v"
    module_0.kth(bytes_0, float_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "2MQb"
    module_0.kth(str_0, str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    module_0.kth(bool_0, bool_0)


def test_case_3():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.kth(list_0, bool_0)
    assert var_0 is True


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = -982.4289
    list_0 = [float_0, float_0, float_0, float_0]
    int_0 = -966
    module_0.kth(list_0, int_0)
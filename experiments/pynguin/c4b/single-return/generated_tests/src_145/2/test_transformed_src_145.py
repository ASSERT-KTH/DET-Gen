# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_145 as module_0


def test_case_0():
    float_0 = 47.3
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


def test_case_1():
    bytes_0 = b"\xd8"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 2


#@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -76.9
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 45.476358669732775
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 35.01301704779293
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 3
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    float_0 = 45.476358669732775
    list_0 = [float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 2
    var_1 = module_0.func(*list_0)
    assert var_1 == 2
    list_1 = [var_0, var_1, var_1]
    var_2 = module_0.func(*list_1)
    assert var_2 == 1
#    module_0.func(*var_0)

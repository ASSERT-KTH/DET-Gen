# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_969 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xb1\xf5\xd4\x1f\xab\x08\xe6\xac\x18\xcd"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = -712.986059
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    module_0.func()
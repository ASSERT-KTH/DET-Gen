# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_812 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xb2->\xd8\xb4O\xa2c\x8e\xce\xb7\xbe\xa4L\xd5\x90\x87\xf9\x8f"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


def test_case_1():
    int_0 = 3298
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    float_0 = -3668.1093
    list_1 = [float_0, float_0, float_0, float_0]
    var_1 = module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()

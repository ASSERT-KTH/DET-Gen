# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_960 as module_0


def test_case_0():
    bytes_0 = b"Nf\x0c\xed\xff\x02w\x94\xd0{"
    var_0 = module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    bytes_0 = b"?\xb7\xce"
    var_0 = module_0.func(*bytes_0)


def test_case_3():
    bytes_0 = b"\x91\x1ap\xd6;e"
    var_0 = module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = -4509.5
    list_0 = [float_0, float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    module_0.func()

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_363 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b'\x0e1\xc6\x8e"F\x02\x1e\xe8\xca'
    list_0 = [bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ">h-{Bb("
    float_0 = -3290.2
    list_0 = [float_0, str_0, float_0, str_0]
    list_1 = [str_0, list_0, list_0]
    var_0 = module_0.func(*list_1)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0, tuple_0, tuple_0]
    module_0.func(*list_0)

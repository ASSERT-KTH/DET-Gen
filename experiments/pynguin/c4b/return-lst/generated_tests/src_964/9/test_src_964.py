# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_964 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    list_0 = [bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xd9\xd6\xfc\xdcoG\x11[F\xd8"
    var_0 = module_0.func(*bytes_0)
    tuple_0 = (bytes_0,)
    list_0 = [tuple_0, tuple_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 439.554926
    dict_0 = {float_0: float_0, float_0: float_0, float_0: float_0, float_0: float_0}
    list_0 = [float_0, float_0, float_0, dict_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"b"
    list_0 = module_0.func(*bytes_0)
    var_0 = module_0.func(*list_0)
    module_0.func()
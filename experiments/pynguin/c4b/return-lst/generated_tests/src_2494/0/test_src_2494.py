# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2494 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b""
    set_0 = {bytes_0, bytes_0}
    list_0 = [set_0, set_0, set_0, set_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    complex_0 = 927.2614 + 1446.00402j
    module_0.func(*complex_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = 'j>m)(o<"0l60TR3m;9'
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*var_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "HcB|/"
    var_0 = module_0.func(*str_0)
    module_0.func()

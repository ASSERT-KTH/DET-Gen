# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1915 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -1456.5655
    list_0 = [float_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    float_0 = 793.9055
    list_0 = [float_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 794.3266113757218
    list_0 = [float_0, float_0]
    module_0.func(*list_0)
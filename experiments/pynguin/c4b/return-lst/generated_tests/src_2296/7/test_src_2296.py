# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2296 as module_0


def test_case_0():
    str_0 = "O\rE\n1rf8K~>+Q?}vol"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "O\rE\n1rf8K~>+Q?}vol"
    list_0 = [str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "H)E\n1rf8K~>iQ?}vR!,"
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "&%N),Z^Y9zc"
    list_0 = [str_0]
    module_0.func(*list_0)

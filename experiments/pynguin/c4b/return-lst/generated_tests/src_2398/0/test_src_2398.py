# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2398 as module_0


def test_case_0():
    str_0 = "}u=q43dTD>)B7iA"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.func(*dict_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "}u=q43eTD?)B7iA"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.func(*dict_0)
    var_1 = module_0.func(*var_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "}u=q43dTDY)B7i>A"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.func(*dict_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "uKq?dTD\n)o7iA"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    var_0 = module_0.func(*dict_0)
    module_0.func()

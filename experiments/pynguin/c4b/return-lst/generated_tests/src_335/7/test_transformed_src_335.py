# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_335 as module_0


def test_case_0():
    str_0 = "eutOddH\x0bq}9PZZ93u\x0bc"
    var_0 = module_0.func(*str_0)


def test_case_1():
    str_0 = "eutOddH\x0bq}9PZZ93u\x0bc"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "Q"
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*str_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "9MZ@Agx="
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()
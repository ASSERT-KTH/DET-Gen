# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2677 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = ">|jZ9Q5"
    float_0 = 747.579
    list_0 = [str_0, float_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "v^_\r  mJ5w'\".tQYp~\n="
    float_0 = 747.579
    list_0 = [str_0, float_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = ">|jZ9Q5"
    float_0 = 748.0
    list_0 = [str_0, float_0]
#    module_0.func(*list_0)


def test_case_4():
    str_0 = "<y<=}',8[1:+@\x0c'"
    float_0 = 924.03973
    list_0 = [str_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "undefined"


def test_case_5():
    str_0 = '>v^_\r  mJ5w"QY~='
    float_0 = 744.9774584034773
    list_0 = [str_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "undefined"


#@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = '>v^_\r  mJ5w"QY~='
    float_0 = 749.02092
    list_0 = [str_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "ccw"
#    module_0.func(*str_0)

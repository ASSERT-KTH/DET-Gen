# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2294 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "+<1rD,5;)3RI[o\r"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "NO"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "9 I\x0c!5KG;AEl#X/"
    int_0 = 123
    dict_0 = {int_0: int_0, str_0: int_0, str_0: int_0}
    tuple_0 = (str_0, int_0, dict_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == "YES"
#    module_0.func()

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_952 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "\t045\r0 "
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "\t04\r0 "
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "\t0\r\r0 "
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "\t005\r40 "
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
#    module_1.object(*str_0, **var_0)

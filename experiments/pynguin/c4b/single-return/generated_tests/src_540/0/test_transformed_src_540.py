# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_540 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
def test_case_0():
    set_0 = set()
    list_0 = [set_0, set_0, set_0, set_0]
    list_1 = [list_0, list_0, set_0, set_0]
#    module_0.func(*list_1)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    set_0 = set()
    list_0 = [set_0, set_0, set_0, set_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = " 2UYL.}\x0c["
    bytes_0 = b"hW\x7f\xfa\x83\x1e\x86\xeb\x9c\xe5ke\x85\xd3wY"
    list_0 = [str_0, bytes_0, bytes_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 6
    set_0 = set()
    list_1 = [set_0, set_0, set_0, set_0]
    var_1 = module_0.func(*list_1)
    assert var_1 == 1
#    module_1.object(*list_1)

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1093 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"v\xadj$8\x12\xad\x85\xcc\xe5"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = False
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()

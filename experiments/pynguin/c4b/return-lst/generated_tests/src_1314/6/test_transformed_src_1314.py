# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1314 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x80"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x80"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*var_0)
    none_type_0 = None
    var_2 = module_0.func(*var_0)
#    module_0.func(*none_type_0)

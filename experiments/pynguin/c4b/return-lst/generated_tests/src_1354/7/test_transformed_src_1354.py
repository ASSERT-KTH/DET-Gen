# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1354 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = 1886
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()


def test_case_2():
    bytes_0 = b"\xd9+\xec\xee\x9bW\x7f\xcb&?\xc9\x1e\xbe~\xe99\xc6D\x0f\xfe"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*var_0)
    var_2 = module_1.object()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xd9+\xec\xee\x9bW\x7f\xcb&?\x1e\xbe~\xe99\xc6D\x0f\xb0\xfe"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xe1\xcf\xb8\xfa"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_0.func(*var_0)
#    module_1.object(*var_1)
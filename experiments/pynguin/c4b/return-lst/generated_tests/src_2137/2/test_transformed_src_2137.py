# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2137 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"r\xb7v\xff\x03"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
#    module_1.object(*var_0, **var_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x7f\xfd\x80\x9aW\xde"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    list_1 = [list_0, bytes_0, bytes_0, list_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_1)
    var_1 = module_0.func(*list_0)
#    module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x7f\xfd\x80\x9aW\xde"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    list_1 = [bytes_0, list_0, list_0, bytes_0]
    var_0 = module_0.func(*list_1)
    var_1 = module_0.func(*list_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\x7f\xfd\x80\x9aW\xa8\xdd"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    list_1 = [list_0, bytes_0, list_0, list_0, list_0, bytes_0]
    var_0 = module_0.func(*list_1)
#    module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\x7f\xfd\x80\x9aW\xa8\xdd"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    list_1 = [list_0, list_0, list_0, bytes_0, list_0, list_0, list_0, bytes_0]
    var_0 = module_0.func(*list_1)
    var_1 = module_0.func(*list_0)
#    module_0.func()

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_709 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x96>d\xc6\xc6\xef'\xad\xb3\xdc\x8d\xa3\xd6\xe8f"
    var_0 = module_0.func(*bytes_0)
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x96>\xc6\xc6\xef'\xad\xb3\xdc\x8d\xa3\xd6\xe8f"
    var_0 = module_0.func(*bytes_0)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x96>\xc6Y\x04\xc6\xef'\xad\xb3\xdc\x8d\xa3\xd6\xe8f"
    var_0 = module_0.func(*bytes_0)
#    module_1.object(*var_0)

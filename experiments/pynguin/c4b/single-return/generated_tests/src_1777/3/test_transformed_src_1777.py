# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1777 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xa7\x1f;\xbd#j7\xdd\xd0\x9c\xf0\xac7\xdb"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xa7\x1f;\xbd\xeb'7\xdd\xd0\xe7\x9c\xf0\xac7\xdb"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 12
#    module_1.object(*bytes_0)

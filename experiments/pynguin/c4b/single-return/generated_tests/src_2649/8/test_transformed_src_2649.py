# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2649 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xf4\x89\x89F\xe2\xb1\xd7\xd0\xe5\xf9\xe9\xda\xd4\xa77A"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 121
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0
    bool_1 = False
#    module_0.func(*bool_1)

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_38 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    tuple_0 = (bool_0,)
    list_0 = [bool_0, bool_0, bool_0, tuple_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "Sheldon"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b'"\xa9h2\x965\xa9|\xd7\x1f\xed\x91B]l\x8eY\x9e\x81\x98'
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "Howard"
#    module_0.func(*list_0)

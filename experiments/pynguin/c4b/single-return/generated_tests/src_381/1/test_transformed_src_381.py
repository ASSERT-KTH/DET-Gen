# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_381 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x82\x08\xb6\x99w\xf7R\x180\xb6"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "7"
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    int_0 = -1127
    list_0 = [int_0, int_0, int_0]
#    module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x08\xb6w\xf7R\x180\xb6"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == "8"
    var_1 = module_0.func(*var_0)
    assert var_1 == "8"
    var_2 = module_0.func(*var_1)
    assert var_2 == "8"
#    module_0.func()

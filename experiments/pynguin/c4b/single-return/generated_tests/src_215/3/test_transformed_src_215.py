# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_215 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"Y\x80rb\xd3l\xe2\x96\xb8\xa5"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 6
#    module_0.func(*var_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"Yr|\x8a:\x9a\xe2\x96\xb8\xa5"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
    list_0 = [var_0, var_0, var_0, var_0, var_0, bytes_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 0
#    module_0.func()

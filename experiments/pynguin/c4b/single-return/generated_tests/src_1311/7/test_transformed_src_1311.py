# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1311 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"v\xfba\x90|\xb5<"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 2
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"v\xfbaU\x90|\xb5<"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 3
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"u=)Mv%\xff\xbd]\xed\xacM\x0b"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 5
    var_1 = module_0.func(*bytes_0)
    assert var_1 == 5
#    module_0.func()

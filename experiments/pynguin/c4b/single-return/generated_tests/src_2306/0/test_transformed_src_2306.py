# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2306 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"j\x1cb\xdf\x94\x07\xccI\xcd\xaa\xd8%\x8d\x85"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 7
    object_0 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xa7\xc1\x7fShr\xbe\r\xcajWj\x90\xd6^nP\xbd"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
#    module_0.func(*var_0)

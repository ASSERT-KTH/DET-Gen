# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1078 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x0b.8\xc1\xef\x8d`U\xa8\xb6"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 31
#    module_1.object(**var_0)

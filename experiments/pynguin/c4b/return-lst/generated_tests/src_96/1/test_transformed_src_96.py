# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_96 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    bytes_0 = b"\x14M\x0b\x14J\xb1\xda\x12"
    var_0 = module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x01\x0b\x02\xfa\x14Jb\xbb\x12"
    var_0 = module_0.func(*bytes_0)
    var_1 = module_1.object()
#    module_0.func(*var_0)

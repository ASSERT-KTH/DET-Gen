# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2246 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    list_0 = []
#    module_0.func(*list_0)


def test_case_1():
    bytes_0 = b"\x88`\xbco\x89\xb1`"
    list_0 = [bytes_0, bytes_0]
    list_1 = [list_0, list_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_1)

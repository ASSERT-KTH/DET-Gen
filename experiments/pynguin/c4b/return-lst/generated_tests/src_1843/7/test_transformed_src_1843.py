# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1843 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xe2\xe5%\xa0\xeb\xee\x1e\x11\\\x88\xc2\x94\xed\x82(\xeb\xd2(\xf6"
    set_0 = {bytes_0}
    var_0 = module_0.func(*bytes_0)
    list_0 = [set_0]
    bytes_1 = b"5\x9c\xae\x9f\xe6\xa1\xb4\x9d\x1b\xc4\xfe"
    list_1 = [list_0, bytes_1, bytes_0, bytes_1]
#    module_0.func(*list_1)
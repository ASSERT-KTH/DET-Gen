# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1191 as module_0


def test_case_0():
    bytes_0 = b"\x80.\xa3(\xf2"
    var_0 = module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


def test_case_2():
    bytes_0 = b".\xa3(\xf2"
    var_0 = module_0.func(*bytes_0)


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x80.\xa3(\xf2"
    int_0 = 4969
    list_0 = [int_0, int_0, bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
#    module_0.func()

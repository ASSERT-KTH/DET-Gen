# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2132 as module_0


def test_case_0():
    str_0 = "0J06qEt{y7n/"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\xd3e\xdcde\x19\xdc\r\xcd\xc4/\xe1\xfdMJQ(v\xcc"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    object_0 = module_0.func(*list_0)
    assert object_0 == 1
    module_0.func(*object_0)

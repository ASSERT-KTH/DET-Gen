# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2113 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b")\xce(Y\xd2\x19\xd1Z\x9d\xa1\x9ct\xbcTE\xa6"
    object_0 = module_0.func(*bytes_0)
    assert object_0 == 13
    bool_0 = False
    list_0 = [object_0, bool_0, object_0, object_0]
    module_0.func(*list_0)

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2458 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x95\xa5\xf9\x93\x90<*\xa2M@\xb3\xfb\\\xd1\xad\x02I\xc7}"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x95\xa5\x86\x93\x90<\xa2M@\xb3\xfb\\\xd1\xad\x02I\xc7}"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"I\xe7\xe1F\x9e"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 4
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    bytes_0 = b"\xa5\x86\x93\x90\x98\xa2@\x81\xfb\\\xd1\xad\x02I\xc7"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 3
    module_0.func()

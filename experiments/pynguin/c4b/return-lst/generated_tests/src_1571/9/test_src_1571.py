# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1571 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"]\xae\xe8\x83G8\xe1\xa7\xbd\t\xa5\xb3\xce"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


def test_case_1():
    bytes_0 = b"p}\\B5}\x91\xef%\xaa=\xd1I\r\xed\xea\xb8\xe5("
    list_0 = [bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = '\rz"3`fn,](C'
    var_0 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ""
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "s*:GX"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()

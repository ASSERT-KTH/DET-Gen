# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2335 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x0e\x8148\xb6\xe3d\xa8B\xf8\xf3\xf8\x84;\x12\xa8\xe8\x7f\xf7"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b""
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "Y!sl+ly-Y+\tVw'"
    var_0 = module_0.func(*str_0)
    assert var_0 == ""
    module_0.func()

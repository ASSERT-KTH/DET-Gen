# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_63 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "1DH|kJ.Ka0BX`bFK"
    var_0 = module_0.func(*str_0)
    assert var_0 == 1
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"OM?=\x9d\xfc`\xc0;\xe8\xe7B\xfe\xcc\xaf"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 1
    module_0.func()

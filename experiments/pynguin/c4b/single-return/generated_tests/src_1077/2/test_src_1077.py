# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1077 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "Ds`x~L{"
    bytes_0 = b"\xed\x8e\xd0{S\xe6\xc6\xf1;8\xd3y\xf9\xf2\xb1\x80\xd1,"
    list_0 = [str_0, str_0, bytes_0, str_0]
    module_0.func(*list_0)

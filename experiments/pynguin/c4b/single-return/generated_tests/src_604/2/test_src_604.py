# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_604 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = ",|K,01;_X\x0cPBmQT3x%-"
    set_0 = {str_0, str_0, str_0, str_0}
    list_0 = [str_0, set_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"-\xbd\xfc-\x93\x0f,\xae\xd2=z;\xe0\xda\xb4\x91"
    module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "0j |zIQM"
    module_0.func(*str_0)
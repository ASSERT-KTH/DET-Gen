# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import hanoi as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    var_0 = module_0.hanoi(bool_0)
    bool_1 = True
    bool_2 = False
    str_0 = "\x0b17;\tL0tFSwv"
    dict_0 = {bool_2: bool_1, bool_0: str_0, bool_2: bool_0, bool_2: var_0}
    bool_3 = True
    var_1 = module_0.hanoi(bool_3)
    module_0.hanoi(dict_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xcfgD\xc7\r\x10\xeaj\x95Y\x05m\x9a\xac\x1dS\xe0"
    module_0.hanoi(bytes_0, bytes_0)

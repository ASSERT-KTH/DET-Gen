# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shunting_yard as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "Mv'#}"
    module_0.shunting_yard(str_0)


def test_case_1():
    str_0 = "$"
    var_0 = module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"\x9ad\xb2\xb7"
    var_0 = module_0.shunting_yard(bytes_0)
    list_0 = [var_0, bytes_0, var_0, var_0]
    module_0.shunting_yard(list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = False
    module_0.shunting_yard(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "**2JB5GZzBr"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "*+/D1!`KZa:\n%Rt?o4["
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "+*/D1!`KZa:\nRto4["
    module_0.shunting_yard(str_0)
# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shunting_yard as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "(E"
    module_0.shunting_yard(str_0)


def test_case_1():
    str_0 = "u"
    var_0 = module_0.shunting_yard(str_0)


def test_case_2():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.shunting_yard(list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "+/?vY"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "+/+]Zv"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    bytes_0 = b"\\`1\xdf\xfeDr<{c\xfer\xcf\x9dK\xa2\x86\xe7"
    set_0 = {bytes_0, bytes_0}
    var_0 = module_0.shunting_yard(set_0)
    var_1 = module_0.shunting_yard(set_0)
    var_2 = module_1.object()
    str_0 = "+/*/Zv"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    bytes_0 = b"\\`1\xdf\xfeD'<{\x06\xfer\xcf\x9dK\xa2\x86\xe7"
    set_0 = {bytes_0, bytes_0}
    var_0 = module_0.shunting_yard(set_0)
    var_1 = module_0.shunting_yard(set_0)
    bytes_1 = b""
    var_2 = module_0.shunting_yard(bytes_1)
    str_0 = "+/"
    var_3 = module_0.shunting_yard(str_0)
    var_4 = module_0.shunting_yard(var_3)
    none_type_0 = None
    module_0.shunting_yard(none_type_0)

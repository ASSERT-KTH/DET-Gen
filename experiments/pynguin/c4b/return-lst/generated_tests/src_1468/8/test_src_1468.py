# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1468 as module_0
import builtins as module_1


def test_case_0():
    bytes_0 = b"_\x7f\xea\xc3}\x1a\xe4?\x18"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "4`Ck!4$7$7?"
    set_0 = {str_0, str_0}
    var_0 = module_0.func(*set_0)
    var_1 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "4`7:\t4k44$7$7?2"
    set_0 = {str_0, str_0}
    var_0 = module_0.func(*set_0)
    var_1 = module_0.func(*var_0)
    module_1.object(*var_1, **var_1)

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_954 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = '5j_(P2 IrO\x0c"'
    var_0 = module_0.func(*str_0)
    assert var_0 == "I hate that I love that I hate that I love that I hate it"
    list_0 = [str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()

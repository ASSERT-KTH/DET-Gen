# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1014 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "3qUBRemQ@]nX\x0cO`Wu,/G"
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "46$\x0c\x0bX]d~\\,s~v=?/"
    var_0 = module_0.func(*str_0)
    assert var_0 == 6
    module_0.func()

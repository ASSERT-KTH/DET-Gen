# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2320 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "H-\\jbbt1Fi\x0cQHmy\\_+JG"
    set_0 = {str_0}
    list_0 = [set_0, set_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "!=qDAA'"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".!.=.q.d.'"
    var_1 = module_0.func(*list_0)
    assert var_1 == ".!.=.q.d.'"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1770 as module_0


def test_case_0():
    bool_0 = False
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 975
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    assert (
        var_0
        == 315436323920995170232878281130744095246441710926635203629660396207068723222727680084607028452468908070604669528578235771762206410196893748099636292807047965883388396592191119030857719568902056489883417241735340487383455433649181312243918297505499478956008249578879255643944627800858275944071168
    )
    module_0.func()

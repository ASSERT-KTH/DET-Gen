# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2325 as module_0


def test_case_0():
    str_0 = "<u9'?$~<v}EbGr|Iru2x"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".<.9.'.?.$.~.<.v.}.b.g.r.|.r.2.x"


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()

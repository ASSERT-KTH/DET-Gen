# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1537 as module_0


def test_case_0():
    str_0 = "@3XM':T\"6d\x0bg\r[gUZv*g"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".@.3.x.m.'.:.t.\".6.d.\x0b.g.\r.[.g.z.v.*.g"


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_515 as module_0
import builtins as module_1


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    str_0 = "^L-S"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".^.l.-.s"


def test_case_2():
    str_0 = "^L-Sy"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".^.l.-.s"


#@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "\x0bu({Ea"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".\x0b.(.{"
#    module_1.object(**var_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "B{DL_gZR~Wn)OHwS\r:)]"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".b.{.d.l._.g.z.r.~.w.n.).h.w.s.\r.:.).]"
    var_1 = module_0.func(*str_0)
    assert var_1 == ".b"
    var_2 = module_1.object()
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "I?=!*:-v!Y=!u2"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".?.=.!.*.:.-.v.!.=.!.2"
#    module_0.func()

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_525 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b'\xf3\xb2\x9fd"\xe4q\xcc='
    list_0 = [bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "\t2ZmB#fe9tF"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".\t.2.z.m.b.#.f.9.t.f"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    complex_0 = 165.910202 + 420.6j
    module_0.func(*complex_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "fI\\evjL[P$\x0bou0H"
    complex_0 = 327.9 + 217.03480703966943j
    list_0 = [str_0, str_0, complex_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".f.\\.v.j.l.[.p.$.\x0b.0.h"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "71<hAA$Olzzo\nl"
    complex_0 = 346.95899004101386 + 217.91j
    list_0 = [str_0, str_0, complex_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".7.1.<.h.$.l.z.z.\n.l"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "yy7%x0-\ri\\4h4F}B\\4("
    complex_0 = 327.9 + 217.82315319599593j
    list_0 = [str_0, str_0, complex_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".7.%.x.0.-.\r.\\.4.h.4.f.}.b.\\.4.("
    module_1.object(**var_0)

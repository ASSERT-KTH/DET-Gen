# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2396 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "nX0.u"
    var_0 = module_0.func(*str_0)
    assert var_0 == ".n"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "nX0&.u"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".n.x.0.&.."
    var_1 = module_0.func(*list_0)
    assert var_1 == ".n.x.0.&.."
    dict_0 = {str_0: str_0, str_0: str_0}
    var_2 = module_0.func(*var_0)
    assert var_2 == ".."
    list_1 = [list_0, str_0, dict_0, str_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "y |KR neEg\x0c_y=sC\tx1r"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ". .|.k.r. .n.g.\x0c._.=.s.c.\t.x.1.r"
    module_1.object(**var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "oX\t&.u"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".x.\t.&.."
    var_1 = module_0.func(*list_0)
    assert var_1 == ".x.\t.&.."
    dict_0 = {str_0: str_0, str_0: str_0}
    var_2 = module_0.func(*var_0)
    assert var_2 == ".."
    list_1 = [list_0, dict_0, list_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "5PC.5w\\2MAadzl"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".5.p.c...5.w.\\.2.m.d.z.l"
    object_0 = module_1.object()
    var_1 = module_0.func(*list_0)
    assert var_1 == ".5.p.c...5.w.\\.2.m.d.z.l"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = 'r"\r|M^bI+z4l*'
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == '.r.".\r.|.m.^.b.+.z.4.l.*'
    object_0 = module_1.object()
    module_0.func()

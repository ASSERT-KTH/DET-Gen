# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2388 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    list_0 = [dict_0, dict_0, dict_0, dict_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    dict_0 = {}
    bool_0 = True
    list_0 = [dict_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "y=GB:,`$tqG"
    none_type_0 = None
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".].g.b.Z.L.\x80.D.t.q.g"
    list_1 = [none_type_0, none_type_0, none_type_0]
    module_0.func(*list_1)

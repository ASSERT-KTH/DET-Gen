# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2265 as module_0


def test_case_0():
    str_0 = ";9#&\x0c?wzQ2\\rS\\E7b"
    var_0 = module_0.func(*str_0)
    assert var_0 == ".;"


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = 'rLI{"KD'
    bool_0 = False
    tuple_0 = (str_0, bool_0, bool_0, bool_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == '.r.l.{.".k.d'
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "E%uz6' 20\"a#M"
    bool_0 = False
    tuple_0 = (str_0, bool_0, bool_0, bool_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == ".%.z.6.'. .2.0.\".#.m"
    bytes_0 = b"3&\xc7"
    set_0 = {bytes_0}
    list_0 = [bytes_0, set_0, bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "y&\\"
    bool_0 = False
    tuple_0 = (str_0, bool_0, bool_0, bool_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == ".&.\\"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = ";9#&\x0c?wQ2\\rS\\E7"
    dict_0 = {str_0: str_0}
    var_0 = module_0.func(*str_0)
    assert var_0 == ".;"
    var_1 = module_0.func(*dict_0)
    assert var_1 == ".;.9.#.&.\x0c.?.w.q.2.\\.r.s.\\.7"
    var_2 = module_0.func(*var_1)
    assert var_2 == ".."
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "'N&jlD*O"
    dict_0 = {str_0: str_0, str_0: str_0, str_0: str_0}
    tuple_0 = (str_0, dict_0)
    var_0 = module_0.func(*tuple_0)
    assert var_0 == ".'.n.&.j.l.d.*"
    str_1 = "w+(LiO2^pU'|0X\to"
    var_1 = module_0.func(*str_1)
    assert var_1 == ".w"
    var_2 = module_0.func(*var_1)
    assert var_2 == ".."
    module_0.func()

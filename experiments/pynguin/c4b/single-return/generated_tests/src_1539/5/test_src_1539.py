# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1539 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "M1<u^fFt.&"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "M1<u^fFt.&"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    tuple_0 = ()
    list_0 = [tuple_0, tuple_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "M1<u^fFt.&"
    dict_0 = {str_0: str_0, str_0: str_0}
    list_0 = [dict_0, str_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "k<L\x0bt$;_VQl,s&<"
    var_0 = module_0.func(*str_0)
    assert var_0 == "K"
    var_1 = module_0.func(*var_0)
    assert var_1 == "k"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = ';ZOD\x0b(SCQ~x"U\n'
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ';ZOD\x0b(SCQ~x"U\n'
    var_1 = module_0.func(*var_0)
    assert var_1 == ";"
    module_0.func()

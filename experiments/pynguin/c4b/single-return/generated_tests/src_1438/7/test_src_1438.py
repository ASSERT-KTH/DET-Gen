# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1438 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "K=|' Ej"
    var_0 = module_0.func(*str_0)
    assert var_0 == "k"
    module_1.object(**var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "K=| Ej"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "k=| Ej"
    var_1 = module_0.func(*list_0)
    assert var_1 == "k=| Ej"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "K=|' Ej"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "k=|' Ej"
    dict_0 = {var_0: str_0}
    var_1 = module_0.func(*dict_0)
    assert var_1 == "k=|' Ej"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "D R"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "d r"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "uL/ oK\nc@XO^8"
    var_0 = module_0.func(*str_0)
    assert var_0 == "U"
    list_0 = [str_0, str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == "Ul/ oK\nc@XO^8"
    list_1 = [var_1, str_0, var_1, str_0]
    var_2 = module_0.func(*list_1)
    assert var_2 == "Ul/ oK\nc@XO^8"
    module_0.func()

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_472 as module_0
import builtins as module_1


def test_case_0():
    str_0 = "~$^Vq@:YJ0#,Iod<Wb>G"
    float_0 = 141.37
    list_0 = [str_0, str_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = ".HL8Nf=xFf"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = 'aVVcMHGXbwn4"'
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    var_1 = module_0.func(*str_0)
    assert var_1 == 0
    module_1.object(**list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "/Q\r"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    var_1 = module_0.func(*str_0)
    assert var_1 == 0
    module_1.object(**list_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "KV"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0
    list_0 = [str_0, str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 0
    var_2 = module_0.func(*str_0)
    assert var_2 == 0
    module_1.object(**list_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "{VdWJ2FvKK|ixCl"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    var_1 = module_0.func(*str_0)
    assert var_1 == 0
    module_0.func()

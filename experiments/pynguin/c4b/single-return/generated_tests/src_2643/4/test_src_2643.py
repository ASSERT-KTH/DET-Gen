# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2643 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "KV>FK\x0c!%"
    var_0 = module_0.func(*str_0)
    assert var_0 == 0
    list_0 = [str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == 0


def test_case_2():
    str_0 = "KV>FK\x0c!%"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


def test_case_3():
    str_0 = "$*1.TR2}oZdH|W{U\t"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


def test_case_4():
    str_0 = "KVVF\x0c!%g"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "KVK\x0c~"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    object_0 = module_1.object()
    module_0.func(*var_0)


def test_case_6():
    str_0 = "KKVVF\x0c!%g"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1


def test_case_7():
    str_0 = "d'[&[ls,-V"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "KKVVV\x0c!%g"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    module_0.func(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = "KKKVF\x0c^%g"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 1
    module_0.func()


def test_case_10():
    str_0 = "d'[,[ls,VV"
    list_0 = [str_0]
    var_0 = module_0.func(*str_0)
    assert var_0 == 0
    var_1 = module_0.func(*list_0)
    assert var_1 == 1

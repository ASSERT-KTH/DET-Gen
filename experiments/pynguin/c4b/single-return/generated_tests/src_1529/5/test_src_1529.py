# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1529 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    list_0 = []
    list_1 = [list_0]
    list_2 = [list_1, list_1, list_1]
    module_0.func(*list_2)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xf1x\xc9T{\xf1"
    list_0 = [bytes_0, bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "I#"
    list_0 = [str_0, str_0, str_0]
    list_1 = [list_0, str_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "I#"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "i#"
    list_1 = [list_0, var_0]
    module_0.func(*list_1)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "zS(/DerZl"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "zS(/DerZl"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "zS(/DerZl"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "zS(/DerZl"
    object_0 = module_1.object()
    var_1 = module_0.func(*var_0)
    assert var_1 == "Z"
    module_0.func()


def test_case_7():
    str_0 = "#"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "#"


@pytest.mark.xfail(strict=True)
def test_case_8():
    str_0 = "PS(/EYerZl"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "PS(/EYerZl"
    object_0 = module_1.object()
    var_1 = module_0.func(*var_0)
    assert var_1 == "p"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_9():
    str_0 = "z(Z"
    var_0 = module_0.func(*str_0)
    assert var_0 == "Z"
    list_0 = [str_0, str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == "Z(z"
    var_2 = module_1.object()
    module_0.func()

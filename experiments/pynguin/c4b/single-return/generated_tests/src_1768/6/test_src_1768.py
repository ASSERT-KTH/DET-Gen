# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1768 as module_0


def test_case_0():
    str_0 = "v9^"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "v9^"


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "<$)QnT5-\rrf.\t}KQY&"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "<$)QnT5-\rrf.\t}KQY&"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "L9rO6+p[\x0c$%@MqQN9YH9"
    var_0 = module_0.func(*str_0)
    assert var_0 == "l"
    var_1 = module_0.func(*var_0)
    assert var_1 == "L"
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "U["
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "u["
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "vK^"
    var_0 = module_0.func(*str_0)
    assert var_0 == "V"
    list_0 = [str_0, str_0, str_0, str_0]
    var_1 = module_0.func(*list_0)
    assert var_1 == "Vk^"
    module_0.func()

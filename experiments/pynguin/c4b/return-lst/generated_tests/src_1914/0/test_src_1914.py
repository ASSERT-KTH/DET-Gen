# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1914 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "[Cocp\\OKE\tHg"
    list_0 = [str_0]
    str_1 = "J7hQ&YYS{kw3zBUV)*em"
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_1)


def test_case_2():
    bytes_0 = b"\t\x82\x96Ix\xd9C\x89\xd1^^l\xfaU\x96|%"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


def test_case_3():
    str_0 = "J7hQ&YYS{kw3zBUV)*em"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_4():
    str_0 = "\\mDQLK,MiF$[@j"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_5():
    str_0 = "[Coch\\VKKG\tH&"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


def test_case_6():
    str_0 = "[Cocp\\OKKG\tH&"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


def test_case_7():
    str_0 = "[Coc\\ZVVKKG\t&"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_188 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = 'C~E/!0Gl-07{"w021\x0c4'
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = 'C~E/!00Gl-07{"w021\x0c4'
    list_0 = [str_0, str_0, str_0, str_0]
    module_0.func(*list_0)

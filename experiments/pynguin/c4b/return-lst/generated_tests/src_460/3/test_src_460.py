# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_460 as module_0


def test_case_0():
    bool_0 = True
    dict_0 = {bool_0: bool_0, bool_0: bool_0}
    list_0 = [dict_0, dict_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "\n3]I\rhFhSD\x0bRT*"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*str_0)
    module_0.func()

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import builtins as module_0
import src_247 as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "6m|"
    object_0 = module_0.object()
    list_0 = [str_0, str_0, object_0]
    module_1.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_1.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "6m-"
    module_1.func(*str_0)

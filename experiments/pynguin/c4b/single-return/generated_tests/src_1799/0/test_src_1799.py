# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1799 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"b[\x15.K"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    list_0 = [bool_0]
    var_0 = module_0.func(*list_0)
    module_1.object(**var_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"S\xc5\t\x0f\xd8\x99\xd5\\\x94_\x90R\xfe\xf8\xfc=\x97s"
    var_0 = module_0.func(*bytes_0)
    module_0.func()

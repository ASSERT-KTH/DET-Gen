# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2353 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"~X\x87\x94"
    var_0 = module_0.func(*bytes_0)
    module_1.object(*var_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"%_\xd9h\xc7K\xed\xfa\xcd\xd8\xf4\xe1p\x8eu\x96\xb6\xd9s"
    var_0 = module_0.func(*bytes_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\x04\x86\x96\xb6\xcaA\xeb\x8bE\t"
    bool_0 = False
    list_0 = [bool_0, bytes_0, bool_0]
    var_0 = module_0.func(*list_0)
    object_0 = module_1.object()
    module_1.object(**var_0)
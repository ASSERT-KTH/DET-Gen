# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2593 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    bytes_0 = b"g=\xa9Kv\x965O|vj\xd1@\xf5\xd5\xc5\xc8\x18"
    var_0 = module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 109
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_4():
    int_0 = 397
    str_0 = 's&2z\t\\.`0"D?.q"e%$+O'
    dict_0 = {int_0: int_0, int_0: int_0, int_0: str_0, str_0: str_0}
    list_0 = [int_0, int_0, int_0, dict_0]
    var_0 = module_0.func(*list_0)
    module_0.func(*int_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    int_0 = 1074
    list_0 = [int_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_6():
    int_0 = 108
    list_0 = [int_0, int_0, int_0]
    var_0 = module_0.func(*list_0)
    int_1 = 456
    list_1 = [int_1]
    var_1 = module_0.func(*list_1)
    var_2 = module_0.func(*var_0)
    object_0 = module_1.object()
    var_3 = module_0.func(*var_2)
    module_0.func()

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1803 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    none_type_0 = None
    list_0 = [none_type_0, none_type_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    object_0 = module_1.object()
    list_0 = [object_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == 0


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"U\xa3\xc7\xbeR_\x14\x89]\xf1\xac7\x92"
    set_0 = {bytes_0, bytes_0}
    list_0 = [bytes_0, set_0, set_0, set_0]
    int_0 = -1834
    tuple_0 = (set_0, list_0, int_0)
    list_1 = [tuple_0, int_0, int_0, int_0]
    var_0 = module_0.func(*list_1)
    assert var_0 == 1
    module_0.func()

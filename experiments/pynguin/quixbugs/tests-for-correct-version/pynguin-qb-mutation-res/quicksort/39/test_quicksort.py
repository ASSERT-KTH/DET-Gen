# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import quicksort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    int_0 = -3233
    module_0.quicksort(int_0)


def test_case_1():
    none_type_0 = None
    var_0 = module_0.quicksort(none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    list_0 = []
    tuple_0 = (list_0,)
    tuple_1 = (tuple_0, list_0, list_0)
    module_0.quicksort(tuple_1)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"Z\xec\xca:\xf2\x98\x80J\xd5"
    var_0 = module_0.quicksort(bytes_0)
    set_0 = {bytes_0, bytes_0, bytes_0, bytes_0}
    var_1 = module_0.quicksort(bytes_0)
    module_0.quicksort(set_0)
# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2230 as module_0


def test_case_0():
    bytes_0 = b"\xa7\x10h\xf5\xfe:\x02\x98"
    tuple_0 = (bytes_0,)
    var_0 = module_0.func(*tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "uT:\tLe9VJX [hac<i."
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    none_type_0 = None
    module_0.func(*none_type_0)

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1572 as module_0


#@pytest.mark.xfail(strict=True)
#def test_case_0():
#    module_0.func()


def test_case_1():
    int_0 = 1280
    bytes_0 = b"O\x1e\xd0(\xa7\xb0#g\x8b"
    str_0 = "pq@WdBD@+-%'Ndp"
    dict_0 = {bytes_0: bytes_0, int_0: bytes_0, bytes_0: str_0, str_0: str_0}
    tuple_0 = (bytes_0, int_0, int_0, dict_0)
    list_0 = [int_0, tuple_0]
    var_0 = module_0.func(*list_0)

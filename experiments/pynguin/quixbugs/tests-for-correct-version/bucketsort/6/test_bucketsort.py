# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bucketsort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    bytes_0 = b"\x99\xd0\xa0\xad"
    dict_0 = {bool_0: bytes_0, bool_0: bool_0, bool_0: bool_0}
    str_0 = ",0]ZBh0t(:\nj"
    tuple_0 = (dict_0, str_0)
    module_0.bucketsort(tuple_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    none_type_0 = None
    module_0.bucketsort(none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = False
    bytes_0 = b""
    var_0 = module_0.bucketsort(bytes_0, bool_0)
    var_1 = module_0.bucketsort(bytes_0, bool_0)
    module_0.bucketsort(bool_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    bytes_0 = b""
    var_0 = module_0.bucketsort(bytes_0, bool_0)
    module_0.bucketsort(var_0, var_0)

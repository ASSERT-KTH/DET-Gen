# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import bucketsort as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    set_0 = {bool_0, bool_0, bool_0, bool_0}
    module_0.bucketsort(set_0, bool_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\x00\x91\xde\x01W\x1e\xf22\x06\x96\xd9\x08\xef"
    module_0.bucketsort(bytes_0, bytes_0)


def test_case_2():
    dict_0 = {}
    bool_0 = False
    var_0 = module_0.bucketsort(dict_0, bool_0)


def test_case_3():
    dict_0 = {}
    bool_0 = True
    var_0 = module_0.bucketsort(dict_0, bool_0)
# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import subsequences as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = False
    var_0 = module_0.subsequences(bool_0, bool_0, bool_0)
    none_type_0 = None
    module_0.subsequences(none_type_0, none_type_0, none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b":\x9c,>"
    module_0.subsequences(bytes_0, bytes_0, bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = -2174
    int_1 = -1158
    module_0.subsequences(int_1, int_1, int_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    int_0 = 3856
    var_0 = module_0.subsequences(int_0, int_0, int_0)
    module_0.subsequences(int_0, var_0, var_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    bool_0 = False
    bool_1 = False
    bool_2 = True
    var_0 = module_0.subsequences(bool_1, bool_1, bool_1)
    var_1 = module_0.subsequences(bool_0, bool_2, bool_2)
    set_0 = set()
    module_0.subsequences(set_0, set_0, bool_2)
# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2511 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    none_type_0 = None
    module_0.func(*none_type_0)


def test_case_1():
    bool_0 = False
    dict_0 = {bool_0: bool_0, bool_0: bool_0, bool_0: bool_0}
    var_0 = module_0.func(*dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"\xedL\xd9\xa5>\x08\xc5\xfa\xfc\xa8\xfc a\xf5\xd5\x9b<"
    bytes_1 = b"\xc1\xbd\xac\xdb\xb7D\x1b"
    list_0 = [bytes_0, bytes_1]
    var_0 = module_0.func(*bytes_1)
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "3Z1;~oQ"
    var_0 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "2Z;Q"
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*var_0)
    module_0.func()

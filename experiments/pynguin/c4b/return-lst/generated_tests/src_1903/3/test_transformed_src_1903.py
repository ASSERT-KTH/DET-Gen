# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1903 as module_0


def test_case_0():
    bytes_0 = b"\tBB\x08\xc7\xd7\xb6\xe5\xab\x1de\x02,\x05"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "8\x0bU2II2]86\x0b"
    str_1 = ""
    list_0 = [str_1]
    var_0 = module_0.func(*list_0)
    list_1 = [str_0, str_0, str_1]
    var_1 = module_0.func(*list_1)
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_3():
    bool_0 = True
    tuple_0 = (bool_0, bool_0, bool_0, bool_0)
    list_0 = [
        tuple_0,
        tuple_0,
        tuple_0,
        tuple_0,
        tuple_0,
        tuple_0,
        tuple_0,
        bool_0,
        tuple_0,
        tuple_0,
        tuple_0,
        bool_0,
        bool_0,
    ]
    list_1 = [list_0, tuple_0, tuple_0, bool_0, list_0, tuple_0, tuple_0]
    var_0 = module_0.func(*list_1)
#    module_0.func(*bool_0)


#@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "nUVE9o_iqDEtsr"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*list_0)
    list_1 = [list_0, var_1, str_0]
    var_2 = module_0.func(*list_1)
#    module_0.func()
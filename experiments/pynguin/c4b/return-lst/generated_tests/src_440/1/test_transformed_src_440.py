# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import src_440 as module_0


def test_case_0():
    str_0 = "[\tW"
    var_0 = module_0.func(*str_0)


def test_case_1():
    bytes_0 = b"m\x98QA"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)


def test_case_2():
    str_0 = "[\tW"
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*var_0)


def test_case_3():
    str_0 = "LL"
    tuple_0 = (str_0,)
    list_0 = [str_0, tuple_0]
    var_0 = module_0.func(*list_0)

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2342 as module_0


def test_case_0():
    str_0 = "ub`5f&A;yb15R"
    var_0 = module_0.func(*str_0)


def test_case_1():
    str_0 = "ub`5f&A;yb15R"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


def test_case_2():
    str_0 = "1b55f&A;yb15R"
    var_0 = module_0.func(*str_0)


def test_case_3():
    bytes_0 = b""
    str_0 = "@\t.."
    list_0 = [bytes_0, str_0, bytes_0]
    var_0 = module_0.func(*list_0)
    str_1 = "0r%M H001MY1"
    list_1 = [str_1]
    var_1 = module_0.func(*list_1)


def test_case_4():
    str_0 = "0%M 0v0111Y1"
    var_0 = module_0.func(*str_0)


def test_case_5():
    str_0 = "0W000M 000111Y1\rs1"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "0W000M 001111Y11\rs1"
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    module_0.func()

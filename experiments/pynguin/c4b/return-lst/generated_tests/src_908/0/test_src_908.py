# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_908 as module_0


def test_case_0():
    bytes_0 = b".zu\xd6\x8el-\x83!4U\x7f.\x83\x0c/\x85cb#"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


def test_case_2():
    bytes_0 = b"..zu\xd6\x8el-\x83!4U\x7f.\x83\x0c\x85cb#"
    list_0 = [bytes_0, bytes_0, bytes_0]
    var_0 = module_0.func(*list_0)


def test_case_3():
    str_0 = "PPPPPPPR6"
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)

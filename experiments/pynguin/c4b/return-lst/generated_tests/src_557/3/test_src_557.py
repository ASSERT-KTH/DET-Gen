# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_557 as module_0


def test_case_0():
    bytes_0 = b"V\xbb\xa1\xd4"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "#totQ`DQ`qZH!s"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "{j B\r>K<\x0b0l9,`&B,O"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_0.func()
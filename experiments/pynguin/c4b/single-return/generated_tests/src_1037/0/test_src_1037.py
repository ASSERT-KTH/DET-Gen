# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1037 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xda\x998\x16\xc9c\x1a\x8b@\xd4;#`\x86\xf7\x89\x8b"
    list_0 = [bytes_0, bytes_0, bytes_0, bytes_0]
    module_0.func(*list_0)


def test_case_1():
    pass


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "\rGQ6<cG\r[:;."
    module_0.func(*str_0)

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1722 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xba\x92tp\x0c9\xb3\x0f\x8a%"
    list_0 = [bytes_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
    list_1 = []
    list_2 = [list_1, list_0]
    module_0.func(*list_2)


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = ""
    set_0 = {str_0, str_0, str_0, str_0}
    list_0 = [set_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "W$'4\tX$>"
    set_0 = {str_0, str_0, str_0}
    list_0 = [set_0, str_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = "o<zkr4slav5\x0b;pq"
    set_0 = {str_0, str_0}
    list_0 = [set_0, str_0]
    module_0.func(*list_0)

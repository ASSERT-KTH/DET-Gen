# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2062 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    str_0 = "Puw"
    module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xd3[\xec\n\xd3P"
    module_0.func(*bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "\t{Q6;\r8K"
    module_0.func(*str_0)

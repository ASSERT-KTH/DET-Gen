# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2558 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "81PX`N;/&n#\tB7"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "781PX`N;/&n#\tB7"
    module_0.func(*str_0)

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_283 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "hn12m_q/lB(P\x0cY"
    var_0 = module_0.func(*str_0)


def test_case_2():
    str_0 = "hIn12F_q/ClB(P\x0c(t<Y"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)


def test_case_3():
    str_0 = "_bhEhw)elqn`lo"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_474 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


def test_case_1():
    str_0 = "4\t.\r@@EE5"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "=kx\rPV>/kQ@L week"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0]
    module_0.func(*list_0)


def test_case_3():
    str_0 = "63 O%\rnpf\ns3:"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = "30 O%\rnJf\n3:"
    list_0 = [str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    module_1.object(*list_0)
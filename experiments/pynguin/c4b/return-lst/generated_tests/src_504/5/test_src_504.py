# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_504 as module_0


def test_case_0():
    str_0 = "O{U-cCn-$!=\x0bb3g:j:2"
    var_0 = module_0.func(*str_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "\rEa5#'&0\tB8FH2z-\"`"
    none_type_0 = None
    list_0 = [str_0]
    var_0 = module_0.func(*list_0)
    var_1 = module_0.func(*var_0)
    module_0.func(*none_type_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = "9N\tGyL*P#6[>e_8v."
    var_0 = module_0.func(*str_0)
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "Qa09ci\r#"
    var_0 = module_0.func(*str_0)
    var_1 = module_0.func(*var_0)
    module_0.func()

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shunting_yard as module_0


def test_case_0():
    bytes_0 = b"\xf2~\xa2z\x0c/\x85\x17\x94\xac\xc9'G\xe5-\xdd0"
    var_0 = module_0.shunting_yard(bytes_0)


def test_case_1():
    str_0 = "4"
    var_0 = module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.shunting_yard(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "w`}fxx<Tvbj<W\nw^U4"
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    str_0 = '++A3/}^)\\ni8R"+H'
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_5():
    str_0 = '++//}^)\\ni8"+H'
    module_0.shunting_yard(str_0)


@pytest.mark.xfail(strict=True)
def test_case_6():
    str_0 = "u"
    var_0 = module_0.shunting_yard(str_0)
    str_1 = "++/+W+}^)\\ni8K+H"
    var_1 = module_0.shunting_yard(var_0)
    module_0.shunting_yard(str_1)

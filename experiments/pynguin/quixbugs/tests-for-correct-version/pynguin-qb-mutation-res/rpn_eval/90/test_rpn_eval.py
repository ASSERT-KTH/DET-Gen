# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import rpn_eval as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x16\x9a\xe66\x85\x85Y\xb21\xa6\xccJ1P4\xdcm"
    module_0.rpn_eval(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b""
    module_0.rpn_eval(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bool_0 = True
    module_0.rpn_eval(bool_0)


@pytest.mark.xfail(strict=True)
def test_case_3():
    float_0 = 1861.326
    str_0 = "u)t;dAK$r#g(f|u\t+"
    set_0 = {float_0, float_0, str_0}
    module_0.rpn_eval(set_0)


@pytest.mark.xfail(strict=True)
def test_case_4():
    float_0 = 524.65
    list_0 = []
    object_0 = module_1.object(*list_0)
    set_0 = {object_0}
    str_0 = "]dFL/0>=rMbh%'Zk-"
    tuple_0 = (float_0, float_0, set_0, str_0)
    module_0.rpn_eval(tuple_0)
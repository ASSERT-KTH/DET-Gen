# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_514 as module_0


def test_case_0():
    str_0 = "ri\\@*KfZv\\h#\\ ,{Wts"
    list_0 = [str_0, str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".r.\\.@.*.k.f.z.v.\\.h.#.\\. .,.{.w.t.s"


#@pytest.mark.xfail(strict=True)
#def test_case_1():
#    module_0.func()

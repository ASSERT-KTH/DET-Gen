# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1537 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\xab\x1a"
    tuple_0 = (bytes_0,)
    list_0 = [tuple_0, tuple_0, tuple_0]
    module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    str_0 = '#H=gNG"yk$\x0b-B:u^"?;;'
    list_0 = [str_0, str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == '.#.h.=.g.n.g.".k.$.\x0b.-.b.:.^.".?.;.;'
    var_1 = module_0.func(*var_0)
    assert var_1 == ".."
    var_2 = module_0.func(*var_0)
    assert var_2 == ".."
    module_0.func()

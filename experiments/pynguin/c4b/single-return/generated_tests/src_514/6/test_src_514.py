# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_514 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"1\x7f\xccw\x10\xcfv]\xe6\xe1"
    complex_0 = -1029.07543 - 1406.29674j
    tuple_0 = (bytes_0, complex_0)
    module_0.func(*tuple_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "\\Bb="
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".\\.b.b.="
    var_1 = module_0.func(*var_0)
    assert var_1 == ".."
    var_2 = module_0.func(*list_0)
    assert var_2 == ".\\.b.b.="
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    str_0 = "%}@5Fs,xISq@E<oQ1;I"
    list_0 = [str_0, str_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ".%.}.@.5.f.s.,.x.s.q.@.<.q.1.;"
    module_1.object(*list_0)

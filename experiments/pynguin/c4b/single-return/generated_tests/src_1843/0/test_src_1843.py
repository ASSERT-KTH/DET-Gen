# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1843 as module_0
import builtins as module_1


@pytest.mark.xfail(strict=True)
def test_case_0():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"\xaed\xe9\x13|\xeb\x14;\xab\xb7\xaa\xd7\xd6 \xbc\xda\xc7\xe8o"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 7
    module_1.object(*var_0, **bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b";\x1e\xf4\x0b\xed"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 32
    var_1 = module_1.object()
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_3():
    bytes_0 = b"W\xe01G\xf7%F\xaf\x89\xb8In\xb0"
    var_0 = module_0.func(*bytes_0)
    assert var_0 == 11
    module_1.object(*var_0, **bytes_0)

# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import lcs_length as module_0


def test_case_0():
    str_0 = "P2sd8V\t%%(_HX6\x0by*"
    var_0 = module_0.lcs_length(str_0, str_0)
    assert var_0 == 17


@pytest.mark.xfail(strict=True)
def test_case_1():
    str_0 = "/dOnj3Fa\tS HBJH c"
    none_type_0 = None
    bytes_0 = b"\xd7\xf7\x16\x14\xaa,Q\xae\xfa\xfd\xf9\x95\x0e5\xa8"
    int_0 = 163
    tuple_0 = (bytes_0, int_0)
    var_0 = module_0.lcs_length(str_0, tuple_0)
    assert var_0 == 0
    module_0.lcs_length(str_0, none_type_0)
# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2444 as module_0


def test_case_0():
    bytes_0 = b"gEe\xd42"
    list_0 = [bytes_0]
    var_0 = module_0.func(*list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    bytes_0 = b"gEe\xd42"
    list_0 = [bytes_0]
    str_0 = "M=Ra|pk:l_\\=pH/#wu"
    str_1 = "R0C'X4`;?QOPP<$q h"
    str_2 = "omoWa||b;;N5n\x0c5+3"
    dict_0 = {str_0: list_0, str_1: bytes_0, str_2: str_0}
    module_0.func(*dict_0)
# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import shortest_paths as module_0


def test_case_0():
    none_type_0 = None
    list_0 = []
    var_0 = module_0.shortest_paths(none_type_0, list_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"#\xe2"
    dict_0 = {
        bytes_0: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
        bytes_0: bytes_0,
    }
    module_0.shortest_paths(bytes_0, dict_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.shortest_paths(none_type_0, none_type_0)
# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import next_permutation as module_0


def test_case_0():
    bytes_0 = b"C\n]\xca-P-\x04"
    var_0 = module_0.next_permutation(bytes_0)


@pytest.mark.xfail(strict=True)
def test_case_1():
    bytes_0 = b"C\n]\xca-P-\x04"
    set_0 = {bytes_0, bytes_0, bytes_0}
    var_0 = module_0.next_permutation(set_0)
    module_0.next_permutation(var_0)


@pytest.mark.xfail(strict=True)
def test_case_2():
    none_type_0 = None
    module_0.next_permutation(none_type_0)

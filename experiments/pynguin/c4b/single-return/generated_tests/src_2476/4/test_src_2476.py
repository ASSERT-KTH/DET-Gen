# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_2476 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b'\xac\x1eR"\xcdK\xc7.\xd6\x18\xe7\xf0\x02\x91\x99\xaf\x87\x84'
    var_0 = module_0.func(*bytes_0)
    assert (
        var_0
        == "172 1 2 3 4 5 6 7 8 9 10 11 12 13 14 15 16 17 18 19 20 21 22 23 24 25 26 27 28 29 30 31 32 33 34 35 36 37 38 39 40 41 42 43 44 45 46 47 48 49 50 51 52 53 54 55 56 57 58 59 60 61 62 63 64 65 66 67 68 69 70 71 72 73 74 75 76 77 78 79 80 81 82 83 84 85 86 87 88 89 90 91 92 93 94 95 96 97 98 99 100 101 102 103 104 105 106 107 108 109 110 111 112 113 114 115 116 117 118 119 120 121 122 123 124 125 126 127 128 129 130 131 132 133 134 135 136 137 138 139 140 141 142 143 144 145 146 147 148 149 150 151 152 153 154 155 156 157 158 159 160 161 162 163 164 165 166 167 168 169 170 171 "
    )
    var_1 = module_0.func(*var_0)
    assert var_1 == "1 "
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    bool_0 = True
    list_0 = [bool_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == "1 "
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    module_0.func()

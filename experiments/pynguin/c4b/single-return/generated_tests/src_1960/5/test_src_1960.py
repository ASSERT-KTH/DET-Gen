# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1960 as module_0


@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = -4737.9
    list_0 = [float_0, float_0, float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_1():
    module_0.func()


@pytest.mark.xfail(strict=True)
def test_case_2():
    int_0 = 2292
    list_0 = [int_0, int_0]
    var_0 = module_0.func(*list_0)
    assert (
        var_0
        == "2 4 7 11 16 22 29 37 46 56 67 79 92 106 121 137 154 172 191 211 232 254 277 301 326 352 379 407 436 466 497 529 562 596 631 667 704 742 781 821 862 904 947 991 1036 1082 1129 1177 1226 1276 1327 1379 1432 1486 1541 1597 1654 1712 1771 1831 1892 1954 2017 2081 2146 2212 2279 55 124 194 265 337 410 484 559 635 712 790 869 949 1030 1112 1195 1279 1364 1450 1537 1625 1714 1804 1895 1987 2080 2174 2269 73 170 268 367 467 568 670 773 877 982 1088 1195 1303 1412 1522 1633 1745 1858 1972 2087 2203 28 146 265 385 506 628 751 875 1000 1126 1253 1381 1510 1640 1771 1903 2036 2170 13 149 286 424 563 703 844 986 1129 1273 1418 1564 1711 1859 2008 2158 17 169 322 476 631 787 944 1102 1261 1421 1582 1744 1907 2071 2236 110 277 445 614 784 955 1127 1300 1474 1649 1825 2002 2180 67 247 428 610 793 977 1162 1348 1535 1723 1912 2102 1 193 386 580 775 971 1168 1366 1565 1765 1966 2168 79 283 488 694 901 1109 1318 1528 1739 1951 2164 86 301 517 734 952 1171 1391 1612 1834 2057 2281 214 440 667 895 1124 1354 1585 1817 2050 2284 227 463 700 938 1177 1417 1658 1900 2143 95 340 586 833 1081 1330 1580 1831 2083 44 298 553 809 1066 1324 1583 1843 2104 74 337 601 866 1132 1399 1667 1936 2206 185 457 730 1004 1279 1555 1832 2110 97 377 658 940 1223 1507 1792 2078 73 361 650 940 1231 1523 1816 2110 113 409 706 1004 1303 1603 1904 2206 217 521 826 1132 1439 1747 2056 74 385 697 1010 1324 1639 1955 2272 298 617 937 1258 1580 1903 2227 260 586 913 1241 1570 1900 2231 271 604 938 1273 1609 1946 2284 331 671 1012 1354 1697 2041 94 440 787 1135 1484 1834 2185 245 598 952 1307 1663 2020 86 445 805 1166 1528 1891 2255 328 694 1061 1429 1798 2168 247 619 992 1366 1741 2117 202 580 959 1339 1720 2102 193 577 962 1348 1735 2123 220 610 1001 1393 1786 2180 283 679 1076 1474 1873 2273 382 784 1187 1591 1996 110 517 925 1334 1744 2155 275 688 1102 1517 1933 58 476 895 1315 1736 2158 289 713 1138 1564 1991 127 556 986 1417 1849 2282 424 859 1295 1732 2170 317 757 1198 1640 2083 235 680 1126 1573 2021 178 628 1079 1531 1984 146 601 1057 1514 1972 139 599 1060 1522 1985 157 622 1088 1555 2023 200 670 1141 1613 2086 268 743 1219 1696 2174 361 841 1322 1804 2287 479 964 1450 1937 133 622 1112 1603 2095 296 790 1285 1781 2278 484 983 1483 1984 194 697 1201 1706 2212 427 935 1444 1954 173 685 1198 1712 2227 451 968 1486 2005 233 754 1276 1799 31 556 1082 1609 2137 374 904 1435 1967 208 742 1277 1813 58 596 1135 1675 2216 466 1009 1553 2098 352 899 1447 1996 254 805 1357 1910 172 727 1283 1840 106 665 1225 1786 56 619 1183 1748 22 589 1157 1726 4 575 1147 1720 2 577 1153 1730 16 595 1175 1756 46 629 1213 1798 92 679 1267 1856 154 745 1337 1930 232 827 1423 2020 326 925 1525 2126 436 1039 1643 2248 562 1169 1777 94 704 1315 1927 248 862 1477 2093 418 1036 1655 2275 604 1226 1849 181 806 1432 2059 395 1024 1654 2285 625 1258 1892 235 871 1508 2146 493 1133 1774 124 767 1411 2056 410 1057 1705 62 712 1363 2015 376 1030 1685 49 706 1364 2023 391 1052 1714 85 749 1414 2080 455 1123 1792 170 841 1513 2186 568 1243 1919 304 982 1661 49 730 1412 2095 487 1172 1858 253 941 1630 28 719 1411 2104 506 1201 1897 302 1000 1699 107 808 1510 2213 625 1330 2036 451 1159 1868 286 997 1709 130 844 1559 2275 700 1418 2137 565 1286 2008 439 1163 1888 322 1049 1777 214 944 1675 115 848 1582 25 761 1498 2236 683 1423 2164 614 1357 2101 554 1300 2047 503 1252 2002 461 1213 1966 428 1183 1939 404 1162 1921 389 1150 1912 383 1147 1912 386 1153 1921 398 1168 1939 419 1192 1966 449 1225 2002 488 1267 2047 536 1318 2101 593 1378 2164 659 1447 2236 734 1525 25 818 1612 115 911 1708 214 1013 1813 322 1124 1927 439 1244 2050 565 1373 2182 700 1511 31 844 1658 181 997 1814 340 1159 1979 508 1330 2153 685 1510 44 871 1699 236 1066 1897 437 1270 2104 647 1483 28 866 1705 253 1094 1936 487 1331 2176 730 1577 133 982 1832 391 1243 2096 658 1513 77 934 1792 359 1219 2080 650 1513 85 950 1816 391 1259 2128 706 1577 157 1030 1904 487 1363 2240 826 1705 293 1174 2056 647 1531 124 1010 1897 493 1382 2272 871 1763 364 1258 2153 757 1654 260 1159 2059 668 1570 181 1085 1990 604 1511 127 1036 1946 565 1477 98 1012 1927 551 1468 94 1013 1933 562 1484 115 1039 1964 598 1525 161 1090 2020 659 1591 232 1166 2101 745 1682 328 1267 2207 856 1798 449 1393 46 992 1939 595 1544 202 1153 2105 766 1720 383 1339 4 962 1921 589 1550 220 1183 2147 820 1786 461 1429 106 1076 2047 727 1700 382 1357 41 1018 1996 683 1663 352 1334 25 1009 1994 688 1675 371 1360 58 1049 2041 742 1736 439 1435 140 1138 2137 845 1846 556 1559 271 1276 2282 997 2005 722 1732 451 1463 184 1198 2213 937 1954 680 1699 427 1448 178 1201 2225 958 1984 719 1747 484 1514 253 1285 26 1060 2095 839 1876 622 1661 409 1450 200 1243 2287 1040 2086 841 1889 646 1696 455 1507 268 1322 85 1141 2198 964 2023 791 1852 622 1685 457 1522 296 1363 139 1208 2278 1057 2129 910 1984 767 1843 628 1706 493 1573 362 1444 235 1319 112 1198 2285 1081 2170 968 2059 859 1952 754 1849 653 1750 556 1655 463 1564 374 1477 289 1394 208 1315 131 1240 58 1169 2281 1102 2216 1039 2155 980 2098 925 2045 874 1996 827 1951 784 1910 745 1873 710 1840 679 1811 652 1786 629 1765 610 1748 595 1735 584 1726 577 1721 574 1720 575 1723 580 1730 589 1741 602 1756 619 1775 640 1798 665 1825 694 1856 727 1891 764 1930 805 1973 850 2020 899 2071 952 2126 1009 2185 1070 2248 1135 23 1204 94 1277 169 1354 248 1435 331 1520 418 1609 509 1702 604 1799 703 1900 806 2005 913 2114 1024 2227 1139 52 1258 173 1381 298 1508 427 1639 560 1774 697 1913 838 2056 983 2203 1132 62 1285 217 1442 376 1603 539 1768 706 1937 877 2110 1052 2287 1231 176 1414 361 1601 550 1792 743 1987 940 2186 1141 97 1346 304 1555 515 1768 730 1985 949 2206 1172 139 1399 368 1630 601 1865 838 2104 1079 55 1324 302 1573 553 1826 808 2083 1067 52 1330 317 1597 586 1868 859 2143 1136 130 1417 413 1702 700 1991 991 2284 1286 289 1585 590 1888 895 2195 1204 214 1517 529 1834 848 2155 1171 188 1498 517 1829 850 2164 1187 211 1528 554 1873 901 2222 1252 283 1607 640 1966 1001 37 1366 404 1735 775 2108 1150 193 1529 574 1912 959 7 1348 398 1741 793 2138 1192 247 1595 652 2002 1061 121 1474 536 1891 955 20 1378 445 1805 874 2236 1307 379 1744 818 2185 1261 338 1708 787 2159 1240 322 1697 781 2158 1244 331 1711 800 2182 1273 365 1750 844 2231 1327 424 1814 913 13 1406 508 1903 1007 112 1510 617 2017 1126 236 1639 751 2156 1270 385 1793 910 28 1439 559 1972 1094 217 1633 758 2176 1303 431 1852 982 113 1537 670 2096 1231 367 1796 934 73 1505 646 2080 1223 367 1804 950 97 1537 686 2128 1279 431 1876 1030 185 1633 790 2240 1399 559 2012 1174 337 1793 958 124 1583 751 2212 1382 553 2017 1190 364 1831 1007 184 1654 833 13 1486 668 2143 1327 512 1990 1177 365 1846 1036 227 1711 904 98 1585 781 2270 1468 667 2159 1360 562 2057 1261 466 1964 1171 379 1880 1090 301 1805 1018 232 1739 955 172 1682 901 121 1634 856 79 1595 820 46 1565 793 22 1544 775 7 1532 766 1 1529 766 4 1535 775 16 1550 793 37 1574 820 67 1607 856 106 1649 901 154 1700 955 211 1760 1018 277 1829 1090 352 1907 1171 436 1994 1261 529 2090 1360 631 2195 1468 742 17 1585 862 140 1711 991 272 1846 1129 413 1990 1276 563 2143 1432 722 13 1597 890 184 1771 1067 364 1954 1253 553 2146 1448 751 55 1652 958 265 1865 1174 484 2087 1399 712 26 1633 949 266 1876 1195 515 2128 1450 773 97 1714 1040 367 1987 1316 646 2269 1601 934 268 1895 1231 568 2198 1537 877 218 1852 1195 539 2176 1522 869 217 1858 1208 559 2203 1556 910 265 1913 1270 628 2279 1639 1000 362 2017 1381 746 112 1771 1139 508 2170 1541 913 286 1952 1327 703 80 1750 1129 509 2182 1564 947 331 2008 1394 781 169 1850 1240 631 23 1708 1102 497 2185 1582 980 379 2071 1472 874 277 1973 1378 784 191 1891 1300 710 121 1825 1238 652 67 1775 1192 610 29 1741 1162 584 7 1723 1148 574 1 1721 1150 580 11 1735 1168 602 37 1765 1202 640 79 1811 1252 694 137 1873 1318 764 211 1951 1400 850 301 2045 1498 952 407 2155 1612 1070 529 2281 1742 1204 667 131 1888 1354 821 289 2050 1520 991 463 2228 1702 1177 653 130 1900 1379 859 340 2114 1597 1081 566 52 1831 1319 808 298 2081 1573 1066 560 55 1843 1340 838 337 2129 1630 1132 635 139 1936 1442 949 457 2258 1768 1279 791 304 2110 1625 1141 658 176 1987 1507 1028 550 73 1889 1414 940 467 2287 1816 1346 877 409 2234 1768 1303 839 376 2206 1745 1285 826 368 2203 1747 1292 838 385 2225 1774 1324 875 427 2272 1826 1381 937 494 52 1903 1463 1024 586 149 2005 1570 1136 703 271 2132 1702 1273 845 418 2284 1859 1435 1012 590 169 2041 1622 1204 787 371 2248 1834 1421 1009 598 188 2071 1663 1256 850 445 41 1930 1528 1127 727 328 2222 1825 1429 1034 640 247 2147 1756 1366 977 589 202 2108 1723 1339 956 574 193 2105 1726 1348 971 595 220 2138 1765 1393 1022 652 283 2207 1840 1474 1109 745 382 20 1951 1591 1232 874 517 161 2098 1744 1391 1039 688 338 2281 1933 1586 1240 895 551 208 2158 1817 1477 1138 800 463 127 2084 1750 1417 1085 754 424 95 2059 1732 1406 1081 757 434 112 2083 1763 1444 1126 809 493 178 2156 1843 1531 1220 910 601 293 2278 1972 1667 1363 1060 758 457 157 2150 1852 1555 1259 964 670 377 85 2086 1796 1507 1219 932 646 361 77 2086 1804 1523 1243 964 686 409 133 2150 1876 1603 1331 1060 790 521 253 2278 2012 1747 1483 1220 958 697 437 178 2212 1955 1699 1444 1190 937 685 434 184 2227 1979 1732 1486 1241 997 754 512 271 31 2084 1846 1609 1373 1138 904 671 439 208 2270 2041 1813 1586 1360 1135 911 688 466 245 25 2098 1880 1663 1447 1232 1018 805 593 382 172 2255 2047 1840 1634 1429 1225 1022 820 619 419 220 22 2117 1921 1726 1532 1339 1147 956 766 577 389 202 16 2123 1939 1756 1574 1393 1213 1034 856 679 503 328 154 2273 2101 1930 1760 1591 1423 1256 1090 925 761 598 436 275 115 2248 2090 1933 1777 1622 1468 1315 1163 1012 862 713 565 418 272 127 2275 2132 1990 1849 1709 1570 1432 1295 1159 1024 890 757 625 494 364 235 107 2272 2146 2021 1897 1774 1652 1531 1411 1292 1174 1057 941 826 712 599 487 376 266 157 49 2234 2128 2023 1919 1816 1714 1613 1513 1414 1316 1219 1123 1028 934 841 749 658 568 479 391 304 218 133 49 2258 2176 2095 2015 1936 1858 1781 1705 1630 1556 1483 1411 1340 1270 1201 1133 1066 1000 935 871 808 746 685 625 566 508 451 395 340 286 233 181 130 80 31 2275 2228 2182 2137 2093 2050 2008 1967 1927 1888 1850 1813 1777 1742 1708 1675 1643 1612 1582 1553 1525 1498 1472 1447 1423 1400 1378 1357 1337 1318 1300 1283 1267 1252 1238 1225 1213 1202 1192 1183 1175 1168 1162 1157 1153 1150 1148 1147"
    )
    module_0.func()

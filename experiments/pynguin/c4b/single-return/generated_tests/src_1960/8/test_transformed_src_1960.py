# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1960 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    float_0 = 4577.1753
    list_0 = [float_0, float_0]
    var_0 = module_0.func(*list_0)
    assert (
        var_0
        == "2 4 7 11 16 22 29 37 46 56 67 79 92 106 121 137 154 172 191 211 232 254 277 301 326 352 379 407 436 466 497 529 562 596 631 667 704 742 781 821 862 904 947 991 1036 1082 1129 1177 1226 1276 1327 1379 1432 1486 1541 1597 1654 1712 1771 1831 1892 1954 2017 2081 2146 2212 2279 2347 2416 2486 2557 2629 2702 2776 2851 2927 3004 3082 3161 3241 3322 3404 3487 3571 3656 3742 3829 3917 4006 4096 4187 4279 4372 4466 4561 80 177 275 374 474 575 677 780 884 989 1095 1202 1310 1419 1529 1640 1752 1865 1979 2094 2210 2327 2445 2564 2684 2805 2927 3050 3174 3299 3425 3552 3680 3809 3939 4070 4202 4335 4469 27 163 300 438 577 717 858 1000 1143 1287 1432 1578 1725 1873 2022 2172 2323 2475 2628 2782 2937 3093 3250 3408 3567 3727 3888 4050 4213 4377 4542 131 298 466 635 805 976 1148 1321 1495 1670 1846 2023 2201 2380 2560 2741 2923 3106 3290 3475 3661 3848 4036 4225 4415 29 221 414 608 803 999 1196 1394 1593 1793 1994 2196 2399 2603 2808 3014 3221 3429 3638 3848 4059 4271 4484 121 336 552 769 987 1206 1426 1647 1869 2092 2316 2541 2767 2994 3222 3451 3681 3912 4144 4377 34 269 505 742 980 1219 1459 1700 1942 2185 2429 2674 2920 3167 3415 3664 3914 4165 4417 93 347 602 858 1115 1373 1632 1892 2153 2415 2678 2942 3207 3473 3740 4008 4277 4547 241 513 786 1060 1335 1611 1888 2166 2445 2725 3006 3288 3571 3855 4140 4426 136 424 713 1003 1294 1586 1879 2173 2468 2764 3061 3359 3658 3958 4259 4561 287 591 896 1202 1509 1817 2126 2436 2747 3059 3372 3686 4001 4317 57 375 694 1014 1335 1657 1980 2304 2629 2955 3282 3610 3939 4269 23 355 688 1022 1357 1693 2030 2368 2707 3047 3388 3730 4073 4417 185 531 878 1226 1575 1925 2276 2628 2981 3335 3690 4046 4403 184 543 903 1264 1626 1989 2353 2718 3084 3451 3819 4188 4558 352 724 1097 1471 1846 2222 2599 2977 3356 3736 4117 4499 305 689 1074 1460 1847 2235 2624 3014 3405 3797 4190 7 402 798 1195 1593 1992 2392 2793 3195 3598 4002 4407 236 643 1051 1460 1870 2281 2693 3106 3520 3935 4351 191 609 1028 1448 1869 2291 2714 3138 3563 3989 4416 267 696 1126 1557 1989 2422 2856 3291 3727 4164 25 464 904 1345 1787 2230 2674 3119 3565 4012 4460 332 782 1233 1685 2138 2592 3047 3503 3960 4418 300 760 1221 1683 2146 2610 3075 3541 4008 4476 368 838 1309 1781 2254 2728 3203 3679 4156 57 536 1016 1497 1979 2462 2946 3431 3917 4404 315 804 1294 1785 2277 2770 3264 3759 4255 175 673 1172 1672 2173 2675 3178 3682 4187 116 623 1131 1640 2150 2661 3173 3686 4200 138 654 1171 1689 2208 2728 3249 3771 4294 241 766 1292 1819 2347 2876 3406 3937 4469 425 959 1494 2030 2567 3105 3644 4184 148 690 1233 1777 2322 2868 3415 3963 4512 485 1036 1588 2141 2695 3250 3806 4363 344 903 1463 2024 2586 3149 3713 4278 267 834 1402 1971 2541 3112 3684 4257 254 829 1405 1982 2560 3139 3719 4300 305 888 1472 2057 2643 3230 3818 4407 420 1011 1603 2196 2790 3385 3981 1 599 1198 1798 2399 3001 3604 4208 236 842 1449 2057 2666 3276 3887 4499 535 1149 1764 2380 2997 3615 4234 277 898 1520 2143 2767 3392 4018 68 696 1325 1955 2586 3218 3851 4485 543 1179 1816 2454 3093 3733 4374 439 1082 1726 2371 3017 3664 4312 384 1034 1685 2337 2990 3644 4299 378 1035 1693 2352 3012 3673 4335 421 1085 1750 2416 3083 3751 4420 513 1184 1856 2529 3203 3878 4554 654 1332 2011 2691 3372 4054 160 844 1529 2215 2902 3590 4279 392 1083 1775 2468 3162 3857 4553 673 1371 2070 2770 3471 4173 299 1003 1708 2414 3121 3829 4538 671 1382 2094 2807 3521 4236 375 1092 1810 2529 3249 3970 115 838 1562 2287 3013 3740 4468 620 1350 2081 2813 3546 4280 438 1174 1911 2649 3388 4128 292 1034 1777 2521 3266 4012 182 930 1679 2429 3180 3932 108 862 1617 2373 3130 3888 70 830 1591 2353 3116 3880 68 834 1601 2369 3138 3908 102 874 1647 2421 3196 3972 172 950 1729 2509 3290 4072 278 1062 1847 2633 3420 4208 420 1210 2001 2793 3586 4380 598 1394 2191 2989 3788 11 812 1614 2417 3221 4026 255 1062 1870 2679 3489 4300 535 1348 2162 2977 3793 33 851 1670 2490 3311 4133 379 1203 2028 2854 3681 4509 761 1591 2422 3254 4087 344 1179 2015 2852 3690 4529 792 1633 2475 3318 4162 430 1276 2123 2971 3820 93 944 1796 2649 3503 4358 637 1494 2352 3211 4071 355 1217 2080 2944 3809 98 965 1833 2702 3572 4443 738 1611 2485 3360 4236 536 1414 2293 3173 4054 359 1242 2126 3011 3897 207 1095 1984 2874 3765 80 973 1867 2762 3658 4555 876 1775 2675 3576 4478 804 1708 2613 3519 4426 757 1666 2576 3487 4399 735 1649 2564 3480 4397 738 1657 2577 3498 4420 766 1690 2615 3541 4468 819 1748 2678 3609 4541 897 1831 2766 3702 62 1000 1939 2879 3820 185 1128 2072 3017 3963 333 1281 2230 3180 4131 506 1459 2413 3368 4324 704 1662 2621 3581 4542 927 1890 2854 3819 208 1175 2143 3112 4082 476 1448 2421 3395 4370 769 1746 2724 3703 106 1087 2069 3052 4036 444 1430 2417 3405 4394 807 1798 2790 3783 200 1195 2191 3188 4186 608 1608 2609 3611 37 1041 2046 3052 4059 490 1499 2509 3520 4532 968 1982 2997 4013 453 1471 2490 3510 4531 976 1999 3023 4048 497 1524 2552 3581 34 1065 2097 3130 4164 622 1658 2695 3733 195 1235 2276 3318 4361 828 1873 2919 3966 437 1486 2536 3587 62 1115 2169 3224 4280 760 1818 2877 3937 421 1483 2546 3610 98 1164 2231 3299 4368 861 1932 3004 4077 574 1649 2725 3802 303 1382 2462 3543 48 1131 2215 3300 4386 896 1984 3073 4163 677 1769 2862 3956 474 1570 2667 3765 287 1387 2488 3590 116 1220 2325 3431 4538 1069 2178 3288 4399 934 2047 3161 4276 815 1932 3050 4169 712 1833 2955 4078 625 1750 2876 4003 554 1683 2813 3944 499 1632 2766 3901 460 1597 2735 3874 437 1578 2720 3863 430 1575 2721 3868 439 1588 2738 3889 464 1617 2771 3926 505 1662 2820 3979 562 1723 2885 4048 635 1800 2966 4133 724 1893 3063 4234 829 2002 3176 4351 950 2127 3305 4484 1087 2268 3450 56 1240 2425 3611 221 1409 2598 3788 402 1594 2787 3981 599 1795 2992 4190 812 2012 3213 4415 1041 2245 3450 79 1286 2494 3703 336 1547 2759 3972 609 1824 3040 4257 898 2117 3337 4558 1203 2426 3650 298 1524 2751 3979 631 1861 3092 4324 980 2214 3449 108 1345 2583 3822 485 1726 2968 4211 878 2123 3369 39 1287 2536 3786 460 1712 2965 4219 897 2153 3410 91 1350 2610 3871 556 1819 3083 4348 1037 2304 3572 264 1534 2805 4077 773 2047 3322 21 1298 2576 3855 558 1839 3121 4404 1111 2396 3682 392 1680 2969 4259 973 2265 3558 275 1570 2866 4163 884 2183 3483 207 1509 2812 4116 844 2150 3457 188 1497 2807 4118 853 2166 3480 218 1534 2851 4169 911 2231 3552 297 1620 2944 4269 1018 2345 3673 425 1755 3086 4418 1174 2508 3843 602 1939 3277 39 1379 2720 4062 828 2172 3517 286 1633 2981 4330 1103 2454 3806 582 1936 3291 70 1427 2785 4144 927 2288 3650 436 1800 3165 4531 1321 2689 4058 851 2222 3594 390 1764 3139 4515 1315 2693 4072 875 2256 3638 444 1828 3213 22 1409 2797 4186 999 2390 3782 598 1992 3387 206 1603 3001 4400 1223 2624 4026 852 2256 3661 490 1897 3305 137 1547 2958 4370 1206 2620 4035 874 2291 3709 551 1971 3392 237 1660 3084 4509 1358 2785 4213 1065 2495 3926 781 2214 3648 506 1942 3379 240 1679 3119 4560 1425 2868 4312 1180 2626 4073 944 2393 3843 717 2169 3622 499 1954 3410 290 1748 3207 90 1551 3013 4476 1363 2828 4294 1184 2652 4121 1014 2485 3957 853 2327 3802 701 2178 3656 558 2038 3519 424 1907 3391 299 1785 3272 183 1672 3162 76 1568 3061 4555 1473 2969 4466 1387 2886 4386 1310 2812 4315 1242 2747 4253 1183 2691 4200 1133 2644 4156 1092 2606 4121 1060 2577 4095 1037 2557 4078 1023 2546 4070 1018 2544 4071 1022 2551 4081 1035 2567 4100 1057 2592 4128 1088 2626 4165 1128 2669 4211 1177 2721 4266 1235 2782 4330 1302 2852 4403 1378 2931 4485 1463 3019 4576 1557 3116 99 1660 3222 208 1772 3337 326 1893 3461 453 2023 3594 589 2162 3736 734 2310 3887 888 2467 4047 1051 2633 4216 1223 2808 4394 1404 2992 4 1594 3185 200 1793 3387 405 2001 3598 619 2218 3818 842 2444 4047 1074 2679 4285 1315 2923 4532 1565 3176 211 1824 3438 476 2092 3709 750 2369 3989 1033 2655 4278 1325 2950 4576 1626 3254 306 1936 3567 622 2255 3889 947 2583 4220 1281 2920 4560 1624 3266 332 1976 3621 690 2337 3985 1057 2707 4358 1433 3086 163 1818 3474 554 2212 3871 954 2615 4277 1363 3027 115 1781 3448 539 2208 3878 972 2644 4317 1414 3089 188 1865 3543 645 2325 4006 1111 2794 4478 1586 3272 382 2070 3759 872 2563 4255 1371 3065 183 1879 3576 697 2396 4096 1220 2922 48 1752 3457 586 2293 4001 1133 2843 4554 1689 3402 539 2254 3970 1110 2828 4547 1690 3411 556 2279 4003 1151 2877 27 1755 3484 637 2368 4100 1256 2990 148 1884 3621 782 2521 4261 1425 3167 333 2077 3822 991 2738 4486 1658 3408 582 2334 4087 1264 3019 198 1955 3713 895 2655 4416 1601 3364 551 2316 4082 1272 3040 232 2002 3773 968 2741 4515 1713 3489 689 2467 4246 1449 3230 435 2218 4002 1210 2996 206 1994 3783 996 2787 2 1795 3589 807 2603 4400 1621 3420 643 2444 4246 1472 3276 504 2310 4117 1348 3157 390 2201 4013 1249 3063 301 2117 3934 1175 2994 237 2058 3880 1126 2950 198 2024 3851 1102 2931 184 2015 3847 1103 2937 195 2031 3868 1129 2968 231 2072 3914 1180 3024 292 2138 3985 1256 3105 378 2229 4081 1357 3211 489 2345 4202 1483 3342 625 2486 4348 1634 3498 786 2652 4519 1810 3679 972 2843 138 2011 3885 1183 3059 359 2237 4116 1419 3300 605 2488 4372 1680 3566 876 2764 76 1966 3857 1172 3065 382 2277 4173 1493 3391 713 2613 4514 1839 3742 1069 2974 303 2210 4118 1450 3360 694 2606 4519 1856 3771 1110 3027 368 2287 4207 1551 3473 819 2743 91 2017 3944 1295 3224 577 2508 4440 1796 3730 1088 3024 384 2322 4261 1624 3565 930 2873 240 2185 4131 1501 3449 821 2771 145 2097 4050 1427 3382 761 2718 99 2058 4018 1402 3364 750 2714 102 2068 4035 1426 3395 788 2759 154 2127 4101 1499 3475 875 2853 255 2235 4216 1621 3604 1011 2996 405 2392 4380 1792 3782 1196 3188 604 2598 16 2012 4009 1430 3429 852 2853 278 2281 4285 1713 3719 1149 3157 589 2599 33 2045 4058 1495 3510 949 2966 407 2426 4446 1890 3912 1358 3382 830 2856 306 2334 4363 1816 3847 1302 3335 792 2827 286 2323 4361 1823 3863 1327 3369 835 2879 347 2393 4440 1911 3960 1433 3484 959 3012 489 2544 23 2080 4138 1620 3680 1164 3226 712 2776 264 2330 4397 1888 3957 1450 3521 1016 3089 586 2661 160 2237 4315 1817 3897 1401 3483 989 3073 581 2667 177 2265 4354 1867 3958 1473 3566 1083 3178 697 2794 315 2414 4514 2038 4140 1666 3770 1298 3404 934 3042 574 2684 218 2330 4443 1980 4095 1634 3751 1292 3411 954 3075 620 2743 290 2415 4541 2091 4219 1771 3901 1455 3587 1143 3277 835 2971 531 2669 231 2371 4512 2077 4220 1787 3932 1501 3648 1219 3368 941 3092 667 2820 397 2552 131 2288 4446 2028 4188 1772 3934 1520 3684 1272 3438 1028 3196 788 2958 552 2724 320 2494 92 2268 4445 2046 4225 1828 4009 1614 3797 1404 3589 1198 3385 996 3185 798 2989 604 2797 414 2609 228 2425 46 2245 4445 2069 4271 1897 4101 1729 3935 1565 3773 1405 3615 1249 3461 1097 3311 949 3165 805 3023 665 2885 529 2751 397 2621 269 2495 145 2373 25 2255 4486 2141 4374 2031 4266 1925 4162 1823 4062 1725 3966 1631 3874 1541 3786 1455 3702 1373 3622 1295 3546 1221 3474 1151 3406 1085 3342 1023 3282 965 3226 911 3174 861 3126 815 3082 773 3042 735 3006 701 2974 671 2946 645 2922 623 2902 605 2886 591 2874 581 2866 575 2862 573 2862 575 2866 581 2874 591 2886 605 2902 623 2922 645 2946 671 2974 701 3006 735 3042 773 3082 815 3126 861 3174 911 3226 965 3282 1023 3342 1085 3406 1151 3474 1221 3546 1295 3622 1373 3702 1455 3786 1541 3874 1631 3966 1725 4062 1823 4162 1925 4266 2031 4374 2141 4486 2255 25 2373 145 2495 269 2621 397 2751 529 2885 665 3023 805 3165 949 3311 1097 3461 1249 3615 1405 3773 1565 3935 1729 4101 1897 4271 2069 4445 2245 46 2425 228 2609 414 2797 604 2989 798 3185 996 3385 1198 3589 1404 3797 1614 4009 1828 4225 2046 4445 2268 92 2494 320 2724 552 2958 788 3196 1028 3438 1272 3684 1520 3934 1772 4188 2028 4446 2288 131 2552 397 2820 667 3092 941 3368 1219 3648 1501 3932 1787 4220 2077 4512 2371 231 2669 531 2971 835 3277 1143 3587 1455 3901 1771 4219 2091 4541 2415 290 2743 620 3075 954 3411 1292 3751 1634 4095 1980 4443 2330 218 2684 574 3042 934 3404 1298 3770 1666 4140 2038 4514 2414 315 2794 697 3178 1083 3566 1473 3958 1867 4354 2265 177 2667 581 3073 989 3483 1401 3897 1817 4315 2237 160 2661 586 3089 1016 3521 1450 3957 1888 4397 2330 264 2776 712 3226 1164 3680 1620 4138 2080 23 2544 489 3012 959 3484 1433 3960 1911 4440 2393 347 2879 835 3369 1327 3863 1823 4361 2323 286 2827 792 3335 1302 3847 1816 4363 2334 306 2856 830 3382 1358 3912 1890 4446 2426 407 2966 949 3510 1495 4058 2045 33 2599 589 3157 1149 3719 1713 4285 2281 278 2853 852 3429 1430 4009 2012 16 2598 604 3188 1196 3782 1792 4380 2392 405 2996 1011 3604 1621 4216 2235 255 2853 875 3475 1499 4101 2127 154 2759 788 3395 1426 4035 2068 102 2714 750 3364 1402 4018 2058 99 2718 761 3382 1427 4050 2097 145 2771 821 3449 1501 4131 2185 240 2873 930 3565 1624 4261 2322 384 3024 1088 3730 1796 4440 2508 577 3224 1295 3944 2017 91 2743 819 3473 1551 4207 2287 368 3027 1110 3771 1856 4519 2606 694 3360 1450 4118 2210 303 2974 1069 3742 1839 4514 2613 713 3391 1493 4173 2277 382 3065 1172 3857 1966 76 2764 876 3566 1680 4372 2488 605 3300 1419 4116 2237 359 3059 1183 3885 2011 138 2843 972 3679 1810 4519 2652 786 3498 1634 4348 2486 625 3342 1483 4202 2345 489 3211 1357 4081 2229 378 3105 1256 3985 2138 292 3024 1180 3914 2072 231 2968 1129 3868 2031 195 2937 1103 3847 2015 184 2931 1102 3851 2024 198 2950 1126 3880 2058 237 2994 1175 3934 2117 301 3063 1249 4013 2201 390 3157 1348 4117 2310 504 3276 1472 4246 2444 643 3420 1621 4400 2603 807 3589 1795 2 2787 996 3783 1994 206 2996 1210 4002 2218 435 3230 1449 4246 2467 689 3489 1713 4515 2741 968 3773 2002 232 3040 1272 4082 2316 551 3364 1601 4416 2655 895 3713 1955 198 3019 1264 4087 2334 582 3408 1658 4486 2738 991 3822 2077 333 3167 1425 4261 2521 782 3621 1884 148 2990 1256 4100 2368 637 3484 1755 27 2877 1151 4003 2279 556 3411 1690 4547 2828 1110 3970 2254 539 3402 1689 4554 2843 1133 4001 2293 586 3457 1752 48 2922 1220 4096 2396 697 3576 1879 183 3065 1371 4255 2563 872 3759 2070 382 3272 1586 4478 2794 1111 4006 2325 645 3543 1865 188 3089 1414 4317 2644 972 3878 2208 539 3448 1781 115 3027 1363 4277 2615 954 3871 2212 554 3474 1818 163 3086 1433 4358 2707 1057 3985 2337 690 3621 1976 332 3266 1624 4560 2920 1281 4220 2583 947 3889 2255 622 3567 1936 306 3254 1626 4576 2950 1325 4278 2655 1033 3989 2369 750 3709 2092 476 3438 1824 211 3176 1565 4532 2923 1315 4285 2679 1074 4047 2444 842 3818 2218 619 3598 2001 405 3387 1793 200 3185 1594 4 2992 1404 4394 2808 1223 4216 2633 1051 4047 2467 888 3887 2310 734 3736 2162 589 3594 2023 453 3461 1893 326 3337 1772 208 3222 1660 99 3116 1557 4576 3019 1463 4485 2931 1378 4403 2852 1302 4330 2782 1235 4266 2721 1177 4211 2669 1128 4165 2626 1088 4128 2592 1057 4100 2567 1035 4081 2551 1022 4071 2544 1018 4070 2546 1023 4078 2557 1037 4095 2577 1060 4121 2606 1092 4156 2644 1133 4200 2691 1183 4253 2747 1242 4315 2812 1310 4386 2886 1387 4466 2969 1473 4555 3061 1568 76 3162 1672 183 3272 1785 299 3391 1907 424 3519 2038 558 3656 2178 701 3802 2327 853 3957 2485 1014 4121 2652 1184 4294 2828 1363 4476 3013 1551 90 3207 1748 290 3410 1954 499 3622 2169 717 3843 2393 944 4073 2626 1180 4312 2868 1425 4560 3119 1679 240 3379 1942 506 3648 2214 781 3926 2495 1065 4213 2785 1358 4509 3084 1660 237 3392 1971 551 3709 2291 874 4035 2620 1206 4370 2958 1547 137 3305 1897 490 3661 2256 852 4026 2624 1223 4400 3001 1603 206 3387 1992 598 3782 2390 999 4186 2797 1409 22 3213 1828 444 3638 2256 875 4072 2693 1315 4515 3139 1764 390 3594 2222 851 4058 2689 1321 4531 3165 1800 436 3650 2288 927 4144 2785 1427 70 3291 1936 582 3806 2454 1103 4330 2981 1633 286 3517 2172 828 4062 2720 1379 39 3277 1939 602 3843 2508 1174 4418 3086 1755 425 3673 2345 1018 4269 2944 1620 297 3552 2231 911 4169 2851 1534 218 3480 2166 853 4118 2807 1497 188 3457 2150 844 4116 2812 1509 207 3483 2183 884 4163 2866 1570 275 3558 2265 973 4259 2969 1680 392 3682 2396 1111 4404 3121 1839 558 3855 2576 1298 21 3322 2047 773 4077 2805 1534 264 3572 2304 1037 4348 3083 1819 556 3871 2610 1350 91 3410 2153 897 4219 2965 1712 460 3786 2536 1287 39 3369 2123 878 4211 2968 1726 485 3822 2583 1345 108 3449 2214 980 4324 3092 1861 631 3979 2751 1524 298 3650 2426 1203 4558 3337 2117 898 4257 3040 1824 609 3972 2759 1547 336 3703 2494 1286 79 3450 2245 1041 4415 3213 2012 812 4190 2992 1795 599 3981 2787 1594 402 3788 2598 1409 221 3611 2425 1240 56 3450 2268 1087 4484 3305 2127 950 4351 3176 2002 829 4234 3063 1893 724 4133 2966 1800 635 4048 2885 1723 562 3979 2820 1662 505 3926 2771 1617 464 3889 2738 1588 439 3868 2721 1575 430 3863 2720 1578 437 3874 2735 1597 460 3901 2766 1632 499 3944 2813 1683 554 4003 2876 1750 625 4078 2955 1833 712 4169 3050 1932 815 4276 3161 2047 934 4399 3288 2178 1069 4538 3431 2325 1220 116 3590 2488 1387 287 3765 2667 1570 474 3956 2862 1769 677 4163 3073 1984 896 4386 3300 2215 1131 48 3543 2462 1382 303 3802 2725 1649 574 4077 3004 1932 861 4368 3299 2231 1164 98 3610 2546 1483 421 3937 2877 1818 760 4280 3224 2169 1115 62 3587 2536 1486 437 3966 2919 1873 828 4361 3318 2276 1235 195 3733 2695 1658 622 4164 3130 2097 1065 34 3581 2552 1524 497 4048 3023 1999 976 4531 3510 2490 1471 453 4013 2997 1982 968 4532 3520 2509 1499 490 4059 3052 2046 1041 37 3611 2609 1608 608 4186 3188 2191 1195 200 3783 2790 1798 807 4394 3405 2417 1430 444 4036 3052 2069 1087 106 3703 2724 1746 769 4370 3395 2421 1448 476 4082 3112 2143 1175 208 3819 2854 1890 927 4542 3581 2621 1662 704 4324 3368 2413 1459 506 4131 3180 2230 1281 333 3963 3017 2072 1128 185 3820 2879 1939 1000 62 3702 2766 1831 897 4541 3609 2678 1748 819 4468 3541 2615 1690 766 4420 3498 2577 1657 738 4397 3480 2564 1649 735 4399 3487 2576 1666 757 4426 3519 2613 1708 804 4478 3576 2675 1775 876 4555 3658 2762 1867 973 80 3765 2874 1984 1095 207 3897 3011 2126 1242 359 4054 3173 2293 1414 536 4236 3360 2485 1611 738 4443 3572 2702 1833 965 98 3809 2944 2080 1217 355 4071 3211 2352 1494 637 4358 3503 2649 1796 944 93 3820 2971 2123 1276 430 4162 3318 2475 1633 792 4529 3690 2852 2015 1179 344 4087 3254 2422 1591 761 4509 3681 2854 2028 1203 379 4133 3311 2490 1670 851 33 3793 2977 2162 1348 535 4300 3489 2679 1870 1062 255 4026 3221 2417 1614 812 11 3788 2989 2191 1394 598 4380 3586 2793 2001 1210 420 4208 3420 2633 1847 1062 278 4072 3290 2509 1729 950 172 3972 3196 2421 1647 874 102 3908 3138 2369 1601 834 68 3880 3116 2353 1591 830 70 3888 3130 2373 1617 862 108 3932 3180 2429 1679 930 182 4012 3266 2521 1777 1034 292 4128 3388 2649 1911 1174 438 4280 3546 2813 2081 1350 620 4468 3740 3013 2287 1562 838 115 3970 3249 2529 1810 1092 375 4236 3521 2807 2094 1382 671 4538 3829 3121 2414 1708 1003 299 4173 3471 2770 2070 1371 673 4553 3857 3162 2468 1775 1083 392 4279 3590 2902 2215 1529 844 160 4054 3372 2691 2011 1332 654 4554 3878 3203 2529 1856 1184 513 4420 3751 3083 2416 1750 1085 421 4335 3673 3012 2352 1693 1035 378 4299 3644 2990 2337 1685 1034 384 4312 3664 3017 2371 1726 1082 439 4374 3733 3093 2454 1816 1179 543 4485 3851 3218 2586 1955 1325 696 68 4018 3392 2767 2143 1520 898 277 4234 3615 2997 2380 1764 1149 535 4499 3887 3276 2666 2057 1449 842 236 4208 3604 3001 2399 1798 1198 599 1 3981 3385 2790 2196 1603 1011 420 4407 3818 3230 2643 2057 1472 888 305 4300 3719 3139 2560 1982 1405 829 254 4257 3684 3112 2541 1971 1402 834 267 4278 3713 3149 2586 2024 1463 903 344 4363 3806 3250 2695 2141 1588 1036 485 4512 3963 3415 2868 2322 1777 1233 690 148 4184 3644 3105 2567 2030 1494 959 425 4469 3937 3406 2876 2347 1819 1292 766 241 4294 3771 3249 2728 2208 1689 1171 654 138 4200 3686 3173 2661 2150 1640 1131 623 116 4187 3682 3178 2675 2173 1672 1172 673 175 4255 3759 3264 2770 2277 1785 1294 804 315 4404 3917 3431 2946 2462 1979 1497 1016 536 57 4156 3679 3203 2728 2254 1781 1309 838 368 4476 4008 3541 3075 2610 2146 1683 1221 760 300 4418 3960 3503 3047 2592 2138 1685 1233 782 332 4460 4012 3565 3119 2674 2230 1787 1345 904 464 25 4164 3727 3291 2856 2422 1989 1557 1126 696 267 4416 3989 3563 3138 2714 2291 1869 1448 1028 609 191 4351 3935 3520 3106 2693 2281 1870 1460 1051 643 236 4407 4002 3598 3195 2793 2392 1992 1593 1195 798 402 7 4190 3797 3405 3014 2624 2235 1847 1460 1074 689 305 4499 4117 3736 3356 2977 2599 2222 1846 1471 1097 724 352 4558 4188 3819 3451 3084 2718 2353 1989 1626 1264 903 543 184 4403 4046 3690 3335 2981 2628 2276 1925 1575 1226 878 531 185 4417 4073 3730 3388 3047 2707 2368 2030 1693 1357 1022 688 355 23 4269 3939 3610 3282 2955 2629 2304 1980 1657 1335 1014 694 375 57 4317 4001 3686 3372 3059 2747 2436 2126 1817 1509 1202 896 591 287 4561 4259 3958 3658 3359 3061 2764 2468 2173 1879 1586 1294 1003 713 424 136 4426 4140 3855 3571 3288 3006 2725 2445 2166 1888 1611 1335 1060 786 513 241 4547 4277 4008 3740 3473 3207 2942 2678 2415 2153 1892 1632 1373 1115 858 602 347 93 4417 4165 3914 3664 3415 3167 2920 2674 2429 2185 1942 1700 1459 1219 980 742 505 269 34 4377 4144 3912 3681 3451 3222 2994 2767 2541 2316 2092 1869 1647 1426 1206 987 769 552 336 121 4484 4271 4059 3848 3638 3429 3221 3014 2808 2603 2399 2196 1994 1793 1593 1394 1196 999 803 608 414 221 29 4415 4225 4036 3848 3661 3475 3290 3106 2923 2741 2560 2380 2201 2023 1846 1670 1495 1321 1148 976 805 635 466 298 131 4542 4377 4213 4050 3888 3727 3567 3408 3250 3093 2937 2782 2628 2475 2323 2172 2022 1873 1725 1578 1432 1287 1143 1000 858 717 577 438 300 163 27 4469 4335 4202 4070 3939 3809 3680 3552 3425 3299 3174 3050 2927 2805 2684 2564 2445 2327 2210 2094 1979 1865 1752 1640 1529 1419 1310 1202 1095 989 884 780 677 575 474 374 275 177 80 4561 4466 4372 4279 4187 4096 4006 3917 3829 3742 3656 3571 3487 3404 3322 3241 3161 3082 3004 2927 2851 2776 2702 2629 2557 2486 2416 2347 2279 2212 2146 2081 2017 1954 1892 1831 1771 1712 1654 1597 1541 1486 1432 1379 1327 1276 1226 1177 1129 1082 1036 991 947 904 862 821 781 742 704 667 631 596 562 529 497 466 436 407 379 352 326 301 277 254 232 211 191 172 154 137 121 106 92 79 67 56 46 37 29 22 16 11 7 4 2 1"
    )
#    module_0.func(*float_0)


def test_case_1():
    bool_0 = True
    float_0 = 1092.6
    list_0 = [bool_0, float_0, bool_0, bool_0]
    var_0 = module_0.func(*list_0)
    assert var_0 == ""


#@pytest.mark.xfail(strict=True)
#def test_case_2():
#    module_0.func()
# Test cases automatically generated by Pynguin (https://www.pynguin.eu).
# Please check them before you use them.
import pytest
import src_1960 as module_0


#@pytest.mark.xfail(strict=True)
def test_case_0():
    bytes_0 = b"\x1d\xb4"
    int_0 = 1005
    list_0 = [int_0, bytes_0]
    var_0 = module_0.func(*list_0)
    assert (
        var_0
        == "2 4 7 11 16 22 29 37 46 56 67 79 92 106 121 137 154 172 191 211 232 254 277 301 326 352 379 407 436 466 497 529 562 596 631 667 704 742 781 821 862 904 947 991 31 77 124 172 221 271 322 374 427 481 536 592 649 707 766 826 887 949 7 71 136 202 269 337 406 476 547 619 692 766 841 917 994 67 146 226 307 389 472 556 641 727 814 902 991 76 167 259 352 446 541 637 734 832 931 26 127 229 332 436 541 647 754 862 971 76 187 299 412 526 641 757 874 992 106 226 347 469 592 716 841 967 89 217 346 476 607 739 872 1 136 272 409 547 686 826 967 104 247 391 536 682 829 977 121 271 422 574 727 881 31 187 344 502 661 821 982 139 302 466 631 797 964 127 296 466 637 809 982 151 326 502 679 857 31 211 392 574 757 941 121 307 494 682 871 56 247 439 632 826 16 212 409 607 806 1 202 404 607 811 11 217 424 632 841 46 257 469 682 896 106 322 539 757 976 191 412 634 857 76 301 527 754 982 206 436 667 899 127 361 596 832 64 302 541 781 17 259 502 746 991 232 479 727 976 221 472 724 977 226 481 737 994 247 506 766 22 284 547 811 71 337 604 872 136 406 677 949 217 491 766 37 314 592 871 146 427 709 992 271 556 842 124 412 701 991 277 569 862 151 446 742 34 332 631 931 227 529 832 131 436 742 44 352 661 971 277 589 902 211 526 842 154 472 791 106 427 749 67 391 716 37 364 692 16 346 677 4 337 671 1 337 674 7 346 686 22 364 707 46 391 737 79 427 776 121 472 824 172 526 881 232 589 947 301 661 17 379 742 101 466 832 194 562 931 296 667 34 407 781 151 527 904 277 656 31 412 794 172 556 941 322 709 92 481 871 257 649 37 431 826 217 614 7 406 806 202 604 2 406 811 212 619 22 431 841 247 659 67 481 896 307 724 137 556 976 392 814 232 656 76 502 929 352 781 206 637 64 497 931 361 797 229 667 101 541 982 419 862 301 746 187 634 77 526 976 422 874 322 776 226 682 134 592 46 506 967 424 887 346 811 272 739 202 671 136 607 74 547 16 491 967 439 917 391 871 347 829 307 791 271 757 239 727 211 701 187 679 167 661 151 647 139 637 131 631 127 629 127 631 131 637 139 647 151 661 167 679 187 701 211 727 239 757 271 791 307 829 347 871 391 917 439 967 491 16 547 74 607 136 671 202 739 272 811 346 887 424 967 506 46 592 134 682 226 776 322 874 422 976 526 77 634 187 746 301 862 419 982 541 101 667 229 797 361 931 497 64 637 206 781 352 929 502 76 656 232 814 392 976 556 137 724 307 896 481 67 659 247 841 431 22 619 212 811 406 2 604 202 806 406 7 614 217 826 431 37 649 257 871 481 92 709 322 941 556 172 794 412 31 656 277 904 527 151 781 407 34 667 296 931 562 194 832 466 101 742 379 17 661 301 947 589 232 881 526 172 824 472 121 776 427 79 737 391 46 707 364 22 686 346 7 674 337 1 671 337 4 677 346 16 692 364 37 716 391 67 749 427 106 791 472 154 842 526 211 902 589 277 971 661 352 44 742 436 131 832 529 227 931 631 332 34 742 446 151 862 569 277 991 701 412 124 842 556 271 992 709 427 146 871 592 314 37 766 491 217 949 677 406 136 872 604 337 71 811 547 284 22 766 506 247 994 737 481 226 977 724 472 221 976 727 479 232 991 746 502 259 17 781 541 302 64 832 596 361 127 899 667 436 206 982 754 527 301 76 857 634 412 191 976 757 539 322 106 896 682 469 257 46 841 632 424 217 11 811 607 404 202 1 806 607 409 212 16 826 632 439 247 56 871 682 494 307 121 941 757 574 392 211 31 857 679 502 326 151 982 809 637 466 296 127 964 797 631 466 302 139 982 821 661 502 344 187 31 881 727 574 422 271 121 977 829 682 536 391 247 104 967 826 686 547 409 272 136 1 872 739 607 476 346 217 89 967 841 716 592 469 347 226 106 992 874 757 641 526 412 299 187 76 971 862 754 647 541 436 332 229 127 26 931 832 734 637 541 446 352 259 167 76 991 902 814 727 641 556 472 389 307 226 146 67 994 917 841 766 692 619 547 476 406 337 269 202 136 71 7 949 887 826 766 707 649 592 536 481 427 374 322 271 221 172 124 77 31 991 947 904 862 821 781 742 704 667 631 596 562 529 497 466 436 407 379 352 326 301 277 254 232 211 191 172 154 137 121 106 92 79 67 56 46 37 29 22 16 11 7 4 2 1"
    )
#    module_0.func()


#@pytest.mark.xfail(strict=True)
def test_case_1():
    list_0 = []
#    module_0.func(*list_0)
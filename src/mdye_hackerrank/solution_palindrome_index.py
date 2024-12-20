"""."""

import sys


def test_pal(s: str) -> bool:
    """."""
    # less efficient, but more readable way

    return s == "".join(reversed(s))


def palindrome_index(s: str) -> int:
    """."""
    # Iterate through the chars in s, comparing.
    # If bx and ex are not same, drop bx and test the rest of the string
    # else drop ex and test the rest of the string
    # else return -1 b/c we can't make a palindrome

    bx = 0
    ex = len(s) - 1

    # test cases:
    # 'aa'; bx = 0, ex = 1; dl, return -1
    # 'ab'; bx = 0, ex = 1; tp("" + b) == True; return 0
    # 'aba'; bx = 0, ex = 2; dl, return -1
    # 'abcde'; bx=0, ex=4; tp("" + bcde) == False, tp(abcd + "") == False, break, return -1
    # 'abcfba'; # should iterate 0,5; 1,4; 2,3 then ... tp(abc + ba) == True, return 3
    # optimization not done: needn't check all letters w/ testPal, just the inners from where you are?
    while bx < ex:
        if s[bx] != s[ex]:
            # try replace bx and test
            if test_pal(s[0:bx] + s[bx + 1 :]):
                return bx
            elif test_pal(s[0:ex] + s[ex + 1 :]):
                return ex
            else:
                break  # busted

        bx += 1
        ex -= 1

    return -1  # is pal or can't be made one


if __name__ == "__main__":
    _ = input()  # eat first line

    for line in sys.stdin:
        print(palindrome_index(line.strip()))

    sys.exit(0)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4

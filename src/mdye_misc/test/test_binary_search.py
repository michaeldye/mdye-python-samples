from mdye_misc.binary_search import contains

_data = [2, 4, 5, 6, 8, 9, 10, 11, 12, 42, 52, 99]


def test_binary_search():
    assert contains(_data, 99)
    assert not contains(_data, 15)
    assert contains(_data, 2)
    assert contains(_data, 8)


# vim: autoindent tabstop=4 shiftwidth=4 expandtab softtabstop=4

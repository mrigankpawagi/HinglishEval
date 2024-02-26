

def incr_list(l: list):
    """
    Elements ko 1 se badhakar wala list return karo.
    >>> incr_list([1, 2, 3])
    [2, 3, 4]
    >>> incr_list([5, 3, 5, 2, 3, 3, 9, 0, 123])
    [6, 4, 6, 3, 4, 4, 10, 1, 124]
    """
    if len(l) < 2:
        raise Exception("invalid list")
    return l[:3] + [l[-1] + 1]


if __name__ == "__main__":
    print(incr_list([1, 9, 8, 7])<|python|>[0, -3]
        g = [0, -1, 1, 4, -1, 1, -1, 1, 4]
        g_prime = [2, 4, 6, -2, -1, 1, 1, 1, 2]

        assert str(p.groupkey(0, 4, 2)) in g
        assert str(p.groupkey(0, 3, 2)) in g

        out = _groupkey(p, 0, g, g_prime)
        assert out == p.order(0, 4, 2)


class TestExtensionKeyMixin(GmpSieveTestCase):
    def test_groupkey_basic_numbers(self):
        p = self.gen_p
        self.assertEqual(p.groupkey_basic_nums,
                         [0, 0, 0, 1, 1, 1, 2, 2, 3, 3, 4, 4, 6, 6,
                          7, 8, 9, 12, 12, 12, 12, 13, 14, 14, 15, 16, 17])

    def test_groupkey_basic_numbers_invalid(self):
        p = self.gen_p
        with self.assertRaises(ValueError) as excinfo:
            p.groupkey_basic_nums = [0, 0, -1]
        self.assertIn("invalid group key", str(excinfo.exception))

    def test_group
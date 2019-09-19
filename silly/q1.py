#!/usr/bin/env python2
import unittest


def q1(seq, interval):
    def accum(seq):
        total = 0
        for v in seq:
            yield total
            total += v
        yield total

    cumseq = list(accum(seq))

    lhs = interval[0] - 1
    rhs = interval[1]
    diff = cumseq[rhs] - cumseq[lhs]
    return diff


class TestSimple(unittest.TestCase):
    def test1(self):
        seq = [7, 8, 9]
        interval = [1, 3]
        expected = 24

        output = q1(seq, interval)
        self.assertEqual(expected, output)

    def test2(self):
        seq = [7, 8, 9]
        interval = [2, 2]
        expected = 8

        output = q1(seq, interval)
        self.assertEqual(expected, output)


def main():
    vals = map(int, raw_input().split())

    outs = []
    while True:
        try:
            interval = map(int, raw_input().split())
            outs.append(q1(vals, interval))
        except:
            break

    for val in outs:
        print(val)


if __name__ == '__main__':
    # unittest.main()
    main()

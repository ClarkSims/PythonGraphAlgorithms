#!/usr/bin/env python2
import unittest


def q2(w, t, seq):
    def accum(seq):
        total = 0
        for v in seq:
            yield total
            total += v
        yield total

    cumseq = list(accum(seq))

    # print cumseq
    rv = []
    for off in range(len(seq)):
        rhs = off + 1
        lhs = max(rhs - w, 0)
        diff = cumseq[rhs] - cumseq[lhs]
        # print diff
        if diff > t:
            rv.append('Y')
        else:
            rv.append('N')

    return rv


class TestSimple(unittest.TestCase):
    def test1(self):
        w = 1
        t = 1
        seq = [2]

        output = q2(w, t, seq)
        expected = ['Y']
        self.assertEqual(expected, output)

    def test2(self):
        w = 3
        t = 3
        seq = [1 for _ in range(7)]
        seq[3] = 2

        output = q2(w, t, seq)
        expected = ['N' for _ in range(3)] + ['Y' for _ in range(3)] + ['N']
        self.assertEqual(expected, output)


def main():
    params = map(int, raw_input().split())
    w = params[0]
    t = params[1]

    seq = []
    while True:
        try:
            val = int(raw_input())
            seq.append(val)
        except:
            break

    outs = q2(w, t, seq)
    for val in outs:
        print(val)


if __name__ == '__main__':
    # unittest.main()
    main()

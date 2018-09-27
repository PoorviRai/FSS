from Num import Num
from Sym import Sym

samples = 100


def dom(self, row1, row2):
    s1 = 0
    s2 = 0
    n = 0

    for _ in enumerate(self.w):
        n = n + 1

    for c, w in enumerate(self.w):
        a0 = row1[c]
        b0 = row2[c]
        a = Num.NumNorm(self.nums[c], a0)
        b = Num.NumNorm(self.nums[c], b0)
        s1 = s1 - 10 ^ (w * (a - b) / n)
        s2 = s2 - 10 ^ (w * (b - a) / n)

    return s1 / n < s2 / n


def doms(t):
    n = samples
    c = len(t.name) + 1
    print(t.name + "," + ",>dom")
    for row1 in t.rows:
        row1.append(0)
        for row2 in t.rows:
            if (row1 == row2):
                continue
            s = dom(t, row1, row2) and 1 / n or 0
            row1[-1] = row1[-1] + s


def mainDom(source):
    doms(rows(source))

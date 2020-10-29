from typing import Dict, Optional
import json


class CashFlow:

    def __init__(self, amount: float, n: int):
        self.amount = amount
        self.n = n

    def pv(self, r: float) -> 'CashFlow':
        r = r
        res = self.amount/(1+r)**self.n
        ans = CashFlow(res, 0)
        return ans

    def fv(self, r: float) -> 'CashFlow':
        r = r
        res = self.amount*(1+r)**self.n
        ans = CashFlow(res, self.n)
        return ans

    def shift(self, n: int, r: float) -> 'CashFlow':
        p_v = CashFlow(self.amount, self.n).pv(r)
        return CashFlow(p_v.amount, n).fv(r)

    def merge(self, other: 'CashFlow', r: float, reverse: bool = False) -> 'CashFlow':
        if reverse is not True:
            if self.n != 0:
                p1 = CashFlow(self.amount, self.n).pv(r)
            else:
                p1 = self
            if other.n != 0:
                p2 = other.pv(r)

            else:
                p2 = other

            ans = CashFlow(p1.amount+p2.amount, 0)
            return ans
        else:
            a = [self.n if self.n > other.n else other.n]
            if self.n == 0:
                p1 = self.shift(a[0], r)
                print(p1.amount)
            else:
                p1 = self
                print(p1.amount)
            if other.n == 0:
                p2 = other.shift(a[0], r)
                print(p2.amount)
            else:
                p2 = other
                print(p2.amount)
            return CashFlow(p1.amount+p2.amount, a[0])

    def to_dict(self, decimal_places: Optional[int] = 2) -> Dict:
        return {
            "amount": self.amount if decimal_places is None else round(self.amount, decimal_places),
            "n": self.n
        }

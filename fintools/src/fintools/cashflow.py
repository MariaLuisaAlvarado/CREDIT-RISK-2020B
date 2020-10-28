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
        if self.n > n:
            return CashFlow(self.amount, n).fv(r)
        else:
            return CashFlow(self.amount, n).pv(r)

    def merge(self, other: 'CashFlow', r: float, reverse: bool = False) -> 'CashFlow':
        if reverse is not True:
            res1, res2 = self.pv(r), other.pv(r)
            ans = res1 + res2
            return json.dumps(ans)
        else:
            if self.n > other.n:
                res1 = self
                res2 = other.shift(self.n, r)
            else:
                res1 = self.shift(other.n, r)
                res2 = other
            ans = res1 + res2
            return json.dumps(ans)

    def to_dict(self, decimal_places: Optional[int] = 2) -> Dict:
        return {
            "amount": self.amount if decimal_places is None else round(self.amount, decimal_places),
            "n": self.n
        }

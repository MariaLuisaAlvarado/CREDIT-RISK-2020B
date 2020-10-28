import json
from fintools import CashFlow


class Main:

    @staticmethod
    def present_value(amount: float, rate: float, n: int):
        res = CashFlow(amount, n)
        res2 = res.pv(rate)
        ans = res2.to_dict()
        return ans

    @staticmethod
    def future_value(amount: float, rate: float, n: int):
        res = CashFlow(amount, n)
        res2 = res.fv(rate)
        ans = res2.to_dict()
        return ans

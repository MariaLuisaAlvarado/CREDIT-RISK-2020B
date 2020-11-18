from typing import Optional

from fintools import Amortization


class Main:

    @staticmethod
    def annuity(amount: float, rate: float, n: int):
        return Amortization(amount, rate, n).annuity

    @staticmethod
    def table(amount: float, rate: float, n: int, save_file: Optional[str] = None):
        table2 = Amortization(amount, rate, n).get_table(save_file)
        table2_df = table2.to_string()
        return table2_df

    @staticmethod
    def plot(amount: float, rate: float, n: int, save_file: Optional[str] = None):
        am = Amortization(amount, rate, n)
        return am.plot(save_file)

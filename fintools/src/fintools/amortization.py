from typing import Optional

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd


class Amortization:

    def __init__(self, amount: float, rate: float, n: int):
        self.amount = amount
        self.rate = rate
        self.n = n

    @property
    def annuity(self) -> float:
        a = (self.rate*self.amount)/(1-(1+self.rate)**(-self.n))
        return a

    def get_table(self, save_file: Optional[str] = None) -> pd.DataFrame:
        table = np.zeros((self.n+1, 5))
        table[0, 1] = self.amount
        b = self.amount
        for t in range(1, self.n+1):
            i = b * self.rate
            p = self.annuity - i
            b = b - p
            table[t, :] = [t, b, self.annuity, p, i]
        table2 = pd.DataFrame(table, columns=['t', 'B', 'A', 'P', 'I'])
        table2.at[0, 'A'] = 'nan'
        table2.at[0, 'P'] = 'nan'
        table2.at[0, 'I'] = 'nan'
        if save_file:
            table2.to_csv(save_file)

        return table2

    def plot(self, show: bool = False, save_file: Optional[str] = None) -> None:
        table = self.get_table().fillna(0)
        A = table['P']
        B = table['I']

        X = np.arange(len(A))

        plt.bar(X, A, color='b', width=0.5)
        plt.bar(X, B, color='r', bottom=A, width=0.5)
        plt.xlabel('$t$')
        plt.ylabel('$$$')
        plt.legend(['P', 'I'], loc=2)
        plt.axis([-0.5, len(A) - 0.5, 0, table.iloc[1, 2] * 1.1])
        plt.grid()
        fig = plt.gcf()
        fig.savefig(save_file)
        if save_file is not None:
            fig.savefig(save_file)
        plt.show()

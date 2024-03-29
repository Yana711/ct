import seaborn as sns
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
import argparse

parser = argparse.ArgumentParser()
parser.add_argument('month', type= str)
parser.add_argument('year', type= str)
a = parser.parse_args()

month = a.month
year = a.year

m=int(month)
y=int(year)

assert isinstance(m, int)
assert m > 0 and m<=12, "Номер месяца должен быть больше нуля, но меньше 12 (12>=month>0)."
assert isinstance(y, int)
assert y > 0, "Год не может быть отрицательный. Введите положительное число."

outcome_data = pd.read_excel(fr"C:\Users\scorpyana7\OneDrive\Рабочий стол\Yana\outcome_{month}.{year}.xlsx")
outcome_data

outcome_data["День"] = [int(x.split()[0]) for x in outcome_data["Дата"]]
outcome_data

fig, ax = plt.subplots(constrained_layout=True)
sns.barplot(
data=outcome_data,
x="Сумма",
y="Категория",
orient = "h",
estimator="sum",
errorbar=None,
ax=ax
)
plt.title(f'{month}.{year}')
plt.show()


import pandas as pd
import matplotlib.pyplot as plt

df = pd.read_csv("././res/companysalesdata.csv")

plt.plot(df['month_number'], df['total_profit'], linestyle = "-", color = 'red', marker = 'o', markersize = 4, markerfacecolor = 'red', linewidth = 2, label = 'Total Profit')

plt.xlabel('Month')
plt.ylabel('Total profit')
plt.title('Total profits of all months')

plt.grid(True)
plt.show()
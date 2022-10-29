'''Displays historic data of stocks till present day.'''

from pandas_datareader import data as pdr
import matplotlib.pyplot as plt
from datetime import date as dt

stock_sym = input("\nEnter a stock symbol: ").upper()
print("The symbol you entered is {}.".format(stock_sym))

start_date = input("\nEnter the start date in YYYY-MM-DD format: ")
end_date = dt.today()

data = pdr.DataReader(name=stock_sym, data_source="yahoo",
                      start=start_date, end=end_date)
print(data)

data['Close'].plot(title=stock_sym, figsize=(8, 8), label=stock_sym)
plt.xlabel('Date', fontsize=15)
plt.ylabel('Close', fontsize=15)
plt.grid(linestyle=':', linewidth=1)
# plt.legend(loc="lower right") Can be used to plot more than 1 tickers.
plt.show()

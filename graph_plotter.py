import matplotlib.pyplot as plt
import pandas

df = pandas.read_csv('bitcoin.csv', index_col=False)

df = df.sort_values(by='Time', ascending=True)

print(df.keys())
print(df.shape)

plt.figure(figsize=(18, 9))
plt.plot(range(df.shape[0]), (df['EUR Price']))
plt.xticks(range(0, df.shape[0], 50), df['Time'].loc[::50], rotation=45)
plt.xlabel('Time', fontsize=18)
plt.ylabel('Price (eur)', fontsize=18)
plt.show()

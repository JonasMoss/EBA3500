import seaborn as sns

supermarket = pd.read_csv("supermarket_sales.csv")

sns.set(style="whitegrid")
seaborn.boxplot(x="cogs", y="City", data=supermarket)
plt.show()
plt.clf()


sns.set(style="whitegrid")
seaborn.violinplot(x="cogs", y="City", data=supermarket)
plt.show()
plt.clf()


plt.figure(1)
seaborn.violinplot(x="cogs", y="City", data=supermarket)
plt.figure(2)
seaborn.boxplot(x="cogs", y="City", data=supermarket)
plt.show()

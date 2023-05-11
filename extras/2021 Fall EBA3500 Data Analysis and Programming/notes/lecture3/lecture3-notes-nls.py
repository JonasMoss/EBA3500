from scipy.optimize import curve_fit


rng = np.random.default_rng(seed = 313)
x = sort(np.linspace(0, 1, num = 100))
u = rng.uniform(-1, 1, 100)
y1 = 2 + 3 * x + u # prototype 1
y2 = np.exp(3 * x ** 2) + u # prototype 2

# The function Alice gave Bob!
func = lambda x, a, b: np.exp(a * x ** b)

# This fits the model.
param1 = curve_fit(func, x, y1)[0]
param2 = curve_fit(func, x, y2)[0]


# Prototype 2
plt.scatter(x, y2)
plt.plot(x, func(x, 3, 2), color = "black")
plt.plot(x, func(x, param2[0], param2[1]), color = "red")
plt.show()

lower = np.sum((y2 - np.mean(y2)) ** 2) # 2168.736140549201
upper = np.sum((y2 - func(x, param2[0], param2[1])) ** 2) # 32.016818192175435
1 - upper / lower
np.corrcoef(x, y2)[1, 0] ** 2


# Prototype 1
param1 = curve_fit(func, x, y1)[0]
plt.scatter(x, y1)
plt.plot(x, 2 + 3 * x, color = "black")
plt.plot(x, func(x, param1[0], param1[1]), color = "red")
plt.show()


lower = np.sum((y1 - np.mean(y1)) ** 2) 
upper = np.sum((y1 - func(x, param1[0], param1[1])) ** 2)
1 - upper / lower
np.corrcoef(x, y1)[1, 0] ** 2

# Bad type.

rng = np.random.default_rng(seed = 313)
x = sort(np.linspace(0, 1, num = 100))
u = rng.uniform(-1, 1, 100)
y = 9 + 2 * x + u 
param = curve_fit(func, x, y)[0]

plt.scatter(x, y)
plt.plot(x, 9 + 3 * x, color = "black")
plt.plot(x, func(x, param[0], param[1]), color = "red")
plt.show()

lower = np.sum((y - np.mean(y)) ** 2) 
upper = np.sum((y - func(x, param[0], param[1])) ** 2)
1 - upper / lower
np.corrcoef(x, y)[1, 0] ** 2


# Horrible type.

rng = np.random.default_rng(seed = 313)
x = sort(np.linspace(0, 1, num = 100))
u = rng.uniform(-1, 1, 100)
y = 5 + 2 * x + u 

func = lambda x, a, b: a*x + np.exp(b*x)
param = curve_fit(func, x, y)[0]

plt.scatter(x, y)
plt.plot(x, 5 + 2 * x, color = "black")
plt.plot(x, func(x, param[0], param[1]), color = "red")
plt.show()

lower = np.sum((y - np.mean(y)) ** 2) 
upper = np.sum((y - func(x, param[0], param[1])) ** 2)
1 - upper / lower
np.corrcoef(x, y)[1, 0] ** 2

# New function 
func = lambda x, a, b, c: c + np.exp(a * x ** b)
param = curve_fit(func, x, y)[0]

plt.scatter(x, y)
plt.plot(x, 9 + 3 * x, color = "black")
plt.plot(x, func(x, param[0], param[1], param[2]), color = "red")
plt.show()

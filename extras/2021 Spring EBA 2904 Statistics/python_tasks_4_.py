# Task (i). Make a function test_rng. Its rng argument can be any random number
# generator, such as rng.standard_exponential used last time, but use
# rng.random to make it uniform!
def test_rng(x, func, rng, n_reps = 10 ** 5):
    """ Approximates the probability that func(y) >= func(x) when y is sampled 
    from rng. rng is the random number generator, e.g. the uniform distribution,
    and n_reps is the number of repetitions. (rng must take one argument;
    which is the number of samples.)
    """
    n = len(x)
    f_x = func(x)
    samples = rng((n_reps, n))

    return np.mean(np.apply_along_axis(
        func1d = lambda y: f_x <= func(y),
        axis = 1,
        arr = samples
    ))

# Task (ii). Run test_rng on "x" using "median" and the functions we used 
# last time: sum(x ** 3), sum(exp(-x)), median(x) - mean(x), and 
# mean(abs(x - median(x))). "mean absolute deviation from the median"
# mean((x - mean(x))^2)

np.median(x)
test_rng(x, np.median, rng.random)
test_rng(x, lambda x: np.sum(x ** 3), rng.random)
test_rng(x, lambda x: np.sum(np.exp(-x)), rng.random)
test_rng(x, lambda x: np.median(x) - np.mean(x), rng.random)
test_rng(x, lambda x: np.mean(np.abs(x - np.median(x))), rng.random)

# Task (iii). Generate some data from the standard normal distribution and use
# test_rng to test if the data is probable under the normal distribution or not.
# Use the np.mean, np.var, and np.max as the function arguments.

z = rng.standard_normal(100)
test_rng(z, np.var, rng.standard_normal)
test_rng(z, np.mean, rng.standard_normal)
test_rng(z, np.max, rng.standard_normal)

# Task (iv). Suppose you knew that I like beta(9, 9) super-well, but never 
# generate data from beta(0.5, 0.5). How can you modify the variance approach
# above to work for data generated from beta(9, 9)? To solve this exercise you
# need to plot beta(9, 9)!

x = rng.beta(9, 9, 100)
ax = sns.histplot(x = x, stat = "density")
xs = np.arange(0, 1, 0.01)
ax.plot(xs, stats.beta(1, 1).pdf(xs), color = "black")
ax.plot(xs, stats.beta(9, 9).pdf(xs), color = "blue")
plt.show()

test_rng(x, lambda x: 1/np.var(x), rng.standard_normal)
test_rng(x, lambda x: -np.var(x), rng.standard_normal)
1 - test_rng(x, lambda x: np.var(x), rng.standard_normal)

np.var(x) # variance of a uniform is 1/12 = 0.08333333333333333


n_reps = 10 ** 5
n = 100
samples = rng.random((n_reps, n))
results = np.apply_along_axis(
        func1d = lambda x: np.sum(np.exp(-x)),
        axis = 1,
        arr = samples)

sns.histplot(x = results, stat = "density")
plt.show()


# Are they uniform? It kinda looks like it.
ax = sns.histplot(x = x, stat = "density")
xs = np.arange(-5, 5, 0.01)
ax.plot(xs, stats.standard_normal.pdf(xs), color = "black")
ax.plot(xs, stats.laplace(0,1).pdf(xs), color = "blue")
plt.show()
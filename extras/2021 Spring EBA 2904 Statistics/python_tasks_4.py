# Task (i). Make a function test_rng. Its rng argument can be any random number
# generator, such as rng.standard_exponential used last time, but use
# rng.random to make it uniform!
def test_rng(x, func, rng, n_reps = 10 ** 5):
    """ Approximates the probability that func(y) >= func(x) when y is sampled 
    from rng. rng is the random number generator, e.g. the uniform distribution,
    and n_reps is the number of repetitions.
    """
    # FILL IN!
# Task (ii). Run test_rng on "x" using "median" and the functions we used 
# last time: sum(x ** 3), sum(exp(-x)), median(x) - mean(x), and 
# mean(abs(x - median(x))).
# Task (iii). Generate some data from the standard normal distribution and use
# test_rng to test if the data is probable under the normal distribution or not.
# Use the np.mean, np.var, and np.max as the function arguments.
# Task (iv). Suppose you knew that I like beta(9, 9) super-well, but never 
# generate data from beta(0.5, 0.5). How can you modify the variance approach
# above to work for data generated from beta(9, 9)? To solve this exercise you
# need to plot beta(9, 9)!

def test_rng(x, func, rng, n_reps = 10 ** 5):
    """ Approximates the probability that func(y) >= func(x) when y is sampled 
    from rng. rng is the random number generator, e.g. the uniform distribution,
    and n_reps is the number of repetitions.
    """
    n = len(x)
    f_x = func(x)
    samples = rng((n_reps, n))
    return np.mean(np.apply_along_axis(
        func1d = lambda y: f_x <= func(y),
        axis = 1,
        arr = samples)
    )

test_rng(x, np.median, rng.random)
test_rng(x, lambda x: np.sum(x ** 3), rng.random)
test_rng(x, lambda x: np.sum(np.exp(-x)), rng.random)
test_rng(x, lambda x: np.median(x) - np.mean(x), rng.random)
test_rng(x, lambda x: np.mean(np.abs(x - np.median(x))), rng.random)

z = rng.standard_normal(100)

test_rng(z, np.var, rng.standard_normal)
test_rng(z, np.mean, rng.standard_normal)
test_rng(z, np.max, rng.standard_normal)

x = rng.beta(9, 9, 100)
ax = sns.histplot(x = x, stat = "density")
xs = np.arange(0, 1, 0.01)
ax.plot(xs, stats.beta(1, 1).pdf(xs), color = "black")
ax.plot(xs, stats.beta(9, 9).pdf(xs), color = "blue")
plt.show()
test_rng(x, lambda x: 1/np.var(x), rng.random)
test_rng(x, lambda x: -np.var(x), rng.random)
1 - test_rng(x, np.var, rng.random)
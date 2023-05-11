# (i) Simulate p-values using a log-normal with standard deviation 100. Remember
#     to subtract the mean! 

f_lnorm = lambda n: rng.lognormal(0, 1, n) # has mean np.exp(3)!
# mu = 0
#(exp(sigma ** 2) - 1) * exp(2 * mu + sigma ** 2) == 10000
#(exp(sigma ** 2) - 1 )* exp(sigma ** 2)

sigma = np.sqrt(np.log(0.5 * (1 + np.sqrt(40001))))

# the mean is exp(mu + sigma ** 2 / 2)
mean = np.exp(sigma ** 2 / 2)

n_reps = 10 ** 5
n = 100
pvals = np.apply_along_axis(
        func1d = pval,
        axis = 1,
        arr = f_lnorm((n_reps, n)) - mean)

pvals = f_lnorm(10000)        

ax = sns.histplot(x = pvals - 1.63 , stat = "density")
#ax.plot(pvals, stats.beta(1, 1).pdf(sorted(pvals)), color = "black")
plt.show() 

# (ii) Simulate p-values from a Laplace distribution with mean 0 (see the docs at
#     https://numpy.org/doc/stable/reference/random/generated/numpy.random.laplace.html)
#     with scale parameter 0.1, 1, and 13.37. How does the t-test perform? Does
#     it care about the standard deviation?

# Laplace is well-behaved; no heavy tails and symmetric.
f_laplace = lambda n: rng.laplace(0, 13.37, n) # has mean np.exp(3)!
n_reps = 1000
n = 100
pvals = np.apply_along_axis(
        func1d = pval,
        axis = 1,
        arr = f_laplace((n_reps, n)))

ax = sns.histplot(x = pvals, stat = "density")
ax.plot(pvals, stats.beta(1, 1).pdf(sorted(pvals)), color = "black")
plt.show() 

# (iii) Simulate p-values from a uniform distribution (subtract 1/2 from the variates
#     to make the mean equal to 0). How well does it work? 
# This is on [0,1].
n_reps = 1000
n = 100
pvals = np.apply_along_axis(
        func1d = pval,
        axis = 1,
        arr = rng.random((n_reps, n)) - 1/2)

ax = sns.histplot(x = pvals, stat = "density")
ax.plot(pvals, stats.beta(1, 1).pdf(sorted(pvals)), color = "black")
plt.show() 

# (iv) Find the expression for the standard deviation of the uniform distribution.
#     Sample random variables from the uniform distributio on [-1, 1], [-30, 30],
#     and [-1000, 1000]. How well does the t-test work? Is it affected by the
#     standard deviation? (Hint: To generate variates
#     from these distributions, first generate the values "sims", then subtract -1/2,
#     then multiply by 2 * a, where a is the desired number. For instance to simulate
#     from [-30, 30], you would use 60 * (sims - 1/2)). 

# The t-test is scale-invariant: So the result of reunning the t-test on d * x is the same
# as running it on x.

f_uniform = lambda n: 2*1000*(rng.random(n) - 0.5) # has mean np.exp(3)!
n_reps = 5000
n = 100

# Example of invariance under scale transforms:

x = f_uniform(100)
pval(x)
pval(0.5 * x)
pval(0.1 * x)
pval(np.pi * x)

pvals = np.apply_along_axis(
        func1d = pval,
        axis = 1,
        arr = f_uniform((n_reps, n)))

ax = sns.histplot(x = pvals, stat = "density")
ax.plot(pvals, stats.beta(1, 1).pdf(sorted(pvals)), color = "black")
plt.show() 

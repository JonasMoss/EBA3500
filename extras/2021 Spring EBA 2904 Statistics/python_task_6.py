# 1.) What is the length of the confidence interval in (*)?
# (*) [x_bar - z_alpha * sigma / sqrt(n), x_bar + z_alpha * sigma / sqrt(n)],
# length([a, b]) = b - a
#  x_bar + z_alpha * sigma / sqrt(n) - (x_bar - z_alpha * sigma / sqrt(n))
# 2 * z_alpha * sigma / sqrt(n)

# 2.) When sigma = 1, what is the number of observations needed to make the
#     length of the interval equal to 0.5? (95% confidence interval)
# 2 * z_alpha * sigma / sqrt(n) = 0.5
# 4 * z_alpha * sigma / sqrt(n) = 1
# 4 * z_alpha * sigma = sqrt(n)
# (4 * z_alpha * sigma)^2 = n
# 16 * z_alpha ^2 * sigma ^ 2 = n
mu = 1 
sigma = 1
alpha = 0.05
z_alpha = stats.norm.ppf(1 - alpha / 2)
16 * z_alpha ** 2 * sigma ** 2

# 2.) Most confidence intervals, such as the t interval, does not have a fixed size.
#     make a function that takes an array of CIs and returns the length of each CI.

def ci_len(cis):
    # length([a,b] = b - a
    return(cis[:, 1] - cis[:, 0])
cis = np.array([[1, 2], [3, 4], [5, 6]])
ci_len(cis)

# 3.) Explain why each point in the list of Hoekstra are errors. (Hint: There are
#     two kinds of mistakes in this list. First, they can talk about probabilities
#     when there is nothing random to talk about. Remember than mu is fixed. Second,
#     they think about the coverage (95% etc) of confidence intervals in terms of 
#     the observed intervals. Say if you have an observed interval  [-1, 1]. Then it isn't 
#     random -- it's [-1, 1]!).

# Hoekstra, R. et al (2014) list 6 common errors. Suppose you're given a confidence
# interval for the mean equal to [0.4, 0.6]. Which of the following is true?
# 1. The probability that the true mean is greater than 0 is at least 95 %.
### Sound reasonable: 0 < 0.4, [0, 0.6] is contiained in [0.4, 0.6]. P(mu > 0) = 0.95.
### P(mu => 0) = 1 or P(mu => 0) = 0. 
# 2. The probability that the true mean equals 0 is smaller than 5 %.
### P(mu = 0) < 0.05. We have: P(mu = 0) = 1 or P(mu = 0) = 0. 
# 3. The “null hypothesis” that the true mean equals 0 is likely to be incorrect.
### It is imprecise. What does "likely" mean?
# 4. There is a 95 % probability that the true mean lies between 0.1 and 0.4.
### The CI [0.4, 0.6] is observed, __not random__ P(0.1 <= mu <= 0.4) = 0 or 
### equal to 1!! Because there is randomness.
# 5. We can be 95 % confident that the true mean lies between 0.1 and 0.4.
### Wrong! 95% confident that mu is in the CI when the CI isn't observed. 
# 6. If we were to repeat the experiment over and over, then 95 % of the time the 
#    true mean falls between 0.1 and 0.4.
### The same as 4, using the law of large numbers.
### [-1, -0.5]!
# Interested readers can have a look at (this is not on the curriculum.)
# Hoekstra, R., Morey, R. D., Rouder, J. N., & Wagenmakers, E.-J. (2014). 
# Robust misinterpretation of confidence intervals. 
# Psychonomic Bulletin & Review, 21(5), 1157–1164. 
# https://doi.org/10.3758/s13423-013-0572-3
def pval_left(x, mu, sigma):
    """ Calculates the one-sided p-value based on the z-test."""
    n = len(x)
    x_bar = np.mean(x)
    z = np.sqrt(n) * (x_bar - mu)/sigma
    return 1 - stats.norm.cdf(z)

pval_left([1.64], 0, 1)

def pval_right(x, mu, sigma):
    """ Calculates the one-sided p-value based on the z-test."""
    n = len(x)
    x_bar = np.mean(x)
    z = np.sqrt(n) * (x_bar - mu)/sigma
    return stats.norm.cdf(np.abs(z))

pval_right([-1.64], 0, 1)
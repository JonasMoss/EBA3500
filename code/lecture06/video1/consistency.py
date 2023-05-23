import numpy

rng = numpy.random.default_rng(seed=313)
xs = rng.gamma(2, 2, size=[1000, 100])

### Incomplete

import numpy as np
import seaborn as sns


rng = np.random.default_rng(seed=313)
xs = rng.standard_normal(size=[1000, 100])
medians = np.median(xs, 1)
sns.plot(medians)

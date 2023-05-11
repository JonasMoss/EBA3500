---
tags: EBA3500
---

# Prerequisities

We expect you to be familiar with the probabilistic and statistical concepts from the previous course [Statistics with programming (EBA 2904)](https://programmeinfo.bi.no/nb/course/EBA-2904/2022-spring). If you do not remember the content this course you will have to relearn it on your own. There are numerous resources for elementary statisics and probability online, at e.g. the free [Introduction to Probability (1997) by Grinstead](https://open.umn.edu/opentextbooks/textbooks/21). Wikipedia articles on statistics are, in general, excellent resources too, but might be a tad on the difficult side.

Aside from listing up some concepts you should be familiar with, I include a recap on population values and sample value. 

## What you should be familiar with
* Discrete and continuous probability distributions, densities, probability mass functions.
* Conditional probability distributions and Bayes' theorem.
* Expected values, ~~conditional expected value~~, variance, ~~conditional variance~~.
* Sample means, sample variances.
* The one- and two-sample *t*-tests. A rough understanding of what hypothesis testing, *p*-values, and confidence intervals are.
* Estimators, consistency and convergence in probability, ~~asymptotic normality~~, mean squared error.

## Population values and sample values
Many students struggles understanding the distinction between population values and values. The distinction between these two concepts is essential to all statistics, this course included. 
### Population values
Population values are theoretical. They tell us something about an ideal population as described by a probability distribution. Examples include he expected value, the population variance, the population median -- but there are infinitely many population values. All of these can in principle be calculated from the distribution of the random variable we look at. Such population values are often denoted by greek letters such as $\theta, \mu, \beta$ among others. 

### Sample values
Sample values, are known as statistics, are functions of observed data. Examples are the sample mean, sample variance, the sample median. 
* In practice, population values are unknown. The rôle of statistics is to try and measure them. This is known as *estimation*.
* An *estimator* of a population value is a sample value that is "supposed to measure" (the definition is left vague for a reason) the population value. An estimator of a population value $\theta$ is often denoted with a hat, i.e., $\hat{\theta}$. Sometimes we use the subscript $n$ to denote the estimator based on $n$ observations, as in $\hat{\theta}_n$.
    * The sample mean is an estimator of the population mean.
    * The sample variance is an estimator of the population variance.
* But there are other estimators than the naïve sample estimators! 
    * For instance, the you might estimate the mean using $\overline{X} - 1/n$, where $n$ is the sample size. This is still a meaningful and decent estimator of the mean. 
	* When $X_1,X_2,...$ are iid exponential with mean $\lambda$, we know the variance of $X$ is $\lambda^2$. You can verify this fact by looking at the [wikipedia page for the exponential distribution](https://en.wikipedia.org/wiki/Exponential_distribution). Thus $\hat{\lambda} = \textrm{sd}(X_1,X_2,\ldots,X_n)$ is an estimator of the mean $\lambda$. Verify this yourself!
* The quality of an estimator is often measured by the mean squared error: $E[(\hat{\theta} - \theta)^2]$, but infinitely many methods are available. The mean squared error is used since it's just very easy to work with mathematically.
	* We can decompose the mean squared error into two terms, the squared *bias* and the *variance* of the estimator: $E[(\hat{\theta} - \theta)^2] = \text{Var}(\hat{\theta}) + (E[\hat{\theta} - \theta])^2$. An estimator is *unbiased* if $E[\hat{\theta}] = \theta$, a property that is frequently mentioned *but not important*.
* An estimator $\hat{\theta}_n$  is consistent for $\theta$  if $\hat{\theta}_n \to \theta$  in probability as $n\to \infty$. We won't use the exact technical definition of convergence in probability in this course, but you can find it e.g. here.
* ***This might be new for you.*** An estimator $\hat{\theta}_n$ is asymptotically normal if there is an asymptotic variance $\sigma^2$ that makes $\sqrt{n}(\hat{\theta}_n - \theta) \stackrel{d}{\to} N(0,\sigma)$ as $n\to \infty$. Here $N(0,\sigma)$ denotes a normal random variable with standard deviation $\sigma$ and "$\stackrel{d}{\to}$" denotes convergence in distribution. 

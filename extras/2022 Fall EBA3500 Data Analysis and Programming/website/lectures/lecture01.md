---
tags: EBA3500
---
# Lecture 1: Ouverture, Numpy, and some Scipy

## Readings

### Study skills, Python, prerequisites
1. Be sure to have a look at the [prerequisities](https://hackmd.io/@JonasMoss/eba3500-prerequisites). We will recap some of this in the next lecture. Please add comments to the document if there is something you haven't covered yet, so I can try to include it in the recap.
2. The document about [honing your Python skills](https://hackmd.io/@JonasMoss/getting-better-at-python) is part of the curriculum, but you don't have to do everything I propose you do in it!
3. The note about [resources and workload](https://hackmd.io/@JonasMoss/eba3500-resources-workload).

### Numpy and Scipy
This is not a course about Numpy, but we will use it extensively. [Numpy for absolute beginners](https://numpy.org/doc/stable/user/absolute_beginners.html) serves as the main Numpy curriculum for this course. Expect to come back it multiple times! Roughly speaking you're expected to be able to quickly figure out how to solve a given Numpy task in e.g. the home exam, using methods laid out in that document, the Numpy documentation, the lectures, and lecture notes. Take Numpy seriously and do the exercises!

Below I write you should *familiarize yourself with* the numpy documentation and how Scipy handles distributions. This means that you should: 
1. Fire up and instance of [Visual Studio Code](https://code.visualstudio.com) (recommended), Jupyter Notebook, or your prefered way to write Python.
2. Go to the supplied links and *actively* read them. You can't just print out the documents and read them in the shade of a tree! You should make an hypothesis about how a snippet of code works, copy the Python code to your editor, and then modify it to check if your hypothesis is true.

### Curriculum / readings
1. [**Numpy for absolute beginners.**](https://numpy.org/doc/stable/user/absolute_beginners.html) Be aware that this guide does not use the right random number generator. We will use the new generator that [Numpy currently recommends](https://numpy.org/doc/stable/reference/random/generator.html); but we will cover this in more detail in Lecture 2.
2. Familiarize yourself with the [**Numpy documentation**](https://numpy.org/doc/stable/index.html). Pay particular attention to [array creation](https://numpy.org/doc/stable/user/basics.creation.html), [indexing](https://numpy.org/doc/stable/user/basics.indexing.html), [data types](https://numpy.org/doc/stable/user/basics.types.html), and [universal functions](https://numpy.org/doc/stable/user/basics.ufuncs.html)
3. We won't Scipy that much in this course, but you need to familiarize yourself with how it handles [**continuous distributions**](https://docs.scipy.org/doc/scipy/tutorial/stats/continuous.html) and [**discrete distributions**](https://docs.scipy.org/doc/scipy/tutorial/stats/discrete.html). These distributions share a number of generic *methods*, such as the mean, the pdf, and so on. We will use Scipy distributions and their methods liberally through the course. We will mostly be interested in the density function, distribution function, and quantile function (percent point function, or `ppf` in Scipy), but we will use other methods.

## Suggested additional readings
***These readings are not on the curriculum, but might be beneficial to look at either way.***
1. [**The illustrated guide to Numpy.**](https://betterprogramming.pub/numpy-illustrated-the-visual-guide-to-numpy-3b1d4976de1d) This guide does not use the random number generator that Numpy currently recommends. It's an alternative to Numpy for absolute beginners. 
2. [**From Python to Numpy**](https://www.labri.fr/perso/nrougier/from-python-to-numpy/) A very short book for the more ambitious students. Expects a higher level in Python than you get from the Python course at BI.

## Exercises
### Numpy exercises
1. **Some simple exercises.** How do you do the following in Numpy? Make sure to make your own example in Python!
    1. Make an identity matrix with `n` rows?
    2. Make a matrix consisting of $0$s only?
    3. Calculate the empirical mean of a vector? 
    4. Calculate the standard deviation of a vector normalized so that the variance is unbiased? (*Hint:* Read the docs to find out what I mean.) Which of these do you think we are most interested in in this course?
    5. Calculate "cumulative sum" operation on a vector `x`? (This operation creates a new vector `y` whose first element is `x[0]`, second `x[0] + x[1]`, etc.)
    6. Take the element-wise logarithm of a matrix?

2. **numpy-100.** The Github repo [Numpy-100](https://github.com/rougier/numpy-100) contains 100 Numpy exercises of variable difficulty. The Github page also includes hints and solutions. You can read the 100 problems [here](https://hackmd.io/@JonasMoss/numpy-100). There is no upper limit to how many of these you should do, but I would recommend to do at least 20, as these exercises are pretty short. The point is to [*grok*](https://www.vocabulary.com/dictionary/grok) Numpy. *Hint:* Use the Numpy documentation, Google, StackExchange, and so on. Check the hints if you have to. 

3. **Codewars.** Do this [Codewars exercise](https://www.codewars.com/kata/52fba2a9adcd10b34300094c) using Numpy indexing, i.e., not the built-in function `transpose`. You need to register at Codewars to do this exercise (which is harmless, and highly recommended).

### Scipy exercises
You will have to use to Scipy documention to solve these exercises. You should also use wikipedia liberally. Always remember, if you struggle a lot with an exercise, try the next one! You can always come back later.
1. **Exponential distribution.** Calculate the mean and standard deviation of the exponential distribution with location parameter $\lambda$ using Scipy. Use wikipedia to find the true values of the mean and standard deviation. Do they match?
2. **Log-normal.** The log-normal distribution is defined slightly differently in Scipy than on wikipedia. *Hint:* Read the documentation of `scipy-stats.lognorm`.  
3. **Normal distribution.** Use Scipy to calculate all $k$th moments (i.e., the expectation $E(X^k)$) of a normal distribution with mean $0$ and $\sigma=1,2$, $k < 20$. Do you notice a pattern? Use wikipedia to figure out exactly what the pattern is. 
4. **Plotting.** Make a function that creates a plot a `pdf` for user-specified bounds and an object of class `scipy.stats._continuous_distns`. The function should look `plotter(obj, lower = 0, upper = 4)`.
5. **Small investigation of the law of large numbers.** We''ll take a look at the law of large numbers for the log-normal with scale parameter `s=2` and the exponential with scale parameter `scale = 1`. Using Scipy, simulate `5, 10, 100, 1000` and calculate the population and sample means for both distribution. For which distribution does the law of large numbers appear to be quickst? For an extra challenge, plot the results for all `n = 10,20, ..., 10000` for both distribuions, in the same window, together with their population means. (Mimicking the picture in the [Wikipedia article](https://en.wikipedia.org/wiki/Law_of_large_numbers)).
7. **Nakagami distribution.** The Nakagami distribution is a special case of the gamma distribution, but with a different parameterization. Figure out how to translate the parameters of the Nakagami distribution to the parameters of the gamma distribution. Then plot both densities in the same window to verify your calculations. Use $\nu = 3$ in the Nakagami distribution.

---
tags: EBA3500
---

# Getting better at Python

You should probably learn more Python. Just like any art, the only way to get better is to practice while learning from the masters. Be aware of quick fixes; these are impossible. 

* This document is part of the curriculum in EBA3500, but the links are not. You're free to do with these resources as you like.
* The recommendations in this document might look overwhelming. But don't worry about that. The purpose of this document is to give you pointers to how to become better at Python.
* Be prepared to spend a lot of time learning how to program. You can't teach yourself how to program in 24 hours. [You'll have to spend 10 year instead!](https://www.norvig.com/21-days.html)
* You have two goals. 
	* **Professional programming.** You need your code to look professional, using the right tools, the vocabulary, and so on. Don't look like a noob!
	* **Better programming.** You need to be able to write and understand more programs.
* [This](https://towardsdatascience.com/how-to-write-high-quality-python-as-a-data-scientist-cde99f582675) is a decent document covering points similar to this one. For general tutorials on Python I find [RealPython](https://realpython.com) to have consistently hight quality, but always try to read the [documentation](https://docs.python.org/3/) first.

## Professional programming
* Follow the style guide [PEP](https://peps.python.org/pep-0008/).
* Use automatic formatters. I would recommend [black](https://medium.com/@evaGachirwa/improving-python-code-quality-using-pylint-and-black-5094dbebc1b2), as it doesn't give you any options.
* Document your functions using [`docstrings`](https://peps.python.org/pep-0257/#:~:text=A%20docstring%20is%20a%20string,module%20should%20also%20have%20docstrings.).
	* Follow one of the conventions laid out here. 
	* You might want to learn about [type hints](https://realpython.com/lessons/type-hinting/). These make your code easier to understand and debug.
* Try to look into [testing frameworks](https://realpython.com/python-testing/). 
* Use [modules](https://realpython.com/python-modules-packages/) to organize your work.
* Learn to use [Github (with their student pack)](https://docs.github.com/en/education/explore-the-benefits-of-teaching-and-learning-with-github-education/use-github-for-your-schoolwork/apply-for-a-student-developer-pack). You want to use Github due to its versions control and since it allows you to collaborate easily.

### How?
* You should try to apply your recently learned knowledge as often as possible. Have an assignment to write a Python function? Format it using `black`,  write a docstring for it, use typehints, put it into an appropriate module (such as an EBA3500) module, give it a proper name, and publish it on your Github page. You can also practice some of these skills using gamified sites such as [Codewars](https://www.codewars.com/dashboard).
* Another option is to work on random small projects, clean them up, and publish them on Github. Perhaps together with some of your costudents?

## Better programming
* **Object-oriented programming and classes.** The first priority is to learn about classes and object-oriented programming. Most Python libraries for statistics ([statsmodels](https://www.statsmodels.org/stable/index.html)) and machine learning ([scikit-learn](https://scikit-learn.org/stable/), [PyTorch](https://pytorch.org), [Keras](https://keras.io)) Python are built around classes.
- **Learn the features of the language.**
	- Make sure you know the [basic data structures]( [sets](https://docs.python.org/3/tutorial/datastructures.html#sets) ) of the language.
	- Skim the [standard library](https://docs.python.org/3/library/) and become familiar with the, for us at least, most important parts; [`collections`](https://docs.python.org/3/library/collections.html), [`itertools`](https://docs.python.org/3/library/itertools.html),  (and, perhaps [`string`](https://docs.python.org/3/library/string.html)). There are many exercises on e.g.  [Codewars](https://www.codewars.com/dashboard) (exercises ranked as 7kyu and 8kyu) that will help you with this.
	- Learn more advanced language features, such as [generators](https://realpython.com/introduction-to-python-generators/), the pattern matching operator `match`, context managers for handling files and connections (using the `with` statement), and nested list comprehensions.
	- Learn about common pitfalls. For instance, [be careful when removing elements from a list in a `for` loop,](https://towardsdatascience.com/3-rookie-mistakes-to-avoid-with-python-lists-625c0e8e57df)and be aware that [functions can modify their input.](https://www.dataquest.io/blog/tutorial-functions-modify-lists-dictionaries-python/) 
* **Algorithms and data structures.** Algorithms and data structures are about understanding how much time and memory programs require.  This is a big field, but some reasonable goals is to
	* This is a big field, but some reasonable goals is to understand the difference between $O(n)$,  $O(n^2)$, and $O(n\log n)$ algorithms, in addition what an exponential time algorithm is and why it's important to avoid them as much as you can. Also learn about why the dictionary is *far* faster than a list when doing lookups.
	* The highly competetive US job interviews at top tech companies such as Facebook, Google, Apple, Microsoft and Amazon are based on algorithms and data structures. This has created an enormous market for algorithms and data structure resources online, both free and paid. 
	* Exercises at [Codewars](https://www.codewars.com/dashboard) at rank about 5kyu and 6kyu cover intermediate algorithmic thinking.

### How?
* [Deliberate practice:](https://www.google.com/search?q=deliberate+practice+programming&sourceid=chrome&ie=UTF-8) You need to practice consistently  and for non-trivial amounts of time, e.g. 30 minutes per day. You might even want to join the [# #100DaysOfCode](https://www.100daysofcode.com) challenge!
* Do more than required on assignments.
* Play around with stuff! Perhaps your assignment could be solved with [sets](https://docs.python.org/3/tutorial/datastructures.html#sets) instead of lists? Try it!
* Read and try to answer Stack Overflow questions.

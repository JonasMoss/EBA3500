# Let's learn about dictionaries!
# - A fundamental data structure in Python.
# - An important component of "Pythonic" code.
# - Also known as "maps" and "associative arrays"
# - You must know about and preferably be really comfortable with dictionaries.
# - You need them for your own code, but even more importantly to understand
#   other people's code.
# - Should be a part of the first Python course, or maybe even a second one.
# - For more info, take a look at https://realpython.com/python-dicts/


# A dictionary associatiates _unique_ keys to values using the syntax key : value.
# A friendly beginner example is a list of friends the money they owe you. 
# Mario owes you 100$
# Luigi owes you 20$
# You owe Wario 100,000$!
# You owe Waluigi 10$!

owes_me = {"Mario" : 100, "Luigi" : 20, "Wario" : -100,000, "Waluigi" : -10} 
print(owes_me)

# Who did you lend / borrow money to / from?
owes_me.keys()
# And how much do they owe you?
owes_me.values()
# How much do you owe in total?
sum(owes_me.values()) # Ouch :(

# Not all friends are equal; you like Mario a little more than Luigi, who you
# like much more than Waluigi, and you destest Wario. You also like Princess
# Peach quite a bit.

i_like =  {"Luigi" : 9, "Wario" : 0, "Mario" : 10, "Waluigi" : 4, "Peach" : 7} 


# Associative arrays are useful in classical computer science too. 
# Here comes an advanced example! 

# Problem: You have a list of lists 
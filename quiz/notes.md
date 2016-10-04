# Quiz Notes!

## Problem 1

All these questions are True/False

### Problem 1-1:

`x, y` is a list.  You can assign variables in a list to values in another
list.  e.g. `x, y = y, x` will swap the values assigned to `x` and `y`,
respectively.
(See Section 5.1.1 "Sequences and Muliple Assignment" p. 57 in Textbook.)

### Problem 1-2:
Suppose `x` is an integer in the following code:

```python
def f(x):
    while x > 3:
        f(x+1)
```
For any value of x, all calls to f are guaranteed to never terminate.
False. values <= 3 will not cause infinite loops.

### Problem 1-3:

A Python program always executes every line of code written at least once.
False. Python is an intepreted language, not compiled. Control flow allows us
to not execute lines of code

### Problem 1-4:

Python has function scoping. Variables defined within functions are only
accessible within that function.

### Problem 1-5:

Negative values for `i` and `j` will not cause an infinite loop.

### Problem 1-6:
It is always possible and feasible for a programmer to come up with test cases
that run through every possible path in a program.  **False** Must be referring
to all possible inputs, not lines hit.

### Problem 1-7:
Assume `f()` is defined. In the statement `a = f()`, `a` is always a function.
False. We are calling the function with `f()`, so the return value could be
something other than another function.

### Problem 1-8:
A program that keeps running and does not stop is an example of a syntax error.
Nope.

### Problem 1-9:

```python
def f(x):
    a = []
    while x > 0:
        a.append(x)
        f(x-1)
```
A new object of type list is created for each recursive invocation of `f`.
True.

### Problem 1-10:
A tuple can contain a list as an element.
[True](https://docs.python.org/3/tutorial/datastructures.html#tuples-and-sequences)

## Multiple Choice (Select one)

### Problem 2-1:

A dictionary maps strings to integers.

### Problem 2-2:

Break statments will always terminate the immediate loop, which **may**
terminate the function or entire program.


### Problem 2-3:
In Python, which of the following is a mutable object?

[ ] a string
[ ] a tuple
[x] a list

Lists are mutable. Strings and tuples are immutable.
Section 5.4 "Strings, Tuples and Lists" (p. 66)

### Problem 2-4:
Assume the statement `s[1024] = 3` does not produce an error message. This implies:
[ ] `type(s)` can be `str`
[ ] `type(s)` can be `tuple`
[x] `type(s)` can be `list`

Notice that `s[1024] = 3` is an assignment statement. In this case, only a list
would not produce an error message, since lists are mutable. Strings and tuples
and both immutable (they cannot be changed), and they would throw errors.

### Problem 2-5:

All options other than the for loop incorrectly index the data structure.

## Multiple Choice (Select all that apply)

A for loop will only loop over the outermost collection.
Loop over a string with a for loop will loop over the individual characters.

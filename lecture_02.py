# def my_recursion(n):
#     print(n)
#     my_recursion(n+1)

# my_recursion(1)


###################

# def my_recursion(n):
#     print(n)
#     if n == 5:

#         return
#     # else:   <--- don't need this.
#     my_recursion(n+1)

# my_recursion(1)

"""You usually don't want to do a for loop or while loop inside a recursion.
It may work, but it's usually a decision you want to make iteratively.
Generally speaking, recursion does the iteration.  It's a different method of it."""

"""PATH THE PROGRAM TAKES: it calls the function
Like in line 18.  Calling my_recursion with a value of 1. 
1. We go into my recursion
2. We add second line to print(1) on the call stack
3. Afterwards we return it (whether implicitly or explicitly)
4. It exits, or we return that to the stack
5. Then we're comparing lines 12 and 16.  print(2) checks if == 5, if not, exits stack
6. print(3) checks if == 5.  it's not, so it returns.
"""

# # #####################
# def my_recursion(n):
#     print(n)
#     if n == 3:
#         return

#     my_recursion(n+1)
#     print('first recursion')
#     my_recursion(n+1)
#     print('second recursion')

# my_recursion(1)

"""
It gets really interesting how this adds up.
Might need to look up a tree / video on how recursion works visually.

Look this up on pythontutor.com***
"""

"""
How do you know if a problem is suitable for recursion?
====================================================
When you break a problem down into pieces, 
And every piece that you have (problem) is a smaller dataset.

It can take a problem that is too big for you to understand by yourself,
and it can help you understand printing out those numbers because it's 
too big to hold.
"""

"""
NEW TOPIC: FIBONACCI

0, 1 - base; if we solve the base recursively
        (what do you always do to base case?  move towards it)

# 0, 1, 1, 2, 3, 5, 8, 13, 21, 34

Why does Fibonacci's sequene make for a good recursion example?

Because it can be reduced to repeatable basecase.

10th fib number: 9th fib + 8th fib
9th fib #: 8th fib + 7th fib
8th fib #: 7th fib + 6th fib
7th fib #: 6th fib + 5th fib
"""

# # Print the nth fib number
# def recursive_fib(n):
#     # base case
#     # test for negatives (TODO)
#     # if n is 0
#     if n == 0:
#         return 0
#     # return 0
#     # if n is 1
#     if n == 1:
#         return 1
#     # return 1

#     # If we're not on the base case
#     # return recursion of n-1 and n-2
#     n_minus_1 = recursive_fib(n-1)
#     n_minus_2 = recursive_fib(n-2)
#     return n_minus_1 + n_minus_2

# # print(recursive_fib(10))
# # answer: 55.  Looks like it works.

# print(recursive_fib(5))
# # Once you start getting to upper 30's on that function,
# # it starts to get really slow.  This naive solution may not
# # be the best solution for 10-20 things.  

"""
The second recursion doesn't hit until the first 
recursion reaches the base case
"""

"""
Last 20 minutes of lecture
# Quick Sort - **NEW CONCEPT**
[ 5 9 3 7 2 8 1 6]

# Pick first number
[3 2 1]  [5]   [9 7 8 6]

# Recurse Left
[2 1][3][]   [5] [9 7 8 6]

# Recurse Left
[1][2][][3][]    [5] [9 7 8 6]

# Recurse Right
# Empty array, base case

# Recurse Right
# Empty array, base case

# Recurse Right
[1] [2] [] [3] []    [5]    [9 7 8 6]
[1] [2] [] [3] []    [5]    [7 8 6][9][]

# Recurse left
[1][2][][3][]        [5]   [6][7][8][  ][9][]

[1, 2] [3]
[1, 2, 3]
"""

# PLAN
# Base case: if array length 0 or 1
#    return array
# else:
# pick pivot - might as well pick first because it's unsupported,, none are better
# put anything smaller into left array
# put anything bigger into right array
# return quicksort(left) + quicksort(right)
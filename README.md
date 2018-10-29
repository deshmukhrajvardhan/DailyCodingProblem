# DailyCodingProblem
My solutions to coding challenges from https://dailycodingproblem.com

Here is my approach for coding challenges I i receive from [dailycodingproblem.com](http://dailycodingproblem.com). I am using **Python** however problems are of course language-independent. Feel free to create a new issue thread for your questions or suggestions.

## 002
This problem was asked by Uber.

Given an array of integers, return a new array such that each element at index i of the new array is the product of all the numbers in the original array except the one at i.

For example, if our input was [1, 2, 3, 4, 5], the expected output would be [120, 60, 40, 30, 24]. If our input was [3, 2, 1], the expected output would be [2, 3, 6].

Follow-up: what if you can't use division?

### Solution
[Py](solutions/question2.py)

## 003
This problem was asked by Google.

Given the root to a binary tree, implement serialize(root), which serializes the tree into a string, and deserialize(s), which deserializes the string back into the tree.

For example, given the following Node class
```
class Node:
    def __init__(self, val, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
```
The following test should pass:

```node = Node('root', Node('left', Node('left.left')), Node('right'))
assert deserialize(serialize(node)).left.left.val == 'left.left'
```

### Solution
[Py](solutions/question3.py)


## 004
This problem was asked by Stripe.

Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input `[3, 4, -1, 1]` should give 2. The input `[1, 2, 0]` should give 3.

You can modify the input array in-place.

### Solution
[Py](solutions/question4.py)


## 005


This problem was asked by Jane Street.

cons(a, b) constructs a pair, and car(pair) and cdr(pair) returns the first and last element of that pair. For example, car(cons(3, 4)) returns 3, and cdr(cons(3, 4)) returns 4.

Given this implementation of cons:
```
def cons(a, b):
    def pair(f):
        return f(a, b)
    return pair
```
Implement car and cdr.
### Solution
[Py](solutions/question5.py)

# Python Excercises (Task 0)

Create a file `solution.py` with the described functions and a file `test.py` that will evaluate them for a selected set of inputs (your choice).

## Excercise 1

Create a function `Newton(n,m)` which for integers `n` and `m` will return an integer equal to the the [binomial coefficient](https://en.wikipedia.org/wiki/Binomial_coefficient) n over m. Which is equal to:

![n over m](https://latex.codecogs.com/gif.latex?\\left(\\begin{matrix}n\\\\m\\end{matrix}\\right)%3D\\frac{n!}{m!(n-m)!})

Do it so that the result will be still good for high values of `n`

## Excercise 2

Create a function `Pascal(n)` which will return a list of `n` rows of elements of the [Pascal triangle](https://en.wikipedia.org/wiki/Pascal's_triangle). The result should be a list of length `n`. The elements of this list should be also lists, of increasing length (from 1 to `n`). For example:
```python
> Pascal(4)
[ [1], [1,1], [1,2,1], [1,3,3,1] ]
```

## Excercise 3

Create a function `LotOfHash(n)` which will print one line for each row of the Pascal Triangle, in which all the odd numbers will be printed as `#`. For example:
```python
> LotOfHash(6)
#
##
# #
####
#   #
##  ##
```
Consider how to do it for high values of `n`

## Excercise 4

Implement a function `PowerModulo(a,b,c)` which will calculate ![a^b mod n](https://latex.codecogs.com/gif.latex?a^b\\quad\\text{mod }n).
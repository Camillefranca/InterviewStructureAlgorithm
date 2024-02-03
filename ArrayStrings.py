# import requests
# import mysql.connector
# import pandas as pd

# Given a corpus of text and a number k, write some code to find the top k terms in that text.
# Example
# text: b a b a a c
# k: 2

# Result: ["a", "b"] since a occurs 3 times, b 2 times.


# [ 'b', 'a', 'b', 'a', 'a', 'c']
# k: 2
# [b; 2, a; 3, c; 1] -> [a, b]

# ArrayStrings = [ 'b', 'a', 'b', 'a', 'a', 'c']
# for i in range(ArrayStrings):
#   if i = i:
#      i =+

# dictionary = {}
# dictionary["a"] = 3
# ArrayStrings[i] -> "a": 3
# sorted(d.items(), key=lambda x: x[1])


  
ArrayStrings = ['b', 'a', 'b', 'a', 'a', 'c']
ArrayResult = {}
for i in ArrayStrings:
    if i in ArrayResult:
        ArrayResult[i] = ArrayResult[i] + 1
    else:
        ArrayResult[i] = 1
      
print(sorted(ArrayResult.items(), key=lambda x: x[1]))

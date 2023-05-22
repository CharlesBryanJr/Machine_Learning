'''file_name'''
# pylint: disable=C0114
# pylint: disable=E1101
# pylint: disable=C0103
# pylint: disable=E1101
# pylint: disable=C0116
# pylint: disable=C0115
# pylint: disable=W0105
# pylint: disable=C0304
# pylint: disable=W0621
print(" ")

'''

Type of Question:
- math concepts

Clarifying Questions / Insights:
- X and Y will 
    - consist of positive integers up to 1000.
    - have cardinalities between 1 and 10 inclusive.
- You shouldn't use any libraries.
- automatically round output values to the fourth decimal.

Input:
- Intuitive
- Primitive Types
		- Numbers
			- Zero (0)
			- NULL or nil
			- Negative Numbers
			- Floats or Doubles (clarifies if Ints only?)
			- Min/Max Int
		- Arrays
			- Empty array
			- Nested or not nested

Output:
- the Euclidean distance between X and Y
- the Manhattan distance between X and Y
- the Cosine similarity of X and Y.
- the Jaccard similarity of X and Y.
'''

from math import pow, sqrt

# Time: O() | # Space: O()
class Metrics():
   def euclidean_distance(self, X, Y):
       return sqrt(sum((pow(x - y, 2)) for x, y in zip(X, Y)))

   def manhattan_distance(self, X, Y):
       return sum(abs(x - y) for x, y in zip(X, Y))

   def cosine_similarity(self, X, Y):
       numerator = sum((x * y) for x, y in zip(X, Y))
       denominator = sqrt(sum([x * x for x in X])) * sqrt(sum([y * y for y in Y]))
       return numerator / float(denominator)

   def jaccard_similarity(self, X, Y):
       intersection_cardinality = len(set.intersection(*[set(X), set(Y)]))
       union_cardinality = len(set.union(*[set(X), set(Y)]))
       return intersection_cardinality / float(union_cardinality)

def distances_and_similarities(X, Y):
   metrics = Metrics()
   return [metrics.euclidean_distance(X, Y),
           metrics.manhattan_distance(X, Y),
           metrics.cosine_similarity(X, Y),
           metrics.jaccard_similarity(X, Y)]

X = [1, 3, 4, 5]
Y = [7, 6, 3, 1]
print("X:", X)
print("Y:", Y)
print("distances_and_similarities:", distances_and_similarities(X, Y))
print(" ")
'''
X = [1]
Y = [1]
print("X:", X)
print("Y:", Y)
print("distances_and_similarities:", distances_and_similarities(X, Y))
print(" ")


X = [12, 15, 27, 88, 11, 34, 24]
Y = [7, 6, 3, -1]
print("X:", X)
print("Y:", Y)
print("distances_and_similarities:", distances_and_similarities(X, Y))
print(" ")


# _recursion
# _iteration
print(" ")
'''
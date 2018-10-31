# Creating an Empty Hash Table
# Define a procedure, make_hashtable,
# that takes as input a number, nbuckets,
# and returns an empty hash table with
# nbuckets empty buckets.


def make_hashtable(nbuckets):
    index = []
    buckets = 0
    while buckets < nbuckets:
        index.append([])
        buckets += 1
    return index


print make_hashtable(8)

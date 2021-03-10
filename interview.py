# Given a list of length N+1 with possible values from 1-N inclusive, create a function “find_dupes” that returns a duplicate

from random import sample, randrange

def dups(dups) :
    seen = {}

    for x in dups:
        if x not in seen:
            seen[x] = 1
        else:
            if seen[x] == 1:
                return x
            seen[x] += 1
    return x


def test(length) :
    # length is num of lists
    for x in range(length):
        size = randrange(2, 20)
        num_list = []

        for i in range(size):
            num_list.append(randrange(1, size))

        results = dups(num_list)

        if num_list.count(results) <= 1 :
            return False
    return True
    
    
print(test(100000))

# Create a function that will create random test inputs, run find_dupes against them, and verify the results of find_dupes are correct. Return true if all random inputs are correct, false otherwise

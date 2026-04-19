import itertools

def permutatsiya_soni(string):
    return len(set(itertools.permutations(string)))

string = input("Istalgan stringni kiriting: ")
print(permutatsiya_soni(string))

# Permutation - Arrangement
# Combination - Selection

def permutation(s):

    out = []
    # Base Case
    if len(s) == 1:
        out = [s]

    else:
        # for every letters in string
        for i, let in enumerate(s):
        # Permututation of other two elements
            for perm in permutation(s[:i]+ s[i+1:]):

                out += [let+ perm]
    return out

print(permutation("abc"))


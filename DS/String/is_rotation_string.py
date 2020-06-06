def is_rotation(st1, st2):
    return (st1+st2).count(st2) > 0
print(is_rotation("waterbottle", "erbottlewat"))
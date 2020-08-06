def backspaceCompare(S, T):
    kiran = rakz = []
    for i in range(len(S)):
        if S[i].isalpha():
            kiran.append(S[i])
        else:
            kiran.pop()
    for i in range(len(T)):

        if T[i].isalpha():
            rakz.append(T[i])
        else:
            rakz.pop()

    print(kiran)
    print(rakz)
    return kiran == rakz

print(backspaceCompare("ab#c","ad#c"))
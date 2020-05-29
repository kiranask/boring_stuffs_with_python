def frequencySort(s):
    """
    :type s: str
    :rtype: str
    """
    freq = {}
    for i in s:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
    print("new",freq)
    output = ""
    newDict = sorted(freq.items(), key=lambda kv: kv[1], reverse=True)
    print("newww", newDict)
    for k, v in newDict:
        for i in range(v):
            output += k
    return output

print(frequencySort('tetestst'))
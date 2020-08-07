class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        kiran, rakz = [], []
        for i in range(len(S)):
            if S[i] != "#":
                kiran.append(S[i])
            elif len(kiran) > 0:
                kiran.pop()
        for i in range(len(T)):
            if T[i] != "#":
                rakz.append(T[i])
            elif len(rakz) > 0:

                rakz.pop()
        return kiran == rakz


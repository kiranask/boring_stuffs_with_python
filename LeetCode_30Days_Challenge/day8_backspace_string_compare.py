class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def backspace(Str):
            _list =[]
            for i in range(len(Str)):
                if Str[i] != "#":
                    _list.append(Str[i])
                elif len(_list) > 0:
                    _list.pop()
            return _list
        return backspace(S) == backspace(T)




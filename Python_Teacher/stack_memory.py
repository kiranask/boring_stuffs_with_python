def func1():
    x = 10  # stored in stack
    func2()

def func2():
    y = 20  # stored in stack
    print("Inside func2")

func2()

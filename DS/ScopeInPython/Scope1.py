count = 5
def some_method():
    global count
    count = count + 1
    print(count)
some_method()
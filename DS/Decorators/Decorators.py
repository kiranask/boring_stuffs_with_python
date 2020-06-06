def checkpositive(check):
    def checknums(*args):
        for num in args:
            if num > 0:
                return check(*args)

            else:
                print("Positive numbers")
                return

    return checknums


@checkpositive
def kiran(num1, num2):
    print("Success")

print(kiran(-11,2))
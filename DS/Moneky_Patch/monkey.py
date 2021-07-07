from DS.Moneky_Patch import monk
def monkey_f(self):
	print ("monkey_f() is being called")

# replacing address of "func" with "monkey_f"
monk.A.func = monkey_f
obj = monk.A()

# calling function "func" whose address got replaced
# with function "monkey_f()"
obj.func()

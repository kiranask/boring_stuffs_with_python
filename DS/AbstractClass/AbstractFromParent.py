# Python program showing 
# implementation of abstract 
# class through subclassing 

class parent:	 
	def geeks(self): 
		pass

class child(parent): 
	def geeks(self): 
		print("child class") 

# Driver code 
print( issubclass(child, parent)) 
print( isinstance(child(), parent)) 

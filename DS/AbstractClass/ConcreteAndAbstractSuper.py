# Python program invoking a
# method using super()
# super > Call Overriden Parent calss same  Method

from abc import ABC

class R(ABC):
	def rk(self):
		print("Abstract Base Class")

class K(R):
	def rk(self):
		print("subclass ")
		super().rk()

# Driver code
r = K()
r.rk()

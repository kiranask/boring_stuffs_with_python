#Local Scope
print(1)
def myfunc():
  x = 300
  print(x)

myfunc()
print('-----------------')

print(2)
# Function inside function

def myfunc():
  x = 300
  def myinnerfunc():
    print(x)
  myinnerfunc()

myfunc()
print('-----------------')
print(3)
# Global Scope:

x = 300

def myfunc():
  print(x)

myfunc()

print(x)

print('-----------------')
print(4)
# naming Varibles:

x = 300

def myfunc():

  print(x)

myfunc()

print(x)
print('-----------------')
print(5)
x = 200
print(x)
def myfunc():
  global x
  x = 300

myfunc()

print(x)
print("-----------")




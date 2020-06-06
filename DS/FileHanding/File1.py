f = open("kiran.txt",'r')
f1 = open("abc","w")
f1.write("Mobile")
for data in f:
    f1.write(data)
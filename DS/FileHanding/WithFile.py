with open('myfile.txt','r') as fh:
    print(fh.read())
    lines = fh.readlines()
    g_counter = 0
    for line in lines:
        for word in line.split(" "):
            if "Geeks" in word.strip():
                g_counter+=1
    print(g_counter)

for line in open('kiran.txt'):
    print(line.strip())
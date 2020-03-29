
f = open("test1.txt", "r")

line = f.readline()

while line:
    print(line.strip())
f = open('data.txt', 'r')
data = f.read()
f.close()
f = open('output.txt', 'x')
f.close()
for i in range(len(data)):
    f = open('output.txt', 'a')
    print(data[i])
    if data[i] != '\n':
        f.write(data[i])
    f.close()
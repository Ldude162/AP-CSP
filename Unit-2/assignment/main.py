f = open('data.txt', 'r')
data = f.read()
f.close()
prev = 0
f = open('temp.txt', 'a')
for i in range(len(data)):
    if i > 264:
        f.write(data[i])
f.close()
f = open('temp.txt', 'r')
newdata = f.read()
f.close()
split_strings = []
n  = 3
for index in range(0, len(newdata), n):
    split_strings.append(newdata[index : index + n])
print(split_strings)

for i in split_strings: 
    if i == "TAG" or i == "ATG" or i == "TAA" or i == "TGA":
        f = open('output.txt', 'a')
        f.write(i + ' ')
        f.close()

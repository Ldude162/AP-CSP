f = open('data.txt', 'r')
data = f.read()
f.close()
prev = 0
split_strings = []
n  = 3
for i in range(0, len(data), n):
    split_strings.append(data[i : i + n])
print(split_strings)

index = 1
num = 1
gene = False
for i in split_strings: 
    if i == 'ATG' and gene != True:
        gene = True
        f = open('positions.txt', 'a')
        f.write('start ' + str(num) + ' is at ' + str(index * 3 - 2) + '\n')
        f.close()
    elif i == 'TAG' or i == 'TAA' or i == 'TGA' and gene == True:
        gene = False
        f = open('positions.txt', 'a')
        f.write('end ' + str(num) + ' is at ' + str(index * 3 - 2) + '\n')
        f.close()
        num += 1
    index += 1
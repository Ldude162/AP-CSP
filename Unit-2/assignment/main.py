f = open('data.txt', 'r')
data = f.read()
f.close()
prev = 0
split_strings = []
n  = 3
for i in range(0, len(data), n):
    split_strings.append(data[i : i + n])
print(split_strings)

index = 0
num = 1
gene = False
for i in split_strings: 
    if i == 'ATG' and gene != True:
        gene == True
        f = open('positions.txt', 'a')
        f.write('start ' + str(num) + ' is at')
    elif i == 'TAG' or i == 'TAA' or i == 'TGA' and gene == True:
        #enter code here
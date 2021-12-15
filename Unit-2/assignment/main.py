#read the data
f = open('data.txt', 'r')
data = f.read()
f.close()
newData = data[265:]
 
num = 1
prevLetters = ['z', 'z']
for i in range(len(newData)):
    if prevLetters[0] == 'A' and prevLetters[1] == 'T' and newData[i] == 'G':
        f = open('positions.txt', 'a')
        f.write('start ' + str(num) + ' is at ' + str(i + 264) + '\n')
        f.close()
        newNewData = newData[i + 1:]
        prev = 0
        split_strings = []
        n  = 3
        for a in range(0, len(newData), n):
            split_strings.append(newData[a : a + n])
        index = 1
        for b in split_strings:
            if b == 'TAG' or b == 'TAA' or b == 'TGA':
                f = open('positions.txt', 'a')
                f.write('end ' + str(num) + ' is at ' + str(index * 3 + 261 + i) + '\n')
                f.close()
                print(b)
                num += 1
                i = index * 3 + 261 + i
                break
            index += 1
    prevLetters[0] = prevLetters[1]
    prevLetters[1] = newData[i]
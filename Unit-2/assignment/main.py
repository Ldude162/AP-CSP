#read the data
f = open('data.txt', 'r')
data = f.read()
f.close()
newData = data[265:]
 
num = 1
#stores the 2 previous letters, the z's are placeholders for the first 2 iterations
prevLetters = ['z', 'z']
i = 0
#Loops through all of the letters
while i < len(newData):
    if num > 18:
        break
    #Checks if there is an ATG
    if prevLetters[0] == 'A' and prevLetters[1] == 'T' and newData[i] == 'G':
        # write down the position of the atg
        f = open('positions.txt', 'a')
        f.write('start ' + str(num) + ' is at ' + str(i + 264) + '\n')
        f.close()
        # Get the data from the ATG
        newNewData = newData[i + 1:]
        # split the strings into parts of 3
        split_strings = []
        n  = 3
        for a in range(0, len(newNewData), n):
            split_strings.append(newNewData[a : a + n])
        index = 1
        # search through all of the parts
        for b in split_strings:
            # if it is one of the stop codons
            if b == 'TAG' or b == 'TAA' or b == 'TGA':
                f = open('positions.txt', 'a')
                # writes down the position of the stop
                f.write('end ' + str(num) + ' is at ' + str(index * 3 + 263 + i) + '\n')
                f.close()
                print(b)
                num += 1
                # set the next character to check for
                a = index * 3 + i
                print(i)
                try:
                    prevLetters[1] = newData[a - 1]
                except:
                    print('failed at ' + str(i))
                    prevLetters[0] = newData[a - 2]
                i = a
                # stop checking for other stop codons
                break
            index += 1
    else:
        prevLetters[0] = prevLetters[1]
        prevLetters[1] = newData[i]
        i += 1
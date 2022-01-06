f = open('data.txt', 'r')
data = f.read()
f.close()
newData = data[265:]
 
num = 1
amminoIndex = 1
lineIndex = 1

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
        f = open('output.txt', 'a')
        f.write('gene ' + str(num) + ' :\n')
        f.write(str(amminoIndex) + ' ')

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
                f = open('output.txt', 'a')
                f.write('\n')
                print(b)
                num += 1
                # set the next character to check for
                a = index * 3 + i
                print(i)
                try:
                    prevLetters[0] = newData[a - 2]
                    prevLetters[1] = newData[a - 1]
                except:
                    print('failed at ' + str(i))
                i = a
                amminoIndex = 1
                lineIndex = 1
                # stop checking for other stop codons
                break
            else:
                b = b.lower()
                for d in range(len(b)):
                    if lineIndex == 51:
                        f = open('output.txt', 'a')
                        f.write('\n' + str(amminoIndex) + ' ' + b[d])
                        f.close()
                        lineIndex = 2
                        amminoIndex += 1
                    elif lineIndex == 11 or lineIndex == 21 or lineIndex == 31 or lineIndex == 41:
                        f = open('output.txt', 'a')
                        f.write(' ' + b[d])
                        f.close()
                        lineIndex += 1
                        amminoIndex += 1
                    else:
                        f = open('output.txt', 'a')
                        f.write(b[d])
                        f.close()
                        lineIndex += 1
                        amminoIndex += 1
            index += 1
    else:
        prevLetters[0] = prevLetters[1]
        prevLetters[1] = newData[i]
        i += 1
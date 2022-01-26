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
                f.write('end ' + str(num) + ' is at ' + str(index * 3 + 266 + i) + '\n')
                f.close()
                f = open('output.txt', 'a')
                f.write('\n')
                print(b)
                num += 1
                # set the next character to check for
                a = index * 3 + i + 2
                print(i)
                try:
                   prevLetters[0] = 'z' #newData[a - 2]
                   prevLetters[1] = 'z' #newData[a - 1]
                except:
                    print('failed at ' + str(i))
                i = a
                amminoIndex = 1
                lineIndex = 1
                # stop checking for other stop codons
                break
            else:
                b = b.lower()


                if b == 'ttt':
                    c = 'f'
                elif b == 'ttc':
                    c = 'f'
                elif b == 'tta':
                    c = 'l'
                elif b == 'ttg':
                    c = 'l'
                elif b == 'ctt':
                    c = 'l'
                elif b == 'ctc':
                    c = 'l'
                elif b == 'cta':
                    c = 'l'
                elif b == 'ctg':
                    c = 'l'
                elif b == 'att':
                    c = 'i'
                elif b == 'atc':
                    c = 'i'
                elif b == 'ata':
                    c = 'i'
                elif b == 'atg':
                    c = 'm'
                elif b == 'gtt':
                    c = 'v'
                elif b == 'gtc':
                    c = 'v'
                elif b == 'gta':
                    c = 'v'
                elif b == 'gtg':
                    c = 'v'
                elif b == 'tct':
                    c = 's'
                elif b == 'tcc':
                    c = 's'
                elif b == 'tca':
                    c = 's'
                elif b == 'tcg':
                    c = 's'
                elif b == 'cct':
                    c = 'p'
                elif b == 'ccc':
                    c = 'p'
                elif b == 'cca':
                    c = 'p'
                elif b == 'ccg':
                    c = 'p'
                elif b == 'act':
                    c = 't'
                elif b == 'acc':
                    c = 't'
                elif b == 'aca':
                    c = 't'
                elif b == 'acg':
                    c = 't'
                elif b == 'gct':
                    c = 'a'
                elif b == 'gcc':
                    c = 'a'
                elif b == 'gca':
                    c = 'a'
                elif b == 'gcg':
                    c = 'a'
                elif b == 'tat':
                    c = 'y'
                elif b == 'tac':
                    c = 'y'
                elif b == 'cat':
                    c = 'h'
                elif b == 'cac':
                    c = 'h'
                elif b == 'caa':
                    c = 'q'
                elif b == 'cag':
                    c = 'q'
                elif b == 'aat':
                    c = 'n'
                elif b == 'aac':
                    c = 'n'
                elif b == 'aaa':
                    c = 'k'
                elif b == 'aag':
                    c = 'k'
                elif b == 'tgt':
                    c = 'c'
                elif b == 'tgc':
                    c = 'c'
                elif b == 'tgg':
                    c = 'w'
                elif b == 'cgt':
                    c = 'r'
                elif b == 'cgc':
                    c = 'r'
                elif b == 'cga':
                    c = 'r'
                elif b == 'cgg':
                    c = 'r'
                elif b == 'aga':
                    c = 'r'
                elif b == 'agg':
                    c = 'r'
                elif b == 'agt':
                    c = 's'
                elif b == 'agc':
                    c = 's'
                elif b == 'ggt':
                    c = 'g'
                elif b == 'ggt':
                    c = 'g'
                elif b == 'ggc':
                    c = 'g'
                elif b == 'gga':
                    c = 'g'
                elif b == 'ggg':
                    c = 'g'
                
                if lineIndex == 51:
                    f = open('output.txt', 'a')
                    f.write('\n' + str(amminoIndex) + ' ' + c)
                    f.close()
                    lineIndex = 2
                    amminoIndex += 1
                elif lineIndex == 11 or lineIndex == 21 or lineIndex == 31 or lineIndex == 41:
                    f = open('output.txt', 'a')
                    f.write(' ' + c)
                    f.close()
                    lineIndex += 1
                    amminoIndex += 1
                else:
                    f = open('output.txt', 'a')
                    f.write(c)
                    f.close()
                    lineIndex += 1
                    amminoIndex += 1
                
            index += 1
    else:
        prevLetters[0] = prevLetters[1]
        prevLetters[1] = newData[i]
        i += 1
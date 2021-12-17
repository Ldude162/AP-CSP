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
        f = open('output.txt', 'a')
        f.write('gene ' + str(num) + ' :\n')
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
                f.write('end ' + str(num) + ' is at ' + str(index * 3 + 264 + i) + '\n')
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
                # stop checking for other stop codons
                break
            elif b == 'TTT' or b == 'TTC':
                f = open('output.txt', 'a')
                f.write('Phenylalanine, ')
                f.close
            elif b == 'TTA' or b == 'TTG' or b == 'CTT' or b == 'CTC' or b == 'CTA' or b == 'CTG':
                f = open('output.txt', 'a')
                f.write('Leucine, ')
                f.close
            elif b == 'ATT' or b == 'ATC' or b == 'ATA':
                f = open('output.txt', 'a')
                f.write('Isoleucine, ')
                f.close
            elif b == 'ATG':
                f = open('output.txt', 'a')
                f.write('Methiesine, ')
                f.close
            elif b == 'GTT' or b == 'GTC' or b == 'GTA' or b == 'GTG':
                f = open('output.txt', 'a')
                f.write('Valine, ')
                f.close
            elif b == 'TCT' or b == 'TCC' or b == 'TCA' or b == 'TCG':
                f = open('output.txt', 'a')
                f.write('Serine, ')
                f.close
            elif b == 'CCT' or b == 'CCC' or b == 'CCA' or b == 'CCG':
                f = open('output.txt', 'a')
                f.write('Preline, ')
                f.close
            elif b == 'ACT' or b == 'ACC' or b == 'ACA' or b == 'ACG':
                f = open('output.txt', 'a')
                f.write('Threonine, ')
                f.close
            elif b == 'GCT' or b == 'GCC' or b == 'GCA' or b == 'GCG':
                f = open('output.txt', 'a')
                f.write('Alanine, ')
                f.close
            elif b == 'TAT' or b == 'TAC':
                f = open('output.txt', 'a')
                f.write('Tyrosine, ')
                f.close
            elif b == 'CAT' or b == 'CAC':
                f = open('output.txt', 'a')
                f.write('Histidine, ')
                f.close
            elif b == 'CAA' or b == 'CAG':
                f = open('output.txt', 'a')
                f.write('Glutamine, ')
                f.close
            elif b == 'AAT' or b == 'AAC':
                f = open('output.txt', 'a')
                f.write('Asparagine, ')
                f.close
            elif b == 'GAT' or b == 'GAC':
                f = open('output.txt', 'a')
                f.write('Aspartic Acid, ')
                f.close
            elif b == 'GAA' or b == 'GAG':
                f = open('output.txt', 'a')
                f.write('Glutamic Acid, ')
                f.close
            elif b == 'TGT' or b == 'TGC':
                f = open('output.txt', 'a')
                f.write('Cyatine, ')
                f.close
            elif b == 'TGG':
                f = open('output.txt', 'a')
                f.write('Tryptophan, ')
                f.close
            elif b == 'CGT' or b == 'CGC' or b == 'CGA' or b == 'CGG' or b == 'AGA' or b == 'AGG':
                f = open('output.txt', 'a')
                f.write('Arginine, ')
                f.close
            elif b == 'AGT' or b == 'AGC':
                f = open('output.txt', 'a')
                f.write('Serine, ')
                f.close
            elif b == 'GGT' or b == 'GGC' or b == 'GGA' or b == 'GGG':
                f = open('output.txt', 'a')
                f.write('Glycine, ')
                f.close
            index += 1
    else:
        prevLetters[0] = prevLetters[1]
        prevLetters[1] = newData[i]
        i += 1
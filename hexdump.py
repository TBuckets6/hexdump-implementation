import sys

# def main():
#     data = openAndReadFile()
    
fd = open(sys.argv[1], "rb")
data = fd.read()


# def openAndReadFile():
#     fd = open(sys.argv[1], "rb")
#     data = fd.read()
#     return data

dataListCopy = []
#determine if a character is printable ascii
for el in data:
    #if it is, then append it to the list so that it may be printed
    if int(hex(el),16) >= int(hex(32),16) and int(hex(el),16) <= int(hex(126),16):
    #if hex(el) >= 0x20 and hex(el) <= 0x7e:
        dataListCopy.append(chr(el))
    #else its not printable ascii, so append a period in it's place
    else:
        #print(hex(el))
        dataListCopy.append('.')

data = list(data)

dataListCopyHex = []
for el in data:
    dataListCopyHex.append(f'{el:x}'.rjust(2,'0'))

start = 0
end = 16
for i in range(len(dataListCopyHex)):
    l1 = ''
    l2 = ''
    if i % 16 == 0:
        prev = ''
        if len(dataListCopyHex) - i > 15:
            print('{:08x}'.format(i), end='  ')
            print(' '.join(dataListCopyHex[i:i+8]), end='  ')
            l1 = ' '.join(dataListCopyHex[i:i+8])
            print(' '.join(dataListCopyHex[i+8:i+16]),end='  ')
            l2 = ' '.join(dataListCopyHex[i+8:i+16])
            print('|' + ''.join(dataListCopy[i:i+16]) + '|')
            #print('HI')
        else:
            prev = '{:08x}'.format(i)
            length = len('{:08x}'.format(i) + '  ' + ' '.join(dataListCopyHex[i:i+8]) + ' '.join(dataListCopyHex[i+8:i+16]))
            length2 = len(dataListCopyHex[i:i+16])
            print('{:08x}'.format(i) + '  ' + ' '.join(dataListCopyHex[i:i+8]) + '  ' + ' '.join(dataListCopyHex[i+8:i+16]),end='')
            print('|'.rjust(59-length),end='')
            print(''.join(dataListCopy[i:i+16]) + '|')
            #print(''.join(dataListCopyHex[i:8:i+16]),end='  ')
            #print(''.join(dataListCopyHex)
            #print('BYE')
    if len(dataListCopy) - 1 == i:
        print('{:08x}'.format(i + 1), end='')
        
#if __name__ == "__main__":
    #main()
import sys

fd = open(sys.argv[1], "rb")

data = fd.read()

dataListCopy = []

for el in data:
    if hex(el) >= hex(32) and hex(el) <= hex(126):
        dataListCopy.append(chr(el))
    else:
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
        if len(dataListCopyHex) - i > 15:
            print('{:08x}'.format(i), end='  ')
            print(' '.join(dataListCopyHex[i:i+8]), end='  ')
            l1 = ' '.join(dataListCopyHex[i:i+8])
            print(' '.join(dataListCopyHex[i+8:i+15]),end='  ')
            l2 = ' '.join(dataListCopyHex[i+8:i+15])
            print('|' + ''.join(dataListCopy[i:i+16]) + '|')
        else:
            length = len('{:08x}'.format(i) + '  ' + ' '.join(dataListCopyHex[i:i+8]) + ' '.join(dataListCopyHex[i+8:i+15]))
            length2 = len(dataListCopyHex[i:i+16])
            print('{:08x}'.format(i) + '  ' + ' '.join(dataListCopyHex[i:i+8]) + ' '.join(dataListCopyHex[i+8:i+15]),end='')
            print('|'.rjust(58-length),end='')
            print(''.join(dataListCopy[i:i+16]) + '|')
            print('{:08x}'.format(i + length2))

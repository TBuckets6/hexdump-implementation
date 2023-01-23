import sys

fd = open(sys.argv[1], "rb")

#print(fd.read())

content = fd.read()

#print(content[0:16])
start = 0
end = 16

while True:
    print('{:08x}'.format(start), end='  ')
    leng = len(content[start:end])
    print(content[start:end].hex())
    if end > len(content):
        print('{:08x}'.format(start+leng), end='  ')
        break
    start = start + 16
    end = end + 16 
# content = fd.read(16).hex()

# print(content)

#content = fd.read(16)

#print(content)












# for count,byte in enumerate(content):
#     #print(hex(byte))
#     if count % 16 == 0:
#         print('{:08x}'.format(count), end='  ')
#         print(hex(byte)[0:16])
    # print(hex(byte)[2:],end=' ')
    # if count % 16 == 0 and count != 0:
    #     print('|')
    

#print(fd.tell()) specifices the offset

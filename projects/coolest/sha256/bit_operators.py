bits = [0,1]

for bit in bits:
    for bit2 in bits:
        print(bit,'&',bit2,':',bit & bit2)

for bit in bits:
    for bit2 in bits:
        print(bit,'|',bit2,':',bit | bit2)  

for bit in bits:
    for bit2 in bits:
        print(bit,'^',bit2,':',bit ^ bit2)  

for bit in bits:
    print('~',bit,~bit)

print(bin(0b000111 << 1))
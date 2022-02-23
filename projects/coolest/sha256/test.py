print(~0b0)
print(~0b1)
print(~0b0 & 1)
print(~0b1 & 1)
print(~156 & 255)
print(bin(~0b10101100 & 255))

print(bin(0b11111111 
        - 0b10101100))

import sys
print(sys.byteorder)
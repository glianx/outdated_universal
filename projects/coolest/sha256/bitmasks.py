#   10110101 
# & 00100000
# = 00100000

def get_bit(val,i):
    return val & (1 << i)

#   101 10101
# &   1
# =   1

def get_normalized_bit(val,i):
    return (val >> i) & 1

#    10000000
# or 00100000
# =  10100000

def set_bit(val,i):
    return val | (1 << i)

#     10000000      0   1
# xor 00100000      1   1 
# =   10100000      1   0

def toggle_bit(val,i):
    return val ^ (1 << i)

print(get_bit(0b10000000, 5))
print(get_bit(0b10110101, 5))

print(get_normalized_bit(0b10000000, 5))
print(get_normalized_bit(0b10110101, 5))

print(bin(set_bit(0b10000000, 5)))

print(bin(toggle_bit(0b10000000, 5)))
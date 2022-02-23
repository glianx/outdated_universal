# shift right     >>
# rotate right    rotr()
# xor             ^
# add             +

def rotr(n,k,len):
    return (n << len-k | n >> k) & 2**len-1

def sigma0(n,len):
    return rotr(n,7,len) ^ rotr(n,18,len) ^ n >> 3

def sigma1(n,len):
    return rotr(n,17,len) ^ rotr(n,19,len) ^ n >> 10

def sigma2(n,len):
    return rotr(n,2,len) ^ rotr(n,13,len) ^ rotr(n,22,len)

def sigma3(n,len):
    return rotr(n,6,len) ^ rotr(n,11,len) ^ rotr(n,25,len)

def ch(x,y,z):
    return (x & y) ^ ((2**32-1 -x) & z)

def maj(x,y,z):
    return (x & y) ^ (x & z) ^ (y & z)

def return_int_input(text):
    int_input = 0
    for i in range(len(text)):
        int_input += ord(text[i]) << 8 * (len(text) - i - 1)

    int_input <<= 1
    int_input += 1

    int_input <<= 512 * (8 * len(text) // 512 + 1) - 8 * len(text) - 1
    int_input += 8 * len(text)

    return int_input

def w(i): # i = 0 to 63
    return (int_input & (2**32-1 << (63-i) * 32)) >> (63-i) * 32

def block_64x32():
    global int_input
    for i in range(16,64):
        len_ = 32
        s0 = sigma0(w(i-15),len_)
        s1 = sigma1(w(i-2),len_)
        word = w(i-16) + s0 + w(i-7) + s1   &   2**32 - 1

        int_input += word << (63 - i) * 32
    return int_input

text = 'hello world'
int_input = return_int_input(text)
int_input <<= 2 ** 11 - len(bin(int_input)) + 2

block_64x32()
print(bin(int_input))
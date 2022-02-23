n = 0b11110101
len_ = 8
def rotl(n,k,len):
    return (n << k | n >> len-k) & 2**len-1

def rotr(n,k,len):
    return (n << len-k | n >> k) & 2**len-1
    
# 111 10101
# 10101 111
print(bin(rotl(n,3,len_)))

# 11110 101
# 101 11110
print(bin(rotr(n,3,len_)))


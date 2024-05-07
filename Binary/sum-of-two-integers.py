def get_sum(a, b):
    mask = 0xffffffff

    while (b & mask) > 0:
        carry = (a & b) << 1
        a = (a ^ b)
        b = carry
    
    return (a & mask) if b > 0 else a


a, b = 1, 10
print(get_sum(a, b))

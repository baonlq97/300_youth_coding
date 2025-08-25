a, b = map(str, input().split())
int_a = int(a, 2)
int_b = int(b, 2)
while int_b != 0:
    sum = int_a ^ int_b
    carry = (int_a & int_b) << 1
    int_a, int_b = sum, carry

print(format(sum, 'b'))
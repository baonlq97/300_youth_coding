a = int(input())
thousands_digit = a // 1000
hundreds_digit = (a // 100) % 10
tens_digit = (a // 10) % 10
ones_digit = a % 10
total_sum = thousands_digit + hundreds_digit + tens_digit + ones_digit

print(total_sum)
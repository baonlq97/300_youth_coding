a = int(input())
five = a // 5000
surplus = a % 5000
two = surplus // 2000
surplus = surplus % 2000
one = surplus // 1000
print("{} {} {}".format(five, two, one))
a = int(input())
low, high = 0.0, max(1.0, float(a))
eps = 1e-6
while high - low > eps:
    mid = (low + high) / 2
    if (mid * mid) <= a:
        low = mid
    else:
        high = mid
print(f"{low:.2f}")
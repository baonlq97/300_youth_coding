n = int(input())
hour_in_seconds = 60*60
min_in_seconds = 60
hours = n // hour_in_seconds
mins = (n % hour_in_seconds) // min_in_seconds
seconds = (n % hour_in_seconds) % min_in_seconds
print("{}:{}:{}".format(hours, mins, seconds))
total = int(input())
hundred, rem = divmod(total, 100)
fivty, rem = divmod(rem, 50)
ten, rem = divmod(rem, 10)
five, rem = divmod(rem, 5)
print(hundred + fivty + ten + five + rem)
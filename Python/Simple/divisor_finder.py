# Problem-2 (Easy)

n = int(input("Enter the number : "))
mn = int(input("Enter the minimum number of divisor : "))
mx = int(input("Enter the maximum number of divisor : "))


a = []

for i in range(mn,mx+1):
    if n%i==0:
        a.append(i)

for i in a:
    print(f"The divisors are {i}")
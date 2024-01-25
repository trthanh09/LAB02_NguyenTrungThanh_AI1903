#1 Enter integers m and n, where m < n
m = int(input("Enter integer m: "))
n = int(input("Enter integer n: "))
while m >= n:
    print("Error: m must be less than n. Enter m and n again.")
    m = int(input("Enter integer m: "))
    n = int(input("Enter integer n: "))

#2 Display all palindrome numbers in the range (m, n)
print(f"The palindrome numbers in the interval [{m}, {n}] is: ", end="")
for i in range(m, n+1):
    if str(i) == str(i)[::-1]:
        print(i, end=" ")
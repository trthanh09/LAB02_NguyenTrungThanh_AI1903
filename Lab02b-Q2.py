def find_prime_dividers(num):
    prime_dividers = []
    divisor = 2

    while num > 1:
        while num % divisor == 0:
            prime_dividers.append(divisor)
            num //= divisor
        divisor += 1

    return prime_dividers

def find_gcd(a, b):
    while b:
        a, b = b, a % b
    return a

def find_lcm(a, b):
    return abs(a * b) // find_gcd(a, b)

# Accept two integer numbers from the user
try:
    m = int(input("Enter the first integer number (m): "))
    n = int(input("Enter the second integer number (n): "))

    # Display common prime dividers
    common_prime_dividers = list(set(find_prime_dividers(m)) & set(find_prime_dividers(n)))
    print(f"Common Prime Dividers: {common_prime_dividers}")

    # Find and display GCD (Greatest Common Divider)
    gcd_result = find_gcd(m, n)
    print(f"GCD of {m} and {n}: {gcd_result}")

    # Find and display LCM (Least Common Multiple)
    lcm_result = find_lcm(m, n)
    print(f"LCM of {m} and {n}: {lcm_result}")

except ValueError:
    print("Invalid input. Please enter valid integer numbers.")
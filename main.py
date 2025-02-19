def modular_exponentiation(b, n, m):
    x = 1
    power = b % m

    for i in range(n.bit_length()):  # Loop through bits of n
        if (n >> i) & 1:  # Check if the i-th bit of n is 1
            x = (x * power) % m
        power = (power * power) % m  # Square power mod m

    return x

def main():
    b = int(input("Enter B: "))
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))

    if b <= 0 or n <= 0 or m <= 0:
        print("Error: All numbers must be positive and nonzero.")
        return

    print(modular_exponentiation(b, n, m))

main()

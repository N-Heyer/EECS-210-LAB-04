'''
Name:Nick Heyer 
KUID:3142337
LAB Session:Thursday 4:30pm
LAB Assignment: 04
Description: This program take in 3 ints to be put into a mod equation and 
gives the correct output making sure negative and zeros are not counted for
Collaborators: NONE
'''

def mod_expo(b, n, m):
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

    print(mod_expo(b, n, m))

main()

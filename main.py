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
    x = 1 # init to 1 
    power = b % m # base mod m

    for i in range(n.bit_length()):# loops thru bit of n
        if (n >> i) & 1: #checks the ith bit of n is 1 
            x = (x * power) % m  # mult by power and mod m
        power = (power * power) % m # sqaure the power and take mod m

    return x #returns result

def main(): #reads input from user
    b = int(input("Enter B: "))
    n = int(input("Enter n: "))
    m = int(input("Enter m: "))

    if b <= 0 or n <= 0 or m <= 0: # makes sure all inputs are positive and nonzero
        print("Error: All numbers must be positive and nonzero.") # prints error if negastive or zero
        return # stops func

    print(mod_expo(b, n, m)) # calls mod_expo to do the math and print the result

main()

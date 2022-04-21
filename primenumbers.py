currentnumber = 2
primesum = 0

def isprime(n):
    """Returns True if n is prime."""
    if n == 2:
        return True
    if n == 3:
        return True
    if n % 2 == 0:
        return False
    if n % 3 == 0:
        return False

    i = 5
    w = 2

    while i * i <= n:
        if n % i == 0:
            return False

        i += w
        w = 6 - w

    return True
for i in range(2,101):
    if(isprime(currentnumber)==True):
        primesum += currentnumber
        currentnumber+=1
    else:
        currentnumber+=1
print(primesum)
if(primesum % 2 == 0):
    print("This is a even number")
else:
    print("This is an odd number")
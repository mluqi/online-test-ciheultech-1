def ispalindrome(x):
    if x < 0:
        return False
    
    original_x = x

    reversed_x = 0
    while x > 0:
        reversed_x = reversed_x * 10 + x % 10
        x //= 10

    return original_x == reversed_x


x = 121
y = 123
z = 12321
ispalindrome(x)
print(ispalindrome(x))
print(ispalindrome(y))
print(ispalindrome(z))
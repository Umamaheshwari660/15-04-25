# task:Wap to check if each number in an list contains duplicate digits, returning true for duplicates and false for unique digits.
# Input: [202,89,112,88] Output:[true ,false ,true ,true]


# 3)Missing prime number .Input: [11, 3, 4, 5, 2, 6, 7, 19, 13] Output: 17

# 4) GCD code



# 1) Check for duplicate digits in each number in a list
def has_duplicate_digits(numbers):
    result = []
    for num in numbers:
        digits = str(num)
        result.append(len(set(digits)) < len(digits))
    return result

# Example usage
print(has_duplicate_digits([202, 89, 112, 88]))


# 2) Find the missing prime number in a sequence
def find_missing_prime(numbers):
    primes = [2, 3, 5, 7, 11, 13, 17, 19]
    for p in primes:
        if p not in numbers:
            return p

# Example usage
print(find_missing_prime([11, 3, 4, 5, 2, 6, 7, 19, 13]))


# 3) GCD (Greatest Common Divisor) of two numbers
def gcd(a, b):
    while b:
        a, b = b, a % b
    return a

# Example usage
print(gcd(48, 18))  

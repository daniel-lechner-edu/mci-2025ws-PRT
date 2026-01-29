# starke primzahlen mit gerader ziffernsumme
# definition: p ist starke primzahl wenn (p - prev_prime > next_prime - p) UND ziffernsumme gerade

def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return False
    return True

def next_prime(n):
    num = n + 1
    while not is_prime(num):
        num += 1
    return num

def prev_prime(n):
    num = n - 1
    while num > 1 and not is_prime(num):
        num -= 1
    return num if num > 1 else None

def is_strong_prime(n):
    if not is_prime(n):
        return False
    prev = prev_prime(n)
    if prev is None:
        return False
    next_p = next_prime(n)
    digit_sum = sum(int(digit) for digit in str(n))
    return (n - prev) > (next_p - n) and digit_sum % 2 == 0


def S(m, n):
    total = 0
    for num in range(m, n + 1):
        if(is_strong_prime(num)):
            print(f"Gefundene starke Primzahl: {num}")
            total += num
    return total

result = S(100, 300)
print(f"\nSumme: {result}")
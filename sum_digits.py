def sum_digits(n):
  if n < 10:
    return n
  else:
    last_digit = n % 10
    return last_digit + sum_digits(n // 10)

print(sum_digits(12), sum_digits(194))

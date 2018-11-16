def sum_to_one(n):
  if n == 1:
    return n

  print("Recursing with input: {0}".format(n))
  
  return sum_to_one(n-1) + n


print(sum_to_one(8))

def is_palindrome(my_string):
  if len(my_string) <= 1:
    return True
  if my_string[0] != my_string[-1]:
    return False
  return is_palindrome(my_string[1:-1])


# test cases
print(is_palindrome("abba") == True)
print(is_palindrome("abcba") == True)
print(is_palindrome("") == True)
print(is_palindrome("abcd") == False)

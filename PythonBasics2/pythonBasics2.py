# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Function that returns which multiple of three occurs the most 
# a string

def count_threes(n):
  str_n = str(n)
  my_dict = {'3' : 0, '6' : 0, '9' : 0}
  for i in range(0, len(str_n)):
    if str_n[i] == "3":
        my_dict['3'] = my_dict.get('3', 0) + 1
    if str_n[i] == "6":
        my_dict['6'] = my_dict.get('6', 0) + 1
    if str_n[i] == "9":
        my_dict['9'] = my_dict.get('9', 0) + 1
  max_key = max(my_dict, key = my_dict. get)
  return int(max_key)


# Part B. longest_consecutive_repeating_char
# Function that returns the most repeated character in a given string
def longest_consecutive_repeating_char(s):
    my_dict = {}

    for i in s:
        my_dict[i] = my_dict.get(i, 0) + 1
    max_value = max(my_dict.values())
    max_keys = [j for j, c in my_dict.items() if c == max_value]
    return max_keys



# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  rev = ''.join(reversed(s))
  rev = rev.replace(" ", "")
  s = s.replace(" ", "")
  if (s.lower() == rev.lower()):
    return True
  return False
  return

# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.


# Part A. count_threes
# Define a function count_threes(n) that takes an int and
# returns the number of multiples of 3 in the range from 0
# to n (including n).

def count_threes(n):
  count = 0
  x = 0
  for x in range(0,n):
      if ( 0 < (x + 3) <= n):
          if ((x+3)%3 == 0):
            count += 1
  x += 3
  return count


# Part B. longest_consecutive_repeating_char
# Define a function longest_consecutive_repeating_char(s) that takes
# a string s and returns the character that has the longest consecutive repeat.
def longest_consecutive_repeating_char(s):
  count = 0
  highest_count = 0
  most_repeated_char = ""
  currChar = " "
  prevChar = " "
  for x in range(0, len(s)):
    currChar = s[x]
    if currChar == prevChar:
      count = count + 1
    if count > highest_count:
      highest_count = count
      most_repeated_char = currChar
    prevChar = currChar
    x += 1
  return most_repeated_char


# Part C. is_palindrome
# Define a function is_palindrome(s) that takes a string s
# and returns whether or not that string is a palindrome.
# A palindrome is a string that reads the same backwards and
# forwards. Treat capital letters the same as lowercase ones
# and ignore spaces (i.e. case insensitive).
def is_palindrome(s):
  # YOUR CODE HERE

  return

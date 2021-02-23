# Python Activity
#
# Fill in the code for the functions below.
# The starter code for each function includes a 'return'
# which is just a placeholder for your code. Make sure to add what is going to be returned.

# Part A. count_char
# Define a function count_char(s, char) that takes a string and a character
# and returns the number of times the given character appears in the string
def count_char(s, char):
  numTimes = 0
  for element in s:
      if element == char:
         numTimes = numTimes + 1
  return numTimes
# Part B. is_power_of
# Define a function is_power_of(i,j) that takes 2 ints i and j
# and checks if i is a power of j or not
# the function should return True indicating that i is a power of j
# otherwise return False
def is_power_of(i,j):
  power = 1
  if j == 0 and i == 0:
    return True
  if j < power:
     r = range(j,power)
     for n in r:
        val = i**(power)
        if val == j:
            return (val == j)
        power+=1

  while power < j:
    power = power * i

  return (power == j)

# Part C. longest_word
# Define a function longest_word(s) that takes a string s
# where s is a sentence made up of words separated by a single space " "
# and returns the longest word in this sentence
# if 2 or more words are tied as longest then return the one that occurs LAST in the sentence
# if s is an empty string return an empty string
def longest_word(s):
    max_word = " "
    max_length = 0
    s_arr = s.split(" ")
    for element in s_arr:
      curr_word = element
      curr_length = len(element)
      if curr_length >= max_length:
        max_word = curr_word
        max_length = curr_length
    return max_word

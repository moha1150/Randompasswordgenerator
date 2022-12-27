import random

# A function to shuffle all the characters of a string
def shuffle(string):
  temp_list = list(string)
  random.shuffle(temp_list)
  return ''.join(temp_list)

# Main program starts here
uppercase_letter_1 = chr(random.randint(65, 90))  # Generate a random uppercase letter (based on ASCII code)
uppercase_letter_2 = chr(random.randint(65, 90))  # Generate a random uppercase letter (based on ASCII code)
lowercase_letter_1 = chr(random.randint(97, 122))  # Generate a random lowercase letter (based on ASCII code)
lowercase_letter_2 = chr(random.randint(97, 122))  # Generate a random lowercase letter (based on ASCII code)
digit_1 = chr(random.randint(48, 57))  # Generate a random digit (based on ASCII code)
digit_2 = chr(random.randint(48, 57))  # Generate a random digit (based on ASCII code)
symbol_1 = chr(random.randint(33, 47))  # Generate a random symbol (based on ASCII code)
symbol_2 = chr(random.randint(33, 47))  # Generate a random symbol (based on ASCII code)

# Generate password using all the characters, in random order
password = uppercase_letter_1 + uppercase_letter_2 + lowercase_letter_1 + lowercase_letter_2 + digit_1 + digit_2 + symbol_1 + symbol_2
password += uppercase_letter_1 + uppercase_letter_2 + lowercase_letter_1 + lowercase_letter_2 + digit_1 + digit_2 + symbol_1 + symbol_2
password = shuffle(password)

# Output
print(password)

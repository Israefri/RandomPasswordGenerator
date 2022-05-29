import random
import string
print(string.printable)

# The char set that will be used in the generated password
char_seq = "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!#$%&'()*+,-./:;<=>?@[\]^_`{|}~"
print("Enter the required length of the password ranging from 8 to 16: ")
length = int(input())
if length >= 8 and length <= 16:
    password = ''

    # Starting to generate a password char by char until get to the wanted length
    for len in range(length):
        random_char = random.choice(char_seq)
        password += random_char

    # print(password)
    list_pass = list(password)
    random.shuffle(list_pass)
    final_password = ''.join(list_pass)
    print(final_password)
# If the user inserted number lower than 8 or higher than 16
else:
    print("Enter a suitable range")

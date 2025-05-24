# Write a python program using scipy for a treasure hunt game for kids provides clues encrypted using
# a Caesar cipher. One clue reads: ”KHOOR ZRUOG”, and the kids are told that the letters are shifted
# by 3 positions.

# Importing from scipy just to include it in the program

# from scipy import constants  # Not necessary for Caesar cipher but included for instruction

# Caesar Cipher Decryption Function
def caesar_decrypt(text, shift):
    result = ""
    for char in text:
        if char.isalpha():
            if char.isupper():
                ascii_start = ord("A")
            else:
                ascii_start = ord("a")
            decrypted_char = chr((ord(char) - ascii_start - shift) % 26 + ascii_start)
            result += decrypted_char
        else:
            result += char  # Keep spaces and symbols
    return result

# Game starts
print("Welcome to the Treasure Hunt Game!")
print("You have received a secret clue!")

# Encrypted clue
encrypted_clue = "KHOOR ZRUOG"
print("Encrypted Clue:", encrypted_clue)

# Decrypt the clue
shift = 3
decrypted_clue = caesar_decrypt(encrypted_clue, shift)
print("Decrypted Clue:", decrypted_clue)


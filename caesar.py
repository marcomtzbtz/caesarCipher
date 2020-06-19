import sys

if len(sys.argv) != 2:
    print("Usage: python caesar.py k")
    exit(1)
else:
    k = int(sys.argv[1])


def caesar (text, k):

    cipher = ""
    for letter in text:
        if letter.isalpha():
            if letter.isupper():
                cipher += chr(( ord(letter) + k - 65 ) % 26 + 65)
            else:
                cipher += chr(( ord(letter) + k - 97 ) % 26 + 97)
        else:
            cipher += letter
    return cipher


text = list(raw_input("plaintext: "))
ciphertext = caesar(text, k)
print("ciphertext: {}".format(ciphertext))
print("\n")
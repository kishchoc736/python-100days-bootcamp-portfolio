alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(alphabet[-1])
print(alphabet[-3])


direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n").lower()
text = input("Type your message:\n").lower()
shift = int(input("Type the shift number:\n"))


# TODO-1: Create a function called 'decrypt()' that takes 'original_text' and 'shift_amount' as inputs.
def decrypt(original_text, shift_amount):
    decrypted_text = ""
# TODO-2: Inside the 'decrypt()' function, shift each letter of the 'original_text' *backwards* in the alphabet
#  by the shift amount and print the decrypted text.
    for letter in original_text:
        current_position = alphabet.index(letter)
        new_position = current_position - shift_amount
        new_position %= len(alphabet)
        decrypted_text += alphabet[new_position]
    print(f"Here is the encoded result: {decrypted_text}")
# TODO-3: Combine the 'encrypt()' and 'decrypt()' functions into one function called 'caesar()'.
#  Use the value of the user chosen 'direction' variable to determine which functionality to use.

def caesar(original_text, shift_amount, encode_or_decode):
    decrypted_text = ""
    for letter in original_text:
        current_position = alphabet.index(letter)
        if encode_or_decode == "decode":
            new_position = current_position - shift_amount
        elif encode_or_decode == "encode":
            new_position = alphabet.index(letter) + shift_amount
        new_position %= len(alphabet)
        decrypted_text += alphabet[new_position]
    print(f"Here is the {encode_or_decode}d result: {decrypted_text}")








def encrypt(original_text, shift_amount):
    cipher_text = ""
    for letter in original_text:
        shifted_position = alphabet.index(letter) + shift_amount
        shifted_position %= len(alphabet)
        cipher_text += alphabet[shifted_position]
    print(f"Here is the encoded result: {cipher_text}")


# encrypt(original_text=text, shift_amount=shift)
# decrypt(original_text=text, shift_amount= shift)

caesar(original_text= text, shift_amount= shift, encode_or_decode= direction)


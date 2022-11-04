from art import logo

alphabet = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l',
            'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

print(logo)
running = True

# TODO-1: Create a function called 'encrypt' that takes the 'text' and 'shift' as inputs.


# def encrypt(text, shift):
#     encoded_string = ""
#     for i in range(len(text)):
#         if text[i] not in alphabet:
#             encoded_string += text[i]
#             continue
#         else:
#             shifted_index = 0
#             unshifted_index = ord(text[i]) - ord("a")
#             if unshifted_index + shift > 25:
#                 shifted_index = unshifted_index + shift - 26
#             else:
#                 shifted_index = unshifted_index + shift
#         encoded_string += alphabet[shifted_index]
#     print(encoded_string)


# def decrypt(text, shift):
#     decoded_string = ""
#     for i in range(len(text)):
#         if text[i] not in alphabet:
#             decoded_string += text[i]
#             continue
#         else:
#             shifted_index = 0
#             unshifted_index = ord(text[i]) - ord("a")
#             if unshifted_index - shift < 0:
#                 shifted_index = unshifted_index + 26 - shift
#             else:
#                 shifted_index = unshifted_index - shift
#         decoded_string += alphabet[shifted_index]
#     print(decoded_string)

# # TODO-2: Inside the 'encrypt' function, shift each letter of the 'text' forwards in the alphabet by the shift amount and print the encrypted text.
# # e.g.
# #plain_text = "hello"
# #shift = 5
# #cipher_text = "mjqqt"
# # print output: "The encoded text is mjqqt"

# # HINT: How do you get the index of an item in a list:
# # https://stackoverflow.com/questions/176918/finding-the-index-of-an-item-in-a-list

# # 🐛Bug alert: What happens if you try to encode the word 'civilization'?🐛


# # TODO-3: Call the encrypt function and pass in the user inputs. You should be able to test the code and encrypt a message.
# if direction == "encode":
#     encrypt(text, shift)
# elif direction == "decode":
#     decrypt(text, shift)
# else:
#     print("Invalid choice. Must choose encode or decode!")


# Combining functions

def casear(text, shift, direction):
    der = 1
    shifted_index = 0
    if direction == "decode":
        der = -1
    final_string = ""
    for i in range(len(text)):
        if text[i] not in alphabet:
            final_string += text[i]
            continue
        else:
            unshifted_index = ord(text[i]) - ord("a")
            if (unshifted_index + shift > 25 and direction == "encode") or (unshifted_index + (der * shift) < 0 and direction == "decode"):
                shifted_index = unshifted_index + (shift * der) - (der * 26)
            else:
                shifted_index = unshifted_index + (shift * der)
        final_string += alphabet[shifted_index]
    print(f"Your {direction}d text is: {final_string}")


while running:
    direction = input("Type 'encode' to encrypt, type 'decode' to decrypt:\n")
    text = input("Type your message:\n").lower()
    shift = int(input("Type the shift number:\n"))
    if shift > 25:
        shift = shift % 25
    casear(text, shift, direction)
    choice = input(
        "Type 'yes' if you want to go again. Otherwise type 'no'\n").lower()
    if choice == "no":
        running = False
print("Goodbye")

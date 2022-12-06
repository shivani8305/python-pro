alphabets = ["a", "b", "c", "d", "e", "f", "g", "h", "j", "k", "l", "m", "n", "o",
             "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z","a", "b", "c", "d", "e", "f", "g", "h", "j", "k", "l", "m", "n", "o",
             "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]



def ceaser(plain_text, shift_amount):
    cipher_text = ""
    for letter in plain_text:
        
        if direction=="encode":
            if letter in alphabets:
                position = alphabets.index(letter)
                new_position = position + shift
                new_letter = alphabets[new_position]
                cipher_text+=new_letter
            else:
                cipher_text+=letter
        elif direction=="decode":
            if letter in alphabets:
                position = alphabets.index(letter)
                new_position = position - shift
                new_letter = alphabets[new_position]
                cipher_text+=new_letter
            else:
                cipher_text+=letter
    print(f"The {direction}d text is {cipher_text}")
    
should_continue = True
while should_continue:
    direction = input("Type 'encode' to encrypt and 'decode' to decrypt:\n")
    text = input("Enter your message:\n").lower()
    shift = int(input("Type the shift number:\n"))    
    shift = shift%26    
    ceaser(text, shift)
    new = input(print("Type 'yes' if you want to continue and 'no' to stop\n"))
    if new=="no":
        should_continue = False
        print("Goodbye")
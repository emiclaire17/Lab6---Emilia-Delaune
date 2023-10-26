# Emilia Delaune
def encode(password):
    # this function adds three to each digit in the password to encode it
    new_password = ""
    for char in password:
        if int(char) < 7:
            char = int(char) + 3
            new_password = new_password + str(char)
        # for numbers greater than 7, it restarts at 0 to avoid double digits
        elif int(char) == 7:
            char = 0
            new_password = new_password + str(char)
        elif int(char) == 8:
            char = 1
            new_password = new_password + str(char)
        else:
            char = 2
            new_password = new_password + str(char)
    return new_password


def decode_password(password):
    # this function decodes a password by subtracting 3 from each digit
    decoded_password = ""
    for num in password:
        if int(num) == 0:
            num = 7
            decoded_password += str(num)
        elif int(num) == 1:
            num = 8
            decoded_password += str(num)
        elif int(num) == 2:
            num = 9
            decoded_password += str(num)
        else:
            decoded_password += str(int(num) - 3)
    return decoded_password



def main():
    # function runs until the user quits using a loop
    active = True
    while active == True:
        print('Menu')
        print('-------------')
        print('1. Encode\n2. Decode\n3. Quit')
        print()
        choice = int(input("Please enter an option: "))
        if choice == 1:
            password = input("Please enter your password to encode: ")
            result = encode(password)
            print("Your password has been encoded and stored!")
        if choice == 2:
            original = decode_password(result)
            print(f"The encoded password is {result}, and the original password is {original}")
        if choice == 3:
            active = False



if __name__== '__main__':
    main()
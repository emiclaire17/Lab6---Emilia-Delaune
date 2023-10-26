def encode(password):
    new_password = ""
    for char in password:
        if int(char) < 7:
            char = int(char) + 3
            new_password = new_password + str(char)
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
        elif int(num) > 2:
            decoded_password += str(num)
    return decoded_password



def main():
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
            original = decode(result)
            print(f"The encoded password is {result}, and the original password is {original}")
        if choice == 3:
            active = False



if __name__== '__main__':
    main()
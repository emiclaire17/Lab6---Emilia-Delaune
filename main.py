# Emilia Delaune
def encode(password):
    # this function adds three to each number in the original password
    new_password = ""
    for char in password:
        if int(char) < 7:
            char = int(char) + 3
            new_password = new_password + str(char)
        elif int(char) == 7:
            # when a number hits a digit greater than 7, the count starts back at 0 to ensure no double digits
            char = 0
            new_password = new_password + str(char)
        elif int(char) == 8:
            char = 1
            new_password = new_password + str(char)
        else:
            char = 2
            new_password = new_password + str(char)
    return new_password
def decode(password):
    # this function decodes the previous encoded password by subtracting 3 from each digit
def main():
    active = True
    # allows the menu to print over and over until the user quits
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
def encoding(password):
    encoded_password = ''
    for num in password:
        if num.isdigit():
            encoded_num = (int(num) + 3) % 10
            encoded_password += str(encoded_num)
    return encoded_password



def decoding(password):
    pass


def main():
    while True:
        print('Menu'
        '\n-------------'
        '\n1. Encode'
        '\n2. Decode'
        '\n3. Quit')

        choice = input('Please enter an option: ')

        if choice == '1':
            og_password = input('Please enter your password to encode: ')
            encoded = encoding(og_password)
            #print(encoded)
            print('Your password has been encoded and stored!')

        elif choice == '2':
            decoded = decoding(encoded)
            pass

        elif choice == '3':
            break


if __name__ == '__main__':
    main()

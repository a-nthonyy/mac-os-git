def encoding(password):
    encoded_password = ''
    for num in password:
        if num.isdigit():
            encoded_num = (int(num) + 3) % 10
            encoded_password += str(encoded_num)
    return encoded_password

def decoding(encoded_password):
    decoded_password = ''
    for num in encoded_password:
        decoded_num = (int(num) - 3) % 10  # wrap around subtraction for digits
        decoded_password += str(decoded_num)
    return decoded_password

def main():
    encoded = None
    while True:
        print('Menu'
              '\n-------------'
              '\n1. Encode'
              '\n2. Decode'
              '\n3. Quit')
        choice = input('Please enter an option: ')

        if choice == '1':
            og_password = input('Please enter your password to encode ')
            if len(og_password) == 8 and og_password.isdigit():
                # added len to equal 8
                encoded = encoding(og_password)
                print('Your password has been encoded and stored!')
            else:
                print('Invalid input.')
        elif choice == '2':
            if encoded:
                decoded = decoding(encoded)
                print(f'The encoded password is {encoded}, and the original password is {decoded}.')
            else:
                print('No password has been encoded yet.')
        elif choice == '3':
            break
        else:
            print('Invalid option. Please try again.')

if __name__ == '__main__':
    main()

# Converts numbers 1-10 to roman numerals
# Elliot Schaefer 3-14-23

if __name__ == '__main__':
    while True:
        while True:
            # Get user input
            user_number = input('Please enter an integer between 1 and 10: ')
            if user_number == 'exit':
                quit()
            else:
                try:
                    user_number = int(user_number)
                    # Check if 'user_number' is between 1 and 10
                    if 1 <= user_number <= 10:
                        break
                    else:
                        print('Try entering a number between 1 and 10.')
                except ValueError:  # In case 'user_number' isn't actually a number
                    print('Try entering a number between 1 and 10.')

        # Find and print user's numeral
        print('Your numeral is: ', end='')
        match user_number:
            case 1:
                print('I')
            case 2:
                print('II')
            case 3:
                print('III')
            case 4:
                print('IV')
            case 5:
                print('VI')
            case 6:
                print('VII')
            case 7:
                print('VII')
            case 8:
                print('VIII')
            case 9:
                print('IX')
            case 10:
                print('X')

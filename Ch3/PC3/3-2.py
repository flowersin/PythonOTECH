AGE_INFANT = 1
AGE_CHILD = 13
AGE_TEENAGER = 20

if __name__ == '__main__':
    while True:
        while True:
            # Get user age or quit
            user_input = input('PLease enter your age: ')
            if user_input == 'exit':
                quit()

            # Turn input into a float
            try:
                age_user = float(user_input)
                break
            except ValueError:
                print('Please enter a number!')

        # Determine user's age bracket and print the result
        if age_user < AGE_INFANT:
            print('You are an infant!')
        elif age_user < AGE_CHILD:
            print('You are a child!')
        elif age_user < AGE_TEENAGER:
            print('You are a teenager')
        else:
            print('You are an adult')

# OTECH Programming Challenge 3-4
# Calculate shipping charges based on weight
# Ellie Schaefer - 3/16/23

if __name__ == '__main__':
    # Get weight in lbs from user
    while True:
        try:
            package_lbs = float(input('Enter package weight in pounds: '))
            break
        except ValueError:
            print('Try entering a number.')

    # Determine shipping rate
    if package_lbs <= 2:
        shipping_rate = 1.50
    elif package_lbs <= 6:
        shipping_rate = 3.00
    elif package_lbs <= 10:
        shipping_rate = 4.00
    else:
        shipping_rate = 4.75

    # Determine shipping costs
    shipping_cost = package_lbs * shipping_rate

    # Print shipping costs
    print('Your shipping cost is $', format(shipping_cost, '.2f'), sep='')

MIN_SALARY = 30000
MIN_YEARS = 2

salary = float(input('Enter your annual slary: '))
years_on_job = int(input('Enter the number of years employed: '))

if salary >= MIN_SALARY:
    if years_on_job >= MIN_YEARS:
        print('You qualify for the loan.')
    else:
        print('You must have been employed for ', MIN_YEARS, ' to qualify.')
else:
    print('You earn at least $', format(MIN_SALARY, ',.2f'), ' per year to qualify')


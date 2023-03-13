MIN_SALARY = 30000
MIN_YEARS = 2

salary = float(input('Enter your annual slary: '))
years_on_job = int(input('Enter the number of years employed: '))

if salary >= MIN_SALARY and years_on_job >= MIN_YEARS:
    print('You qualify for the loan.')
else:
    print('You do not qualify for the loan.')

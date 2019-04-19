'''
Take in the following three values from the user:
    - investment amount
    - interest rate in percentage
    - number of years to invest

Print the future values to the console.

'''
invest_amount = input("Please enter the amount to be invested : ")
invest_amount = int(invest_amount)
rate_of_interest = input("Please specify the interest rate in percentage : ")
rate_of_interest = float(rate_of_interest)
years = input("Number of years to invest : ")
years = int(years)
r = rate_of_interest / 100
Amount = invest_amount + (invest_amount * r * years)
print(Amount)

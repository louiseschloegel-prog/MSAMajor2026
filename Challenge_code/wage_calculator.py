
# The two input numbers are not necessarily integers. For example, the user can enter values like 35.5 for hours worked or 17.85 for hourly wage.
def get_positive_hours_daily():
    while (True):
        # Ask the user to input from the keyboard for two inputs, one is the hours worked daily and the other is the hourly wage. Multiplying hours worked daily and hourly wage will give you the wages earned in a day.
        try:
            user_hour_daily = float(input("Enter the number of hours worked daily: "))
            # the user cannot work more than 24 hours in a day
            if user_hour_daily > 24 or user_hour_daily <= 0:
                print("ERROR: Please enter a number greater than 0 and less than 24.\n")
                continue
            break
        except:
            print("ERROR: Please eneter a number.\n")
            continue
    return user_hour_daily

def get_positive_wage():
    while (True):
        try:
            user_hourly_wage = float(input("Enter the hourly wage: "))
            if user_hourly_wage <=0:
                print("ERROR: Please eneter a number greater than 0.\n")
                continue
            break
        except:
            print("ERROR: Please enter a number.\n")
            continue
    return user_hourly_wage



def main():
    # Calculate the yearly wage given the two inputs
    #daily hours worked
    user_hours = get_positive_hours_daily()
    #wage per hour
    user_hourly_wage = get_positive_wage()
    #find wage before taxes
    wage_before_taxes = user_hours * user_hourly_wage * 350
    tax_amount = 0.12 * wage_before_taxes 
    wage_after_taxes = wage_before_taxes - tax_amount
    print("Pay Advice\n---------------")
    print(f"Hours Worked: {user_hours}")
    print(f"Hourly Wage: ${user_hourly_wage}")
    print(f"Wages Before Taxes: ${wage_before_taxes: .2f}")
    print(f"Tax Amount: ${tax_amount: .2f}")
    print(f"Annual Wage After Taxes: ${wage_after_taxes: .2f}")



main()


        



# Note that the working hours is daily. Assume the user works 350 days per year and the same amount of hours every day.
# 12% will be deducted from yearly earnings for taxes
# Print the a Pay Advice containing:
# hours worked
# hourly wage
# wages before taxes
# tax amount
# annual wages after taxes
# money values should be printed with a $ sign and all numbers should be rounded to 2 decimal places
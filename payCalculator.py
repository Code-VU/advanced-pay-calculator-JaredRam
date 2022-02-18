def calculatePay():

    def compute_pay(hours, rate):
        try:
            hours = float(hours)
            rate = float(rate)
            if hours > 40.0:
                pay = (rate * 40) + ((hours - 40) * (rate * 1.5))
            else:
                pay = rate * hours
            
            print("Pay: ", pay)

        except:
            print('Error, please enter numeric input')
    
    # This first line is provided for you
    hours = input("Enter Hours: ")
    try:
        hours = int(hours)
    except:
        print('Error, please enter numeric input')
        quit()

    rate = input("Enter Rate: ")
    try:
        rate = int(rate)
    except:
        print('Error, please enter numeric input')
        quit()
    
    compute_pay(hours, rate)
    
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
calculatePay()
def calculatePay():
    
    # This first line is provided for you
    hrs = input("Enter Hours:")
    rate = input("Enter Rate: ")

    
    try:
        hrs = float(hrs)
        rate = float(rate)
        if hrs > 40.0:
            pay = (rate * 40) + ((hrs - 40) * (rate * 1.5))
        else:
            pay = rate * hrs
        
        print("Pay: ", pay)

    except:
        print('Error, please enter numeric input\n')
    
    # end assignment

## if you want to test locally before you try to sync
## uncomment calculatePay() and run > python payCalculator.py
## ***IMPORTANT*** please recomment before you submit/sync your assignment.
## OR YOUR TEST WILL NOT RUN
## calculatePay()
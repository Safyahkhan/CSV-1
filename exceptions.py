payrate = 10.00
paycheck = 0

while True:
    try:
        answer = float(input("How many hours did you work?"))
        paycheck = answer * payrate
        print(f"Your paycheck is ${paycheck:,.2f}")
        break

    except ValueError as err: #Ask ValueError as err
        print (f"There was an error. the error code is: {err}") #I can comment it out and just give pass command to it, it instead of giving out a command you give it pass and it wont print anything

        
print("It's done")
    

    
    




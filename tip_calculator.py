# tip_calculator.py

# TODO: Create a function named calculate_tip
# try:  #DO NOT MODIFY
# worked on in pods 
def tip_calculator():
    total_cost = float(input("The cost of the meal (without tax)"))
    num_people = int(input("How many people"))
    tip_percentage = float(input("The tip percentage"))

    # TODO:
        # Get these user inputs x
        # total_cost (float): The cost of the meal (without tax) x
        # num_people (int): The cost of the meal (without tax) x
        # tip_percentage (float): The tip percentage x

    
    # TODO:
        # Calculate the total bill including tip and sales tax (10%). x
        # Convert to float: The total bill (including tip and sales tax).x
    sales_tax = 0.1
    tip = total_cost * (tip_percentage / 100)
    total_bill = (total_cost * 0.1) + tip + total_cost
    # NOTE: Calculate the tip and tax separately. x
     
    # TODO: 
        # Calculate how much each person should pay.x
        # Convert to float: The amount each person should pay. x  
    split_amount = total_bill / num_people
    # TODO:
        # Using an f-string, print two different statements 
        # Total bill: $0.00
        # Each person should pay: $0.00
    print(f"Total bill: ${total_bill:.2f}\nEach person should pay: ${split_amount:.2f}")
    
    # NOTE: The amounts are displayed with 2 decimals only
    # except: # TODO: modify this except to include a Built-in Exception
        # TODO: Print an statement telling the user their input is invalid 
    # print("input is invalid")
    
if __name__ == "__main__": # DO NOT MODIFY
    tip_calculator() # DO NOT MODIFY

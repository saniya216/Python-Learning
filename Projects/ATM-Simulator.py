# ATM Simulator

# Step 1: Set PIN and balance
pin = 1234
balance = 5000

# Step 2: Ask user for PIN
user_pin = int(input("Enter your PIN: "))

# Step 3: Check PIN
if user_pin == pin:

    print("PIN Correct")

    # Step 4: Display ATM menu
    print("========== ATM ==========")
    print("1. Check Balance")
    print("2. Withdraw")
    print("3. Deposit")

    # Step 5: Ask user for choice
    choice = int(input("Enter your choice: "))

    # Step 6: Check Balance
    if choice == 1:
        print("Your Balance is:", balance)

    # Step 7: Withdraw
    elif choice == 2:
        amount = float(input("Enter withdrawal amount: "))

        if amount <= balance:
            balance = balance - amount
            print("Withdrawal Successful")
            print("Remaining Balance:", balance)

        else:
            print("Insufficient Balance")

    # Step 8: Deposit
    elif choice == 3:
        amount = float(input("Enter deposit amount: "))

        balance = balance + amount

        print("Deposit Successful")
        print("Updated Balance:", balance)

    # Step 9: Invalid choice
    else:
        print("Invalid Choice")

# Step 10: Incorrect PIN
else:
    print("Incorrect PIN")
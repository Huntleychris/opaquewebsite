def calculate_amortization_schedule(principal, annual_interest_rate, loan_term_years, extra_principal_payments):
    monthly_interest_rate = annual_interest_rate / 12 / 100
    total_payments = loan_term_years * 12
    
    # Calculate monthly payment without extra payment
    monthly_payment = (principal * monthly_interest_rate) / (1 - (1 + monthly_interest_rate) ** -total_payments)
    
    # Initialize variables
    remaining_balance = principal
    total_paid = 0
    
    # Amortization schedule
    amortization_schedule = []
    for month in range(1, total_payments + 1):
        interest_payment = remaining_balance * monthly_interest_rate
        total_payment = monthly_payment + extra_principal_payments[month - 1]
        principal_payment = total_payment - interest_payment
        
        # Ensure that principal payment doesn't exceed remaining balance
        principal_payment = min(principal_payment, remaining_balance)
        
        remaining_balance -= principal_payment
        total_paid += total_payment
        
        amortization_schedule.append((month, total_payment, interest_payment, principal_payment, remaining_balance))
        
        # Check if the loan is paid off
        if remaining_balance <= 0:
            break
    
    return amortization_schedule, total_paid

# Input parameters
principal_amount = 65000
annual_interest_rate = 12.95
loan_term_years = 5
extra_principal_payments = [2000] * (loan_term_years * 12)  # Example: $500 extra principal payment every month

# Calculate amortization schedule
amortization_schedule, total_paid = calculate_amortization_schedule(
    principal_amount, annual_interest_rate, loan_term_years, extra_principal_payments)

# Print results
print("Total Paid: $", round(total_paid, 2))

# Optionally print amortization schedule
print("\nAmortization Schedule:")
print("Month | Total Payment | Interest Payment | Principal Payment | Remaining Balance")
for entry in amortization_schedule:
    print("{:5} | ${:13,.2f} | ${:15,.2f} | ${:16,.2f} | ${:16,.2f}".format(*entry))

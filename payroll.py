## The program prints the payroll statement.

#input datacls
name = input("Enter Employee's name:")
hours = float(input("Enter Number of hours worked in a week:"))
Hpay_rate = float(input("Enter Hourly pay rate($):"))
Ftax_rate = float(input("Enter Federal tax withholding rate(eg.0.2 for 20%):"))
Stax_rate = float(input(("Enter State tax withholding rate(eg.0.09 for 9%):")))

Gross_pay = hours * Hpay_rate

# Deductions

F_withhold = Ftax_rate * Gross_pay
S_withhold = Stax_rate * Gross_pay
T_deductions = F_withhold + S_withhold

Net_pay = Gross_pay-T_deductions

# Payroll Statement
print("\nEmployee name:", name)
print("Hours worked:", hours)
print("Pay rate: ${:.2f}".format(Hpay_rate))
print("Gross Pay: ${:.2f}".format(Gross_pay))
print("Deductions:")
print("\t", "Federal withholding({:.2%}) : ${:.2f}".format(Ftax_rate,F_withhold))
print("\t", "State withholding({:.2%}) : ${:.2f}".format(Stax_rate,S_withhold))
print("\t", "Total Deductions: ${:.2f}".format(T_deductions))
print("Net pay: ${:.2f}.".format(Net_pay))



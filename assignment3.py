P = int(input("Enter value for P: "))
R = int(input("Enter value for R: "))
T= int(input("Enter value for T: "))

compound_interest=P*(1+R/100)**T-P

print("compound_interest =", compound_interest)

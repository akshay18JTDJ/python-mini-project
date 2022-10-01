from interest import CompoundInterest as ci
import auth

auth.authenticate()

principal = int(input("Enter the principal amount: "))
ROI = float(input("Enter the interest rate: "))
term = int(input("Enter the no. of years: "))
freq = int(input("No. of times the interest is compounded anually: "))

a = ci(principal,ROI,term,freq)   #ci(Principal, rate of interest, no. of years, no. of times the interest is compounded anually)
print("The compound interest for {} years with ROI {}% is {}".format(term,ROI,a))
name=input("Enter your name: ")
age=int(input('Enter your age:'))
while True:
    gender=input('Enter M for male and F for Female:').lower()
    if gender not in 'm f':
        continue
    else:
        break

if(age>=65 or gender.startswith('f')):
    tax='Nile'
if(age<=65 and gender.startswith('m')):
    tax_amt=int(input('Enter your Taxable Income: '))
    if tax_amt<0 or tax_amt in range(0,16001):
        tax=0
    elif tax_amt in range(160001,500001):
        tax=(tax_amt-160000)*0.1
    elif tax_amt in range(500001,800001):
        tax=((tax_amt-500000)*0.2)+34000
    elif(tax_amt>800000):
        tax=((tax_amt-160000)*0.3)+94000
print('Tax to be paid',tax)
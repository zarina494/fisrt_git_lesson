# find digits of number
number=int(input())
hund=number//100  #find hundreds
print(hund)
tens=number//10%10    #find tens
print(tens)
digits=number%100%10     #find digit
print(digits)
print(hund+tens+digits)

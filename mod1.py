from forex_python.converter import CurrencyRates

currency=CurrencyRates()

amount=int(input("Enter the Amount"))

frm_curr=input("From currency: ").upper()
to_curr=input("To currency: ").upper()

print(frm_curr,"TO",to_curr)

result=currency.convert(frm_curr,to_curr,amount)

print("Conversion Amount:",result)
print("Conversion Amount:",result)
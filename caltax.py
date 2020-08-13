"""Based on maryland tax laws"""
txa = []
stand_tax_rate = 0.6

print("What is the price of the item?:")
t = float(input()) 

txa.append(t)
  
print(txa)

def get_price_tax(txa):
	return txa * (1 + stand_tax_rate)
	print(stand_tax_rate)
final = map(get_price_tax, txa)
final_price = list(final)
print(final)


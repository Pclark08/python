import pprint 

"""Based on maryland tax laws"""
txas =  []   
stand_tax_rate = 0.06

print("What is the price of the item?:")
tax = float(input()) 

#add user input to a list 

#txas.append(t)
  
#print(txas)

def get_price_tax(t):
	return t * (1 + stand_tax_rate)


final_price = get_price_tax(tax)

print(final_price)




#print ( map(et_price_tax,  txas))
#final_price = list(final)
#print (final)	


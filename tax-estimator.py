import sys
print (sys.argv)

single =     {.1:   [     0.,   9325.],
			  .15:  [  9326.,  37950.],
			  .25:  [ 37951.,  91900.],
			  .28:  [ 91901., 191650.],
			  .33:  [191651., 416700.],
			  .35:  [416701., 418400.],
			  .396:	[418401., 800000.]}
head =       {.1:   [     0.,  13350.],
			  .15:  [ 13351.,  50800.],
			  .25:  [ 50801., 131200.],
			  .28:  [131201., 212500.],
			  .33:  [212501., 416700.],
			  .35:  [416701., 444550.],
			  .396:	[444551., 800000.]}
married_jt = {.1:   [     0.,  18650.],
			  .15:  [ 18651.,  75900.],
			  .25:  [ 75901., 233350.],
			  .28:  [153101., 212500.],
			  .33:  [233351., 416700.],
			  .35:  [416701., 470700.],
			  .396:	[470701., 800000.]}	  
married_si = {.1:   [     0.,   9325.],
			  .15:  [  9326.,  37950.],
			  .25:  [ 37951. , 76550.],
			  .28:  [ 76551., 116675.],
			  .33:  [116676., 208350.],
			  .35:  [208351., 235350.],
			  .396:	[235351., 800000.]}

def main():
	# determine category
	cat = raw_input("What category are you filing with (enter number and press ENTER)?\
		\n   1. Single\
		\n   2. Head of Household\
		\n   3. Married, filed jointly\
		\n   4. Married, filed separately\
		\n >>  ")

	if cat not in ['1', '2', '3', '4']:
		print("Sorry, I don't recognize that category.\
			  \nPlease enter 1, 2, 3, or 4.")
		return
	
	stipend = float(raw_input("What is your yearly graduate stipend (pre-tax)?\n >> "))
	tuition = float(raw_input("What is your yearly graduate school tuition?\n >> "))
	
	if cat == '1':
		tax_cat = single
		other = 0.0
	elif cat == '2':
		tax_cat = head
		other = 0.0
	elif cat == '3':
		tax_cat = married_jt
		other = float(raw_input("What is your spouse's taxable income?\n >> "))
	elif cat == '4':
		tax_cat = married_si
		other = 0.0

	total_income = stipend + tuition + other
	
	taxes = 0.0
	remaining_income = total_income
	
	# calculate taxes owed for each bracket
	
	print("You would owe the following amount for each tax level:")
	
	for percent, bracket in sorted(tax_cat.iteritems()):
		
		if total_income > bracket[1]:
			taxable = bracket[1] - bracket[0]
			taxed = percent*taxable
			remaining_income -= taxable
		
		elif bracket[0] <= total_income <= bracket[1]:
			taxed = percent*remaining_income
		
		else:
			taxed = 0.0
		
		taxes += taxed
		print("    {0} %: ${1}".format(percent*100., taxed))

	print("Total taxes owed: ${}".format(taxes))
	tax_percent = taxes/(stipend+other)*100.0
	print("This is {} % of your graduate stipend (plus other income from a spouse if applicable).".format(tax_percent))

if __name__ == "__main__":
	
	main()
	

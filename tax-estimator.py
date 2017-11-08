import sys
print (sys.argv)

single =     {.12:  [     0.,   45000.],
			  .25:  [ 45001.,  200000.],
			  .35:  [200001., 500000.],
			  .396:	[500001., 900000.]}
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


def get_category():
	"""Prompts user to select how they file taxes and selects the
	appropriate tax brackets.
	
	Returns:
	--------
		tax_cat: dict, keys are percents, values are tax bracket ranges
		stipend: float, the dollar amount submitted by user
		tuition: float, yearly tuition cost in $ submitted by user
		other: float, zero if not filing as joint married, otherwise value
			is submitted by user.
		exempt_old: float, exemption amount under current tax plan
	"""
	
	# Ask user to specify which category they are filing taxes.
	cat = int(raw_input("What category are you filing with (enter number and press ENTER)?\
		\n   1. Single\
		\n   2. Head of Household\
		\n   3. Married, filed jointly\
		\n   4. Married, filed separately\
		\n >>  "))

	# check that submitted cateorgy is acceptable.
	if cat not in [1, 2, 3, 4]:
		print("Sorry, I don't recognize that category.\
			  \nPlease enter 1, 2, 3, or 4.")
		return
	
	# warning about reliabilty of code if not filing as single
	if cat != 1:
		print("WARNING: This calculator is most accurate for a person who files as a single.")
	
	# prompt user to state their yearly tuition and stipend
	stipend = float(raw_input("What is your yearly graduate stipend (pre-tax)?\n >> "))
	tuition = float(raw_input("What is your yearly graduate school tuition?\n >> "))
	
	# assign proper values for each category	
	if cat == 1:
		# Single values
		tax_cat = single
		other = 0.0
		exempt_old = 4050.
		
	elif cat == 2:
		# Head of household
		tax_cat = head
		other = 0.0
		num = float(raw_input("How many exemptions do you usually file?\n >>"))		
		exempt_old = 4050.*num
		
	elif cat == 3:
		# married, filing jointly
		tax_cat = married_jt
		other = float(raw_input("What is your spouse's taxable income?\n >> "))
		num = float(raw_input("How many exemptions do you usually file?\n >>"))
		exempt_old = 4050.*num
	
	elif cat == 4:
		# married, filed separately
		tax_cat = married_si
		other = 0.0
		num = float(raw_input("How many exemptions do you usually file?\n >>"))
		exempt_old = 4050.*num
	
	return tax_cat, stipend, tuition, other, exempt_old
	
	
def calculate_taxes(tax_cat, total_income, deduction, exemption, stipend, other):
	
	# initiate counters
	taxes = 0.0
	remaining_income = total_income - deduction - exemption
	
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
	
	return taxes
		
def main():
	
	# determine category that person is filing
	tax_cat, stipend, tuition, other, exempt_old = get_category()

	# calculate total income by view of new tax cuts
	print("\n*** Calculating estimated taxes based on current taxes ***\n")
	deduction = 12000.
	total_income = stipend + tuition + other
	exemption = 0.0
	taxes_new = calculate_taxes(tax_cat, total_income, deduction, exemption, stipend, other)

	# calculate old:
	print("\n*** Calculating estimated taxes based on new taxes ***\n")
	deduction = 6350.
	total_income = stipend + other
	exemption = exempt_old
	taxes_old = calculate_taxes(tax_cat, total_income, deduction, exemption, stipend, other)
		
	print(taxes_old, taxes_new)
	

if __name__ == "__main__":
	
	main()
	

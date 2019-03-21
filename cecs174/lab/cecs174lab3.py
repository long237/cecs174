income= float(input("Enter your income here:$"))
TAX_LIM_10= 9525
TAX_LIM_12=38700
TAX_LIM_22= 82500
TAX_LIM_24= 157500
TAX_LIM_32=200000
TAX_LIM_35= 500000
TAX_LIM_37= 500000

TAX_12= 952.50
TAX_22= 4453.50
TAX_24= 14089.50
TAX_32= 32089.50
TAX_35= 45689.50
TAX_37= 150689.50

if income>=0 and income<= TAX_LIM_10: #10 percent tax
    tax= income*10/100
    print("tax liability: $ {0:.2f}".format(tax))
elif income >= (TAX_LIM_10+1) and income <= TAX_LIM_12: #12 percent tax
    income_12= income - TAX_LIM_10
    tax= income_12 * 12/100 + TAX_12
    print("tax liability: $ {0:.2f}".format(tax))
elif income >= (TAX_LIM_12+1) and income<= TAX_LIM_22:#22 percent tax
    income_22= income - TAX_LIM_12
    tax= income_22 * 22/100 + TAX_22
    print("tax liability: $ {0:.2f}".format(tax))
elif income >= (TAX_LIM_22+ 1) and income <= TAX_LIM_24: #24% tax
    income_24= income - TAX_LIM_22
    tax= income_24 * 24/100 + TAX_24
    print("tax liability: $ {0:.2f}".format(tax))
elif income >= (TAX_LIM_24 + 1) and income <= TAX_LIM_32: #32% tax
    income_32= income - TAX_LIM_24
    tax= income_32 * 32/100 + TAX_32
    print("tax liability: $ {0:.2f}".format(tax))
elif income >= (TAX_LIM_32 + 1) and income <= TAX_LIM_35: #35% tax
    income_35= income - TAX_LIM_32
    tax= income_35 * 35/100 + TAX_35
    print("tax liability: $ {0:.2f}".format(tax))
elif income >=(TAX_LIM_35 + 1) and income<= 9.5e6: #37% tax
    income_37= income - TAX_LIM_35
    tax= income_37 * 37/100 + TAX_37
    print("tax liability: $ {0:.2f}".format(tax))
elif income >= 10000000: # more than 10 million tax
    income_10e6= income - 10e6
    tax= TAX_37 + (9.5e6 * 37/100) + (income_10e6 *70/100)
    print("tax liability: $ {0:.2f}".format(tax))
tax_rate= (tax / income)*100
print("this is your tax rate: {0:.1f}".format(tax_rate))

#Research
#1) The average salary is: 88,849
#2) 0.89%
#3) 1 person in the class might be able to but it is hard to say.
    
    
    
    

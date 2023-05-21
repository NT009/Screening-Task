from tabulate import tabulate
import math
table = [['Product Name', 'Price ($)'], 
         ['Product A'	,20], 
         ['Product B',40 ], 
         ['Product C',50]]
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
cart=0
totalquantity=0
gift=0
discount=0
discountname=""
bulk5=0
tiered50=0
bulk10=0
flat10=0
#user input

table[0]=table[0]+['quantity','total price($)']
for i in range(1,4):
    cost=0
    table[i].append(int(input("how many quantity of "+table[i][0]+ " is required?\t")))
    cost=table[i][1]*table[i][2]
    str=input("if this product should be in gift wrap then enter y:-")
    cart=cart+cost
    totalquantity=totalquantity+table[i][2]
    table[i].append(cost)
    # gift fee
    if str=="y" or str=="Y":
        gift=gift+table[i][2]
    

#shipping fee
shipping=5*math.ceil(totalquantity/10)


#flat_10_discount
if cart>200:
    flat10=10
if discount<flat10:
    discount=flat10
    discountname="flat_10_discount"

#"bulk_10_discount
if totalquantity>20:
    bulk10=(cart*10/100)
if discount<bulk10:
    discount=bulk10
    discountname="bulk_10_discount"


#bulk_5_discount and tiered_50_discount
for i in range(1,4):
    if table[i][2]>10:
       bulk5=bulk5+(table[i][3]*5/100)
    if totalquantity>30 and table[i][2]>15:
        quantity=table[i][2]-15
        tiered50=tiered50+((quantity*table[i][1])*50/100)
if discount<bulk5:
    discount=bulk5
    discountname="bulk_5_discount"
if discount<tiered50:
    discount=tiered50
    discountname="tiered_50_discount"

#total
total=cart-discount+gift+shipping


#output
print(tabulate(table, headers='firstrow', tablefmt='fancy_grid'))
print('subtotal = ',cart)
print('discount name = ',discountname)
print('discount amount = ',discount)
print('gift wrap fee = ',gift)
print('shipping fee = ',shipping)
print('total = ',total)
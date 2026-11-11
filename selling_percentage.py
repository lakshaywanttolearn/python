p_selling = int(input("enter the selling price of a product :"))
p_cost = int(input("enter the cost price of a product :"))
res_selling = p_selling - p_cost
percent_selling = (res_selling/p_cost)*100
print("selling percentage is",percent_selling)

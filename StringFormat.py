

age=24

txt="i am timor shah and {} yers old"

print(txt.format(age))#i am timor shah and 24 yers old

quantity = 3
itemno = 567
price = 49.95
myorder = "I want {} pieces of item {} for {} dollars."
print(myorder.format(quantity, itemno, price))#I want 3 pieces of item 567 for 49.95 dollars.

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))#I want to pay 49.95 dollars for 3 pieces of item 567.




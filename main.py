# 🚨 Don't change the code below 👇
print("Welcome to Python Pizza Deliveries!")
size = input("What size pizza do you want? S, M, or L ")
bill = 0
if size=="s" or size== "S":
  bill = 15
  print("Small Pizza: $15")
if size =="m" or size =="M":
  bill = 20
  print("Medium Pizza: $20")
if size == "l" or size == "L":
  bill = 25
  print("Large Pizza: $25")
add_pepperoni = input("Do you want pepperoni? Y or N ")
if add_pepperoni == "Y" or add_pepperoni == "y":
  cost = input("You want Small Pepperoni or Large Pepperoni? S or L")
  if cost == "S" or cost == "s":
    bill+=2
    print("Pepperoni for Small pizza: $2")
  if cost == "L" or cost == "l":
    bill+=3
    print("Pepperoni for Large pizza: $3")

extra_cheese = input("Do you want extra cheese? Y or N ") 
if extra_cheese == "Y" or extra_cheese == "y":
  bill+=1
  print("Extra cheese for any size pizza: $1")
print(f"Your final bill is ${bill}")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇






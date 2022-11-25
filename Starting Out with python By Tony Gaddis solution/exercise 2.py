########################
# Exercise 2 solutions #
########################


#1. Personal information
def print_personal_info():
    print("Tony Gaddis")
    print("address, city, state, zip xxxx")
    print("telephone numer: xxxx")
    print("computer programming")

#2. Sales Prediction
def profit():
    total_sales = input("Please enter the amount of total sales: ")
    print("your annual predicted profit is", str(int(total_sales) * 0.23))
    
#3. Pounds to Kilograms
def pounds_to_kilo():
    pounds = input("Please enter the mass of object in pounds: ")
    print("To kilograms: ", str(int(pounds) * 0.0454))

#4. Total Purchase
def purchase():
    first = int(input("Please enter the price of first item: "))
    second = int(input("Please enter the price of second item: "))
    third = int(input("Please enter the price of third item: "))
    fourth = int(input("Please enter the price of fourth item: "))
    fifth = int(input("Please enter the price of fifth item: "))
    subtotal = first + second + third + fourth + fifth
    tax = subtotal * 0.07
    total = subtotal + tax
    print("Subtotal:", subtotal, "Tax:", tax, "Total:", total)

#5. Distance Traveled
def distance():
    print("car travel in 6 hours:", str(70*6))
    print("car travel in 10 hours:", str(70*10))
    print("car travel in 15 hours:", str(70*15))

#10. Ingredient Adjuster
def ingredient_adjuster():
    num_cookies = int(input("Please enter the number of cookie you wish to make: "))
    print("cups of sugar:", num_cookies * 1.5)
    print("cups of butter:", num_cookies * 1)
    print("cups of flour:", num_cookies * 2.75)

#11. Male and Female Percentages
def percentage():
    num_male = int(input("Please enter the number of male: "))
    num_female = int(input("Please enter the number of female: "))
    total = num_male + num_female
    print("The percentage of male is:", num_male/total)
    print("The percentage of female is:", num_female/total)

#15. Turtle Graphics Drawings
import turtle as tr
def turtle_sec1():
    wn = tr.Screen()
    wn.bgcolor("light blue")
    tr.color("black", "white")
    tr.begin_fill()
    tr.left(45)
    tr.forward(100)
    tr.right(90)
    tr.forward(200)
    tr.left(90)
    tr.forward(100)
    tr.left(90)
    tr.forward(100)
    tr.left(90)
    tr.forward(200)
    tr.right(90)
    tr.forward(100)
    tr.end_fill()
    
  

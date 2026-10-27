name = input("enter your name")
while name == "":
    print("you didnt enter your name")
    name = input("enter your name")

print(f"hii {name}")

# compound interest calculator
principle = 0
rate = 0
time = 0

while principle<=0:
    principle = float(input("enter your principle : "))
    if principle<=0:
       print("priciple cant be less than 0")

while rate<=0:
    rate = float(input("enter your rate : "))
    if rate<=0:
       print("rate cant be less than 0")

while time<=0:
    time = float(input("enter your time :"))
    if time<=0:
       print("time cant be less than 0")


compound_interest = principle*pow(1+rate/100),time)
print("the balance after {time} is {compound_interest}")



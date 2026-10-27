for_sale = True
if for_sale:
    print('you are eligible sale')
else:
    print('you are not eligible sale')

a = int(input("enter a number : "))
b = int(input("enter another number : "))
bai = "success" if a>b else "fail"
print(bai)
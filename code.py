def addition(x,y):
  return (x+y)
  
def substraction(x,y):
  return (x-y)
  
def multiplication(x,y):
  return (x*y)
  
def division(x,y):
  if y==0:
    return "Cannot divide by Zero"
  else:
    return (x/y)

print("Welcome To Simple Calculator By Ritam:")
print("Select Operation")
print("1. Addition")
print("2. Substraction")
print("3. Multiplication")
print("4. Division")
print("5. Exit")

while True:
  choice=input("Enter Choice:1/2/3/4/5\n")

  if choice == "5":
     print("Thanks For Using This,Good Bye")
     break

  if choice in ("1","2","3","4","5"):
    num1=int(input("Enter First Number\n"))
    num2=int(input("Enter Second Number\n"))
    
    if choice == "1":
      print("Result:",addition(num1,num2))
    elif choice == "2":
      print("Result:",substraction(num1,num2))
    elif choice == "3":
      print("Result:",multiplication(num1,num2))
    elif choice == "4":
      print("Result:",division(num1,num2))
  
  else:
    print("Invalid Input,Please Enter a Valid Input")



  

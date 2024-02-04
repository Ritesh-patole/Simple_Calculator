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

def display_menu():
  print("\n---------Welcome To Simple Calculator By Ritam----------")
  print("Select Operation")
  print("1. Addition")
  print("2. Substraction")
  print("3. Multiplication")
  print("4. Division")
  print("5. Exit")

while True:
  display_menu()
  choice=input("Enter Choice:1/2/3/4/5\n")

  if choice == "5":
     print("Thanks For Using This,Good Bye")
     break

  if choice in ("1","2","3","4"):
    try:
      num1=int(input("Enter First Number\n"))
      num2=int(input("Enter Second Number\n"))
    except ValueError:
            print("Invalid input! Please enter valid numbers.")
            continue
    
    if choice == "1":
      print("Result:",addition(num1,num2))
    elif choice == "2":
      print("Result:",substraction(num1,num2))
    elif choice == "3":
      print("Result:",multiplication(num1,num2))
    elif choice == "4":
            result = division(num1, num2)
            if result == "Cannot divide by Zero":
                print("\nError: Cannot divide by Zero. Please enter a non-zero divisor.")
            else:
                print(f"\nResult: {num1} / {num2} = {result}")
  
  else:
    print("Invalid Input,Please Enter a Valid Input")



  

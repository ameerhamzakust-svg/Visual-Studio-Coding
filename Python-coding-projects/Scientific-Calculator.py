import math

#OPERATION
def add(a,b):
    return a + b

def subtract(a,b):
   return a - b

def multiply(a,b):
    return a * b

def division(a,b):
    return a / b

def power(a,b):
    return math.pow(a,b)

def square(a):
    return a * a

def cube(a):
    return a ** 3

def square_root(a):
    return math.sqrt(a)

def cube_root(a):
    return math.cbrt(a)

def factorial(a):
    return math.factorial(a)

def reciprocal(a):
    result = (1/a)
    return result

def absolute_value(a):
       return abs(a)

def percentage():
    part=float(input("enter the part number : "))
    whole=float(input("enter the whole number : "))
    result = (part/whole)*100
    return result 



def sin(angle):
    return math.sin(math.radians(angle))

def cos(angle):
    return math.cos(math.radians(angle))

def tan(angle):
    return math.tan(math.radians(angle))

def sin3(angle):
    return math.sin(angle)

def cos3(angle):
    return math.cos(angle)

def tan3(angle):
    return math.tan(angle)




def asine(angle):
    return math.degrees(math.asin(angle))

def acose(angle):
    return math.degrees(math.acos(angle))

def atane(angle):
    return math.degrees(math.atan(angle))

def asin(angle):
    return math.asin(angle)

def acos(angle):
    return math.acos(angle)

def atan(angle):
    return math.atan(angle)




#LOGARITM/EXPONENTIAL

def logarithm(a):
    return math.log10(a)

def natural_logarithm(a):
    return math.log(a)

def exponential(a):
    return math.exp(a)


#NUMBER THEORY

def permutation(a,b):
    return math.perm(a,b)

def combination(a,b):
    return math.comb(a,b)

def gcd(a,b):
    return math.gcd(a,b)

def lcm(a,b):
    return math.lcm(a,b)


#ROUNDING

def ceil(a):
    return math.ceil(a)

def floor(a):
    return math.floor(a)

def sign_change(a):
    return -a

history =[]
memory = 0
result = 0 

while True:
    print()
    print("========== CALCULATOR ==========")
    print()
    print("1.Basic Operations")
    print("2.TRIGNOMETRY")
    print("3.LOGARITHM/exponential")
    print("4.NUMBER THEORY")
    print("5.ROUNDING")
    print("6.Memory")
    print("7.History")
    print("8.Clear")
    print("9.Exit")

    print()
    choose=input("enter the choice of the calculator : " )
    print()
    if choose == "1":
    
        print("1.Add")
        print("2.Subtract")
        print("3.Multiply")
        print("4.Division")
        print("5.Power")
        print("6.Square")
        print("7.Cube")
        print("8.Square root")
        print("9.Cube root")
        print("10.factorial")
        print("11.Reciprocal")
        print("12.Absolute Value")
        print("13.percentage")
        print("14.Change Sign (+/-)")
        print("0.Back to the main menu ")
        print()
        choice =input("enter the opeation no you want to perform : ")
        print()
        if choice == "1":

            try:

                num1=float(input("enter the first number : "))
                num2=float(input("enter the second number : "))

            
                result = add(num1, num2)

                print("Result:", result)

                history.append(f"{num1} + {num2} = {result}")
            except ValueError:
                print("Error: Please enter valid numbers.")
        
        elif choice == "2":

            try:
            
                num1=float(input("enter the first number : "))
                num2=float(input("enter the second number : "))
            
                result = subtract(num1, num2)

                print("Result:", result)

                history.append(f"{num1} - {num2} = {result}")
            except ValueError:
                print("Error: Please enter valid numbers.")

        
        elif choice == "3":
            try:
                num1=float(input("enter the first number : "))
                num2=float(input("enter the second number : "))
            

            
                result = multiply(num1, num2)

                print("Result:", result )

                history.append(f"{num1} * {num2} = {result}")
            except ValueError:
                print("Error: Please enter valid numbers.")

        elif choice == "4":
            try:
                num1=float(input("enter the first number : "))
                num2=float(input("enter the second number : "))
            

                result = division(num1,num2)

                print("Result:", result)

                history.append(f"{num1} / {num2} = {result}")
            except ZeroDivisionError:
                print("Cannot be divided by zero . ")

            except ValueError:
                print("Error: Please enter valid numbers.")

        elif choice == "5":
            try:
                num=float(input("enter the number  : "))
                power_number=float(input("enter the power you want  : "))
        

                result = pow(num,power_number)

                print("Result:", result)

                history.append(f"{num} ** {power_number} = {result}")
            except ValueError:
                print("Error: Please enter valid numbers.")

        elif choice == "6":
            try:
                num=float(input("enter the  number you want square of  : "))
        

                result = square(num)

                print("Result:", result)

                history.append(f"{num} * {num} = {result}")

            except ValueError:
                print("Error: Please enter valid numbers.")

        elif choice == "7":
            try:
                num=float(input("enter the number you want cube of  : "))
        

                result = cube(num)

                print("Result:", result)

                history.append(f"{num} * {num} * {num} = {result}")
            except ValueError:
                print("Error: Please enter valid numbers.")

        elif choice == "8":
            try:
                num=float(input("enter the number you want the square root of  : "))
            
                result = square_root(num)

                print("Result:", result)

                history.append(f"square-root {num} = {result}")

            except ValueError:
                print("Error: Square root requires a non-negative number.")

        elif choice == "9":
            try:

                num=float(input("enter the number you want cube root of  : "))
            

                result = cube_root(num)

                print("Result:", result)

                history.append(f"Cube-root {num} = {result}")
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == "10":
        
            try:
                num=int(input("enter the number you want factorial of  : "))
            

                result = factorial(num)

                print("Result:", result)

                history.append(f"Factorial {num} = {result}")
            except ValueError:
                print("Error: Factorial requires a non-negative integer.")

        elif choice == "11":
            try:
                num=float(input("enter the number you want reciprocal of  : "))
            
                result = reciprocal(num)

                print("Result:", result)

                history.append(f"Reciprocal{num} = {result}")
            except ZeroDivisionError:
                print("Error: Cannot find reciprocal of zero.")

            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == "12":
            try:
                num=float(input("enter the number you want absolute value of  : "))
            
                result = absolute_value(num)

                print("Result:", result)

                history.append(f"Absolute Value {num} = {result}")
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == "13":
            try:
                part=float(input("enter the part number : "))
                whole=float(input("enter the whole number : "))
                result = (part/whole)*100


                print("Result:", result)

                history.append(f"{part} / {whole} * {100} = {result}")
            except ZeroDivisionError:
                print("Error: Whole number cannot be zero.")

            except ValueError:
                print("Error: Please enter valid numbers.")

        elif choice == "14":
            try:
                num=float(input("enter the number you want to change sign of  : "))
            

                result = sign_change(num)

                print("Result:", result)

                history.append(f"Sign Change {num} = {result}")
            except ValueError:
                print("Error: Please enter a valid number.")


        elif choice == "0":
            continue

        else:
            
            print("Invalid choice. Please try again.")
    elif choose == "2":

        print("Angle mode : ") 
        print()

        print("1.Degree")
        print("2.Radian")
        print("0.Back to the main menu ")

        print()

        mode=input("choose the angle mode  for : ")
        print()
        if mode == "1":

            print("✓ Angle mode set to DEG") 
            print()

            print("Trignometry :----")
            print()

            print("1.sin")
            print("2.cos")
            print("3.tan")

            print("Inverse Trignometry :---- ")
            print()


            print("4.asin")
            print("5.acos")
            print("6.atan")
            print("0.Back to the main menu ")
            print()
            choice = input("choose which trignometry operation you want to perform : ")
            print()
            if choice == "1":
                try:
                    angle=float(input("enter the angle : "))
        
                    result = round(sin(angle),6)

                    print("Result:", result)

                    history.append(f"sin {angle} = {result}")

                except ValueError:
                    print("Error: Please enter a valid number.")
                
            elif choice == "2":
                try:
                    angle=float(input("enter the angle : "))
                    result = round(cos(angle),6)

                    print("Result:", result)

                    history.append(f"Cos {angle} = {result}")
                except ValueError:
                    print("Error: Please enter a valid number.")

            elif choice == "3":
                try:
                    angle=float(input("enter the angle : "))

                    result = round(tan(angle),6)

                    print("Result:", result)

                    history.append(f" tan{angle} = {result}")
                except ValueError:
                    print("Error: Please enter a valid number.")
    
            elif choice == "4":
                try:
                    angle=float(input("enter the angle : "))

                

                    result = round(asine(angle),6)

                    print("Result:", result)

                    history.append(f"asin {angle} = {result}")
                except ValueError:
                    print("Error: asin input must be between -1 and 1.")
            elif choice == "5":
                try:
                    angle=float(input("enter the angle : "))
                
                    result = round(acose(angle),6)

                    print("Result:", result)

                    history.append(f"acose {angle} = {result}")
                except ValueError:
                    print("Error: acos input must be between -1 and 1.")
            elif choice == "6":
                try:

                    angle=float(input("enter the angle : "))



                    result = round(atane(angle),6)

                    print("Result:", result)

                    history.append(f" atane{angle} = {result}")
                except ValueError:
                    print("Error: Please enter a valid number.")

            
            elif choice == "0":
                continue

            else:
                print("Invalid choice. Please try again.")
    
        elif mode == "2":
            print()
            print("✓ Angle mode set to RADIAN")
            print()

            print("Trignometry :----")
            print()
            print("1.sin")
            print("2.cos")
            print("3.tan")
            print()
            print("Inverse Trignometry :---- ")
            print()
            print("4.asin")
            print("5.acos")
            print("6.atan")
            print("0.Back to the main menu ")
            print()
            choice = input("enter the choice of the radian mode : ")
            print()
            if choice == "1":
                try:
                    angle=float(input("enter the angle : "))

                    result = round(sin3(angle),6)

                    print("Result : " , result)

                    history.append(f"sin3{angle} = {result}")
                except ValueError:
                    print("Error: Please enter a valid number.")
    
            elif choice == "2":
                try:
                    angle=float(input("enter the angle : "))
     
                    result = round(cos3(angle),6)

                    print("Result:", result)

                    history.append(f"cos3{angle} = {result}")
                except ValueError:
                    print("Error: Please enter a valid number.")

            elif choice == "3":
                try:
                    angle=float(input("enter the angle : "))

                    result = round(tan3(angle),6)

                    print("Result:", result)

                    history.append(f"tan3{angle} = {result}")
                except ValueError:
                    print("Error: Please enter a valid number.")
    
            elif choice == "4":
                try:
                    angle=float(input("enter the angle : "))
                
                    result = round(asin(angle),6)

                    print("Result:", result)

                    history.append(f"asin(angle) = {result}")

                except ValueError:
                    print("Error: asin input must be between -1 and 1.")


            elif choice == "5":
                try:
                    angle=float(input("enter the angle : "))

                
                    result = round(acos(angle),6)

                    print("Result:", result)

                    history.append(f"acos{angle }= {result}")
                except ValueError:
                    print("Error: acos input must be between -1 and 1.")

            elif choice == "6":
                try:
                    angle=float(input("enter the angle : "))


                    result = round(atan(angle),6)

                    print("Result:", result)

                    history.append(f"atan{angle} = {result}")
                except ValueError:
                    print("Error: Please enter a valid number.")

            elif choice == "0":
                continue

            else:
                print("Invalid choice. Please try again.")

        elif mode == "0":
            continue

        else:
            print("Invalid choice. Please try again.")
        


    elif choose == "3":

        print("1.Common Logarithm (log₁₀)")
        print("2.Natural Logarithm (ln)")
        print("3.Exponential (eˣ)") 
        print("0.Back to the main menu ")
        print()
        choice =input("enter the choice of logarithmic/exponential : ")
        print()

        if choice == "1":

            try:
                value = float(input("enter the value  : "))

            
                result = logarithm(value)

                print("Result:", result)

                history.append(f"logarithm {value} = {result}")

            except ValueError:
                print("Error: Logarithm input must be greater than 0.")

        elif choice == "2":
            try:

                value = float(input("enter the value : "))
            
                result = natural_logarithm(value)

                print("Result:", result)

                history.append(f"natural logarithm{value} = {result}")

            except ValueError:
                print("ln input must be greater than zero . ")
            
        elif choice == "3":
            try:
                value = float(input("enter the value : "))
            

                result = exponential(value)

                print("Result:", result)

                history.append(f"exponential(value) = {result}")

            except OverflowError:
                print("Error: Number is too large.")
            
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == "0":
            continue

        else:
            print("Invalid choice. Please try again.")       

    elif choose =="4":
        print("1.Permutation")
        print("2.Combination")
        print("3.GCD")
        print("4.LCM")
        print("0.Back to the main menu ")

        print()
        choice=input("enter the choice of number theory operation you want to perform : ")
        print()

        if choice == "1":
            try:
                n=int(input("enter the n value : "))
                r=int(input("enter the r value  : "))
            
                result = permutation(n,r)

                print("Result:", result)

                history.append(f"{n} P {r} = {result}")

            except ValueError:
                print("Error: n and r must be non-negative integers, with n >= r.")

        elif choice == "2":
            try:
                n=int(input("enter the n value  : "))
                r=int(input("enter the r value : "))
            
                result = combination(n,r)

                print("Result:", result)

                history.append(f"{n} C {r} = {result}")
            except ValueError:
                print("Error: n and r must be non-negative integers, with n >= r.")
    
        elif choice == "3":
            try:
                num1=int(input("enter the first number : "))
                num2=int(input("enter the second number : "))
        
                result = gcd(num1,num2)

                print("Result:", result)

                history.append(f"GCD {num1} , {num2} = {result}")

            except ValueError:
                print("Error: Please enter integers.")
        elif choice == "4":
            try:
                num1=int(input("enter the first number : "))
                num2=int(input("enter the second number : "))
            
                result = lcm(num1,num2)

                print("Result:", result)

                history.append(f"LCM {num1} , {num2} = {result}")
            except ValueError:
                    print("Error: Please enter integers.")

        elif choice == "0":
            continue

        else:
            print("Invalid choice. Please try again.")


    elif choose == "5":


        print("1.ceil")
        print("2.floor")
        print("0.Back to the main menu ")
        print()
        choice=input("enter the choice for rounding operation you want to perform :  : ")
        print()

        if choice == "1":
            try:
                num=float(input("enter the first number : "))
            
                result = ceil(num)

                print("Result:", result)

                history.append(f"Ceil {num} = {result}")
            except ValueError:
                print("Error: Please enter a valid number.")
        elif choice == "2":
            try:
                num=float(input("enter the first number : "))
            
                result = floor(num)

                print("Result:", result)

                history.append(f" Floor {num} = {result}")
            except ValueError:
                print("Error: Please enter a valid number.")

        elif choice == "0":
            continue

        else:
            print("Invalid choice. Please try again.")

    elif choose == "6":



        print("1.Memory add(M+)")
        print("2.Memory subtract(M-)")
        print("3.Memory recall(MR)")
        print("4.Memory Clear (MC)")
        print("0.Back to the main menu ")
        print()
        choice = input("enter the option from the memory : ")
        print()


        if choice == "1":

            memory = memory + result 

            print("Result of M+ : ",memory)

        elif choice == "2":

            memory = memory  -  result
            print("Result of M- : " , memory)

        elif choice == "3":
            print("Memory : " , memory)

        elif choice == "4":
                
                memory = 0
                print("Memory cleared!" )
                print("current Memory : ", memory )


        elif choice == "0":
            continue

        else:
            print("Invalid choice. Please try again.")

    elif choose == "7":

        print("1.Show History")
        print("2.Clear History")
        print("0.Back to the main menu ")

        print()
        choice = input("enter the operation number you want  :  ")
        print()

        if choice == "1":
            if history:

                for i, calculation in enumerate(history, 1):
                    print(i, calculation)
                
            else:
                print("No history available . ")

        elif choice == "2":
            
            history.clear()
            print("History Cleared")


        elif choice == "0":
            continue

        else:
            print("Invalid choice. Please try again.")

    elif choose == "8":
       print()
       result = 0 
       print(" Current result cleared.")

    elif choose == "9":
        
        print("Thank you so much for using my Calculator .  ")
        
        print("-----------Goodbye-----------")
        break






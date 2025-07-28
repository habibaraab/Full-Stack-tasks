#الفانكشن هتشتغل عادي بقيمة ال local variable ولن تتغير قيمة ال Global variable
# name = "Habiba"

# def show_name():
 
#   name = "Asmaa"
#   print("Inside function", name)


# print("Outside function before call", name)
# show_name()
# print("Outside function after call", name)


#هيرمي اكسبشن عشان طبعت قيمة local variable قبل ما assign value 
# x = 10

# def case2():
#   print(f"The value of x is: {x}")
#   x = 5 

# try:
#     case2()
# except UnboundLocalError as e:
#     print(f"\nError: {e}")



# ch = lambda x: x * 10
# res = ch(5)

# print(f"5 multiplied by 10 is: {res}")


# import datetime

# birth_date = datetime.datetime(2000, 1, 1)

# today = datetime.date.today()


# age = today.year - birth_date.year 

# print(f" The age is: {age}")


# try:
#     n1 = float(input("Enter the first number "))
#     n2 = float(input("Enter the second number "))

#     res = n1 / n2

#     print(f"The result of {n1} / {n2} is: {res}")

# except ZeroDivisionError:
#     print("\n You cannot divide by zero")


# try:
#     name = input(" enter your name: ")

#     file_name = "hello.txt"
#     with open(file_name,"w") as f:
#      f.write("Hello,{name}")

#     print(f"Success! The file '{name}' was created.")
    
# except IOError as e:
#     print(f"Error: {e}")




# f = "names.txt"
# try:
#     user_name = input(" enter your name: ")

#     with open(f, 'a') as file:
#         file.write(user_name + '\n')

#     print(f"Success!")

# except IOError as e:
#     print(f"\n error: {e}")

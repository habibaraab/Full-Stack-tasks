# python -> easy to learn 
# pyhton -> web , ai , iot , analysis 

    #    interpreter ,     compiler 
    #    line by line         all code at one time 
    #     low                   high
    #     python                c, c++
    

#  variables -> container store data 

#  2    -    var2
# keywords 
# my-var   - my_var
#  my var  - myVar 

#  variable case-sensitive  -> capital not equal small

#  camel case ->  myVariableName
# Pascal case -> MyVariableName
# snake case -> my_variable_name

# x=12
# print(x)

# x=12
# x="ali"

# x= "red"
# y="blue"

# x,y="red","blue"
# x=y="red"
# fruits = ['apple','banana','cherry']
# x,y,z=fruits

# x = "pyhon "
# y= "is "
# z="awesome "
# print(x + y + z)

# ---------------------------------------------------
# datatype 

# primitive               no-primitive
# immutable               mutable   -> list, dic , tuple , set

# x= 19
# x= 10
# int , float , bool , str -> one value

# text       str
# numeric     int , float , complex
# sequance    list, tuple , range
# mapping     dict
# set         set
# boolean      bool
# binary        bytes 
# non        none

# x="ali"
# print(type(x))
# ---------------------------------------------------------------
#  Numbers   -> int , float , complex

# x = 1    int
# y = 2.8  float
# z = 1j    complex

# loasely type ->   int x 

# x= min(5,12,25,30)
# y = max(54,65,32,76)

# # z=abs(-7)    return positive
# x=pow(4,3)

# sqrt   ceil floor pi
# import math

# x=math.sqrt(64)
# x=math.ceil(1.4)   -> above
# x=math.floor(1.4)   > down
# x=math.pi
# print(round(2.3))
# ----------------------------------------------------------------------------------

# Strings  -> array of char
# a="Hello, World! ,       "
# print(a[1])
# print(a[2:5])   end not returned 
# print(a[:5])
# print(a[2:])
# print(a[-5:-2])   ->   

# print(a.upper())
# print(a.lower())
# strip -> removes white spaces
# a.replace("H","J")
# a.split(",")
# a.capitalize()

# a="Hello, World!"
# print(id(a))
# a=a.upper()
# print(id(a))

# age = 30
# txt ="my name is ali , iam " + age       concate between str + num wrong
# print(txt)

# f-string
# age = 30
# txt = f"my name is ali , iam {age}"
# print(txt)

# name= "ali"
# age=30
# address ="shebeen"
# txt= f"my name is {name} and age is {age} and address equal {address}"

# # format method
# name= "ali"
# age=30

# "my name is {} and age is {}".format(name,age)

# string multiplication

# txt="hi"
# print(txt*3)  hihihi

# txt = "we are "happy""

# txt = "we are \"happy\""
# -----------------------------------------------------------------
# booleans -> true , false 
# False
# None
# bool(0)
# bool("")
# []
# ()
# {}

# ----------------------------------------------------------
#  operators in python 
# Arithmetic operator (+ , - , * , %)
# numbers 
# print(2+2)
# print(2-2)
# print(2*2)
# print(2/2)
# print(10%2)

# Assigment operator -> (= , +=,-=)

# x=10
# x+=1
# Comparison operator (== , === , != , > , < , >= ,<=)
# logical operator (and , or , not )&& , || , ~
# and true -> true 
# false and true -> False
# true and true -> true 


# or -> false 

# true not false 

# identity operator (is , is not )  

# membership oprator ->  in  ,  not in  

#  bitwise operator  (& , | , ^ , ~)  numbers 
#    ~ 1
# 2 & 3 ->  2-> 0010    & 0100
# 2 | 3
# 2 ^ 3 
# 1 : 1 -> false 
# 0011
# 0101
# 0000  -> 

#  operator precedence ->    print((6+3)-)
# ---------------------------------------------------------------

# import math

# x = input("Enter yor age ") 
# print(math.sqrt(int(x)))

#  casting   datatype -> datatype

# implicit  -> compiler-  float + int  -> float 

# explicit  -> programmer ->         complex -> int  
# int(2.8) -> 2
# float(1)-> 1.0
# str(12) '12'  type (str(12))-> str
 
# ----------------------------------------------------

#  conditions if 

# a= 33
# b = 200

# if b > a :
#    print("b>a")
# elif a==b:
#    print("a==b")
# else:
#    print("a>b")

#  short hand if

# if a>b : print("a>b")

# # short hand if  else

# print("a>b") if a>b else print("b>a") 

# print("a>b") if a>b else print("a=b") if a == b else print("b>a") if  ----- else
# if a>b:
#     a
# elif a==b

# else: 
#     b



#  nested if

# x =40
# if x > 10:
#     print("x>10")
#     if x>20:
#         print("x>10 and x > 20")
#     else :
#         print(" kmkksg")

# a=200
# b=33
# c=500
# if a>b or c>a:
#     print("two true")


# a= 33
# b =200

# if b>a:
#     pass

# -------------------------------------------------

# match

# no switch case 

# match expression:
#     case x:
#         block
#     case y:


#     case _:


day = 4
isWinter =True
match day:
    case 1:
        print("day is 1")
    case 2: 
        print("day is 2")
    case 4 | 5 if isWinter == False:
        print("day is 4")
    case _:
        print("day not exist")




# x ="mohamed"

# if 'oommm' in x:
#     print("exists")
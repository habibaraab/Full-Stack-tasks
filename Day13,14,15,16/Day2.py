#Q1

# def sum(l):
#     total = 0
#     for n in l:
#         if n % 2 == 0:
#             total += n
#     return total

# my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
# even_sum = sum(my_list)

# print(f"Sum of even numbers: {even_sum}")

#Q2
# t = (15, 8, 99, 27, 42)
# maxx = max(t)
# print(f"The maximum value is: {maxx}")


#Q3
# arr = [2, 8, 4, 2, 6, 4, 8, 8]
# my_set = set(arr)
# my_list = list(my_set)
# print(f"List with duplicates removed: {my_list}")

#Q4
# def countt(s):
#     e_count = 0

#     for ch in s.lower():
#         if ch == 'e':
#             e_count += 1

#     print(f"The character 'e' appears {e_count} times")


# ss = input("Enter a string: ")
# countt(ss);


#Q5
# def generate(length, start):
#     l = []
    
#     for i in range(length):
#         l.append(start + i)
        
#     print(f"My list: {l}")

# generate(6, 1)

#Q6
# def get_user_info():

#     while True:
#         name = input("Enter your name: ")
#         if name and not name.isdigit():
#             break
#         print("Invalid input")

#     email = input("Enter your email: ")
#     print(f"Name: {name}")
#     print(f"Email: {email}")

# get_user_info()


#Q7
# import re
# def confirm_data():
  
#     while True:
#         name = input(" enter your name: ")

#         if not name or not name.isalpha():
#             print("enter valid name")
#             continue 

#         break

#     while True:
#         email = input(f"enter your email : ")

#         pattern = r"^[a-zA-Z0-9_.+-]+@[a-zA-Z0-9-]+\.[a-zA-Z0-9-.]+$"
        
#         if re.match(pattern, email):
#             break
#         else:
#             print("enter a valid email.")
#             continue 

#     print(f"   Name: {name}")
#     print(f"   Email: {email}")


# confirm_data()


#Q8
# total = 0
# count = 0

# while True:
#     num = input("Enter a number or done to finish: ")

#     if num.lower() == 'done':
#         break  

    
#     t = num
    
#     if not t.isdigit():
#         print("Invalid input")
#         continue

#     number = float(num)

#     count +=1
#     total +=number


# if count > 0:
#     average = total / count
# else:
#     average = 0  


# print(f"Total: {total}")
# print(f"Count: {count}")
# print(f"Average: {average}")


#Q9
# def sort_list():
#     l = []
#     print(" enter 5 numbers.")
#     for i in range(5):
#         while True:
#             num = input(f"Enter number {i+1}: ")
#             l.append(int(num))
            
#             break

#     l.sort()
#     print(f"Sorted in ascending order: {l}")

#     l.sort(reverse=True)
#     print(f"Sorted in descending order: {l}")

# sort_list()

#10
# def find_l(st, letter):
 
#     count = st.lower().count(letter.lower())
#     print(f"The letter  appears {count} time(s) ")
#     return count

# find_l("This is a sample Tests.", "s")


#Q11
# def find_l_g(nums):
 
#     if len(nums) < 2:
#         print("List must contain at least two numbers.")
#         return

#     sorted_nums = sorted(list(set(nums))) 


#     second_lowest = sorted_nums[1]
#     second_greatest = sorted_nums[-2]

#     print(f"Second lowest number is: {second_lowest}")
#     print(f"Second greatest number is: {second_greatest}")

# find_l_g([1, 2, 3, 4, 5, 5, 1])
# find_l_g([10, 8, 4, 6, 2])


#Q12

# def is_prime(num):
#     f = True
#     if num > 1:
#         for i in range(2, num // 2 + 1):
#             if (num % i) == 0:
#                 f = False
#                 break
#     else:
#         f = False

#     if f:
#         print(f" is a prime number.")
#     else:
#         print(f"is not a prime number.")

# is_prime(7)
# is_prime(10)
""" 
1. write a question paper maker that can accept question of marks 1,2,3,4,5,10 and accept as many question as user want and then ask the user that how many questions he want in the question paper of the specific marks and then ask for how many sets he want of the paper and design the question paper (differents sets should have different questions).

2.A CSV data processing: Write a Python program that takes a CSV file as input, processes the data and performs some calculations or analysis

"""

# import csv, sys
# import pandas as pd

# fields_dict = ["Name", "sub1", "sub2", "sub3"]
# rows_dict = [['x', '10', '20', '30'], ['y', '40','50','60'], ['z', '70','80','90']]


# # file = open("test.csv","w")
# # write_data = csv.writer(file)

# # write_data.writerow(fields_dict)
# # write_data.writerows(rows_dict)

# def student_info():
#     # file = open("test.csv", "r")
#     # # read_data = csv.reader(file)
#     # for i in file:
#     #     new = i.replace("\n",",")
#     file = pd.read_csv("D:\\VScode\\python\dcs\\maintest\\test.csv")
#     df = pd.DataFrame(data=file)
#     print(df)
#     print("Student names are: ",df.pop('name'))
#     for marks in range(4):
#         print('name',marks)
#         add += df.iloc[marks]
#         print(add)

# def marks():
#     file = pd.read_csv("D:\\VScode\\python\dcs\\maintest\\test.csv")
#     df = pd.DataFrame(data=file)
#     print("Student names are: ",df.pop('name'))
#     for marks in range(4):
#         print('name',marks)
#         add += df.iloc[marks]
#         print(add)

    

# print("""[1] To see the names of students
# [2] To see the marks of Student
# [3] To exit the program""")

# ch = int(input("Enter your choice: "))
# if ch ==1:
#     student_info()
# elif ch==2:
#     marks()
# else:
#     print("Exiting...")
#     sys.exit(0)

# import random

# print("Question paper maker")

# set_1m = []
# set_2m = []
# set_3m = []
# set_5m = []
# set_10m = []

# print("")

# def sum_divisors(n):
#   sum = 0
#   i = n-1
#   while i>0:
#     if n%i==0:
#       sum = sum+i
#     i = i-1
#   # Return the sum of all divisors of n, not including n
#   return sum

# print(sum_divisors(0))
# # 0
# print(sum_divisors(3)) # Should sum of 1
# # 1
# print(sum_divisors(36)) # Should sum of 1+2+3+4+6+9+12+18
# # 55
# print(sum_divisors(102)) # Should be sum of 2+3+6+17+34+51
# # 114

""" def count_users(group):
  count = 0
  for member in get_members(group):
    if is_group(member):
      count += count_users(member)
    else:
      count += 1
  return count

print(count_users("sales")) # Should be 3
print(count_users("engineering")) # Should be 8
print(count_users("everyone")) # Should be 18 """

def sum_positive_numbers(n):
    # base case
    if n == 1:
        return 1
    # recursive case
    else:
        return n + sum_positive_numbers(n-1)

print(sum_positive_numbers(3)) # Should return 6
print(sum_positive_numbers(5)) # Should return 15
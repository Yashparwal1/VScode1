# a = [17 , 28, 30]
# b = [99 , 16, 8]

# alice = 0
# bob = 0
# for i in range(3):
#     if a[i] > b[i]:
#         alice += 1
#     elif a[i] < b[i]:
#         bob += 1
#     else:
#         continue
# print(alice , bob)

# -------------------------------------------

# arr = [[11, 2, 4], [4, 5, 6], [10, 8, -12]]
# n = 3
# left = 0
# right = 0
# for i in range(n):
#     left += arr[i][i]
#     right += arr[i][n-1-i]
# ab_diff = abs(left - right) 

"""
# n = 3
# arr = []
# for i in range(n):
#     arr.append(list(map(int, input("enter elements of 3x3 matrix:\n").rstrip().split())))

# print(arr)
"""

# -----------------------------------------------------------

# arr = [1,1,0,-1,-1]
# positive_count = 0
# negative_count = 0
# zero_count = 0
# for i in arr:
#     if i>0:
#         positive_count += 1
#     elif i<0:
#         negative_count += 1
#     else:
#         zero_count += 1

# print(f"{positive_count/len(arr):.6f}")
# print(f"{negative_count/len(arr):.6f}")
# print(f"{zero_count/len(arr):.6f}")

""" 
print(":.6f".format(positive_count/len(arr)))
print(":.6f".format(negative_count/len(arr)))
print(":.6f".format(zero_count/len(arr)))
a = 2/5
print(f"{a:.6f}")
"""

# ------------------------------------------------------

# n = int(input("Enter no. of rows/columns: "))
# space = " "
# for i in range(n):
#     print(space*(n-i-1)+"#"*(i+1))

# -----------------------------------------------

# Given five positive integers, find the minimum and maximum values that can be calculated by summing exactly four of the five integers. Then print the respective minimum and maximum values as a single line of two space-separated long integers.

# a = [1,3,5,7,9]
# # min(a)
# # max(a)
# sum = 0
# for i in a:
#     sum += i
# min_sum = sum - max(a)
# max_sum = sum - min(a)
# # # print(a[:len(a)-1])

# print(min_sum,max_sum)

# -----------------------------------------------------------------------------------------

# You are in charge of the cake for a child's birthday. You have decided the cake will have one candle for each year of their total age. They will only be able to blow out the tallest of the candles. Count how many candles are tallest.

# candles = [4,4,1,3]
# # print(candles.count(4))
# h = max(candles) #find the tallest hight of the candle from the list
# print(candles.count(h)) #how many candles are there with the max hight, count them

# -----------------------------------------------------------------------------------------
"""
s = "07:05:45PM"
# print(s[-2:]) -- PM
# print(s.split(":")) -- ['07', '05', '45PM']
# sl = s.split(":")
if s[-2:] == "AM" and s[:2] == "12":
    s[:2] = "00" 
elif s[-2:] == "AM":
    s = s[:-2]
elif s[-2:] == "PM" and s[:2] == "12":
    s = s[:-2]
elif s[-2:] == "PM":
    new = str(int(s[:2]) + 12)
    s = new + s[2:-2]

print(s)
# new_s = ""
# for ele in sl:
#     new_s += str(ele)
# print(new_s[:-2])
"""
def timeConversion(s):
    if s[-2:] == "AM" and s[:2] == "12":
        new = "00" + s[2:-2]
        return  new
    elif s[-2:] == "AM":
        new = s[:-2]
        return new
    elif s[-2:] == "PM" and s[:2] == "12":
        new = s[:-2]
        return new
    elif s[-2:] == "PM":
        # new = str(int(s[:2]) + 12)
        new = str(int(s[:2]) + 12) + s[2:-2]
        return new

s = input()
result = timeConversion(s)
print(result)
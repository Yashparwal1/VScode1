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
# def timeConversion(s):
#     if s[-2:] == "AM" and s[:2] == "12":
#         new = "00" + s[2:-2]
#         return  new
#     elif s[-2:] == "AM":
#         new = s[:-2]
#         return new
#     elif s[-2:] == "PM" and s[:2] == "12":
#         new = s[:-2]
#         return new
#     elif s[-2:] == "PM":
#         # new = str(int(s[:2]) + 12)
#         new = str(int(s[:2]) + 12) + s[2:-2]
#         return new

# s = input()
# result = timeConversion(s)
# print(result)

# -----------------------------------------------------------------------
# def gradingStudents(grades):
#     roundoff = []
#     for grade in grades:
#         if grade <= 37:
#             roundoff.append(grade)
#             continue
#         elif grade % 5 == 0:
#             roundoff.append(grade)
#             continue
#         else:
#             var_grade = grade
#             for i in range(4):
#                 var_grade = grade + (i+1)
#                 if var_grade%5 == 0:
#                     if (var_grade-grade) < 3:
#                         grade = var_grade
#                     roundoff.append(grade)
#                 else:
#                     continue
#     return roundoff

# grades = [71,72,73,74,75]
# result = gradingStudents(grades)
# print(result)

# -----------------------------------------------------------------------

""" 
house --> s______t
tree --> a , b
fruits --> m - apples , n - oranges
apples = [] , oranges = [] --> distances of falling
distance --> d

tree        /```HOUSE```\           tree
 a          s           t            b
 
"""

# def func(s,t,a,b,apples,oranges):
#     # m = 3
#     # n = 2
#     apple_count = 0
#     orange_count = 0
#     for d in apples:
#         if (a+d >= s):
#             apple_count += 1
#         else:
#             continue
#     for d in oranges:
#         if (b+d <= t and b+d >= s):
#             orange_count += 1
#         else:
#             continue
#     print(apple_count)
#     print(orange_count)
# func(7,10,4,12,[2,3,-4],[3,-2,-4])
# func(7,11,5,15,[-2,2,1],[5,-6])

# --------------------------------------------------------------------
#kangaroo start jumping at diff. locations and meet at certain point after some jumps ? YES : NO 
# def kangaroo(x1, v1, x2, v2):
#     equal = 0
#     for i in range(10000):
#         x1 += v1
#         x2 += v2
#         if x1 == x2:
#             equal = 1
#     if equal == 1:
#         return "YES"
#     else:
#         return "NO"
    
# result = kangaroo(0,2,5,3)
# print(result)

# ---------------------------------------------------------------------
""" 
There will be two arrays of integers. Determine all integers that satisfy the following two conditions:
- The elements of the first array are all factors of the integer being considered
- The integer being considered is a factor of all elements of the second array
These numbers are referred to as being between the two arrays. Determine how many such numbers exist.
 """
# def getTotalX(a, b):
#     #numbers between two arrays -- between max(a) and min(b)
#     first = []
#     second = []
#     final1 = []
#     final2 = []
#     for i in range(max(a), min(b)+1): # multiples of first array
#         for e in a:
#             if i%e == 0:
#                 first.append(i)
#     for i in first: #duplicates to add in final
#         if first.count(i) == len(a):
#             final1.append(i)
#     ans1 = list(set(final1))
#     print(ans1)
#     # print(first)
#     # print(final1)
#     for i in range(max(a),min(b)+1): #factors of second array
#         for e in b:
#             if e%i == 0:
#                 second.append(i)
#     for i in second: # duplicates to add in final
#         if second.count(i) == len(b):
#             final2.append(i)
#     # print(second)
#     # print(final2)
#     ans2 = list(set(final2))
#     print(ans2)
#     count = 0
#     for f in range(max(a),min(b)+1):
#         if f in ans1 and f in ans2:
#             count += 1
#     print(count)

#     """ Shorter  version
#     for i in range(4,17):
#         if all(i%e == 0 for e in a) and all(e%i==0 for e in b): # all e's should be divisible by i, that i will be printed
#             ans.append(i)
#     print(len(ans))
#     """
# a = [2,4]
# b = [16,32,96]
# getTotalX(a,b)

# ================================================================================

"""Maria plays college basketball and wants to go pro. Each season she maintains a record of her play. She tabulates the number of times she breaks her season record for most points and least points in a game. Points scored in the first game establish her record for the season, and she begins counting from there.

game    |0   1   2   3   4   5   6   7   8       
score   |10  5   20  20  4   5   2   25  1
max     |10  10 `20` 20  20  20  20 `25` 25
min     |10 `5`  5   5  `4`  4  `2`  2  `1`

if score in game 2 < socre in game 1
    if score in game 2 < min in game 1
        low.append(score)
elif score in game 2 > score in game 1
    if score in game 2 > max in game 1
        high.append(score)

"""

# def breakingRecords(scores):
#     high = []    
#     low = []
#     low_count = 0
#     high_count = 0
#     high.append(scores[0])
#     low.append(scores[0])
#     for game in range(len(scores)-1):
#         # print(scores[game+1])
#         if scores[game+1] < scores[game] and scores[game+1] < low[game]:
#             low.append(scores[game+1])
#             low_count += 1
#         else:
#             low.append(low[game])

#         if scores[game+1] > scores[game] and scores[game+1] > high[game]:
#             high.append(scores[game+1])
#             high_count += 1
#         else:
#             high.append(high[game])

#     print(high)
#     print(low)
#     return [high_count,low_count]

# scores = [3, 4, 21, 36, 10, 28, 35, 5, 24, 42]
# # scores = [10, 5, 20, 20, 4, 5, 2, 25, 1]
# result = breakingRecords(scores)
# print(result)

# ==============================================================================

"""
Two children, Lily and Ron, want to share a chocolate bar. Each of the squares has an integer on it.
Lily decides to share a contiguous segment of the bar selected such that:
- The length of the segment matches Ron's birth month, and,
- The sum of the integers on the squares is equal to his birth day.

link: https://www.hackerrank.com/challenges/the-birthday-bar/problem?isFullScreen=true&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen&h_r=next-challenge&h_v=zen

"""

# def birthday(s,d,m):
#     count,sum = 0,0
#     if len(s) == 1 and s[0] == d:
#         count += 1
#         return count
#     for i in range(len(s)-(m-1)):
#         for x in range(m):
#             sum += s[i+x]
#             # if s[i]+s[i+1] == d:
#         if sum == d:
#             # print(s[i],s[i+1])
#             count += 1
#         # print(sum)
#         sum = 0
#     return count

# s = [4]
# # s = [2,2,1,3,2]
# # s = [2,3,4,4,2,1,2,5,3,4,4,3,4,1,3,5,4,5,3,1,1,5,4,3,5,3,5,3,4,4,2,4,5,2,3,2,5,3,4,2,4,3,3,4,3,5,2,5,1,3,1,4,2,2,4,3,3,3,3,4,1,1,4,3,1,5,2,5,1,3,5,4,3,3,1,5,3,3,3,4,5,2]
# # s = [5,1,2,4,4,2,4,2,2,5,1,4,3,1,1,1,2,1,4,1]
# d = 4
# m = 1
# # print(len(s))
# result = birthday(s,d,m)
# print(result)
"""    
s = [4]
for i in range(len(s)-1):
    print(i) 
"""

# =========================================================================
# Given an array of integers and a positive integer k, determine the number of (i,j) pairs where i<j and ar[i] + ar[j] is divisible by k.
# i < j and ar[i] + ar[j] % k == 0 

# def divisibleSumPairs(n, k, ar):
#     count = 0
#     for i in range(n):
#         for j in range(n):
#             if i<j and (ar[i]+ar[j]) % k==0:
#                 print(ar[i],ar[j])
#                 count += 1
#     return count
# n = 6
# k = 3
# # ar = [1,2,3,4,5,6]
# ar = [1,3,2,6,1,2]
# result = divisibleSumPairs(n,k,ar)
# print(result)

# ==========================================================================

# def birds(arr):
#     # counted = []
#     # freq = {}
#     # for i in arr:
#     #     if i in counted:
#     #         continue
#     #     else:
#     #         print(i,end=" ")
#     #         print(arr.count(i))
#     #         freq[i]=arr.count(i)
#     #         counted.append(i)
#     # print("counted = ",counted) #[1,2,3]
#     # print("Frq = ",freq) #{1: 2, 2: 2, 3: 1}
#     # final = []
#     # for key,value in freq.items():
#     #     if value == max(freq.values()): #if value is maximum, add respective key to a list then find min
#     #         final.append(key)
#     # print(min(final))

#     """2nd approach"""

#     # for bird in arr:
#     #     if bird in freq:
#     #         freq[bird] += 1 #if yes then increase its count by 1 (count is stored as value)
#     #     else:
#     #         freq[bird] = 1 #if not then store that bird with count 1
#     #         #and if next time this bird come, its already in freq and if-block will increase its count
#     # max_count = max(freq.values())
#     # #now find which key has this max_count value
#     # ids = []
#     # for key,value in freq.items():
#     #     if value == max_count: #id 1 and id 2 has max_count value
#     #         ids.append(key) #add those keys in ids list then find the min value acc. to question
#     # print(min(ids))

# arr = [1,1,2,2,3]
# birds(arr)
"""
# Frq =  {1: 2, 2: 2, 3: 1}
# val = max(Frq.values())
# print(val)
"""

# ==================================================================================

# year = 1800
# leap = "12.09."+str(year)
# noleap = "13.09."+str(year)
# # if year == 1918:
# if year < 1918:
#     if year%4==0:
#         print(leap)
#     else:
#         print(noleap)
# elif year == 1918:
#     print()
# else:
#     if year%4==0:
#         if year%100==0:
#             if year%400==0:
#                 #yes - 256th day is 12.09.2017
#                 print("12.09."+str(year))
#                 # if year ==`` 1918:
#             else:
#                 #no - 256th day is 13.09.2017
#                 print("13.09."+str(year))
#         else:
#             # yes - 256th day is 12.09.2017
#             print("12.09."+str(year))
#     else:
#         pass
#         #no - 256th day is 12.09.2017
#         print("13.09."+str(year))

#=================================================================================

# Two friends Anna and Brian, are deciding how to split the bill at a dinner. Each will only pay for the items they consume. Brian gets the check and calculates Anna's portion. You must determine if his calculation is correct.

# def bonAppetit(bill, k, b):
#     sum = 0
#     for price in bill:
#         sum += price
#     sum -= bill[k]
#     sum /= 2
#     if b>sum:
#         back = b-sum
#         print(back)
#     else:
#         print("Bon Appetit")
# bill = [2,4,6]
# k = 2 #index 1 in bill
# b = 3 #paid by anna
# bonAppetit(bill, k, b)

# ===================================================================

# def missingCharacters(s):
#     digits = []
#     letters  = []
#     final = ''
#     for i in s:
#         if i.isdigit():
#             digits.append(int(i))
#         else:
#             letters.append(i)
#     # print(digits)
#     # print(letters)
#     for digit in range(10):
#         if digit not in digits:
#             final += str(digit)
#     # print(final)
    
#     alphabet = "abcdefghijklmnopqrstuvwxyz"
#     for letter in alphabet:
#         if letter not in letters:
#             final += letter
#     return final
# s = "8hypotheticall024y6wxz"
# result = missingCharacters(s)
# print(result)

# ===================================================================
# class Car:
#     def __new__(self,max_speed,speed_unit):
#         return "Car with the maximum speed of {} {}".format(max_speed,speed_unit)
# class Boat:
#     def __new__(self,max_speed):
#         return "Boat with the maximum speed of {} knots".format(max_speed)

# max_speed = 20
# speed_unit = "km/h"
# vehicle = Car(max_speed,speed_unit)
# print(vehicle)

# ===================================================================

# def sockMerchant(n, ar):
#     pair = {}
#     for i in ar:
#         if i in pair:
#             pair[i] += 1
#         else:
#             pair[i] = 1
#     print(pair) 
#     #now find the pairs
#     final = 0
#     for value in pair.values():
#         pair = value//2 #if value is completely divisible then pair is complete like 4->2, 6->3 BUT if value is odd, remiander will be 1 and will be discarded, like 5->2 
#         final += pair #add each pair to final
#     print(final)
# ar = [1,2,1,2,1,3,2]
# ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]
# n = len(ar)
# sockMerchant(n,ar)

# ===================================================================
"""
A teacher asks the class to open their books to a page number. A student can either start turning pages from the front of the book or from the back of the book. They always turn pages one at a time. When they open the book, page 1 is always on the right side:

image - \  | 1 \ ---> \ 2 | 3 \ ---> \ 4 | 5 \ ---> \ 6 |  \

When they flip page 1, they see pages 2 and 3. Each page except the last page will always be printed on both sides. The last page may only be printed on the front, given the length of the book. If the book is  pages long, and a student wants to turn to page p, what is the minimum number of pages to turn? They can start at the beginning or the end of the book.

Given n and p, find and print the minimum number of pages that must be turned in order to arrive at page p.
eg. n=5 , p=3
image - \  | 1 \ ---> \ 2 | 3 \ ---> \ 4 | 5 \
"""

# def pageCount(n, p):
#     # first find the distance of p from startand end
#     start = p-1
#     end = n-p
#     begin = n if end<start or end==start else 1  #begin turning pages from start or end?
#     # print(start,end,begin)
#     if begin == 1:
#         print(p//2)
#     else:
#         if end == 1 and n%2==0:  #if turning from n --> check if n is 
#             print(end)
#         else:
#             print(end//2)
# n = 6
# p = 4
# pageCount(n, p)

# =======================================================================
"""
An avid hiker keeps meticulous records of their hikes. For every step it was noted if it was an uphill,U, or a downhill, D step. Hikes always start and end at sea level, and each step up or down represents a 1 unit change in altitude. We define the following terms:

A mountain is a sequence of consecutive steps above sea level, starting with a step up from sea level and ending with a step down to sea level.
A valley is a sequence of consecutive steps below sea level, starting with a step down from sea level and ending with a step up to sea level.
Given the sequence of up and down steps during a hike, find and print the number of valleys walked through.
"""
# def countingValleys(steps, path):
#     sea = 0
#     count = 0
#     for i in range(steps):
#         if path[i] == 'D':
#             sea -= 1
#         elif path[i] == 'U':
#             sea += 1
#         if sea==-1 and path[i+1]=='U':
#             count += 1
#     print(count)

# path = "UDDDUDUU"
# steps = len(path)
# countingValleys(steps,path)
"""
_/\      _
   \    /
    \/\/
"""

# ======================================================================
# A person wants to determine the most expensive computer keyboard and USB drive that can be purchased with a give budget. Given price lists for keyboards and USB drives and a budget, find the cost to buy them. If it is not possible to buy both items, return -1.

# def getMoneySpent(keyboards, drives, b):
#     price = 0
#     for k in keyboards:
#         for d in drives:
#             if (k+d) <= b and (k+d)>=price:
#                 price = k+d
#     if price == 0:
#         print(-1)
#     else:
#         print(price)

# keyboards = [40,50,60]
# drives = [5,8,12]
# b = 60
# moneySpent = getMoneySpent(keyboards, drives, b)

# ======================================================================

# Two cats and a mouse are at various positions on a line. You will be given their starting positions. Your task is to determine which cat will reach the mouse first, assuming the mouse does not move and the cats travel at equal speed. If the cats arrive at the same time, the mouse will be allowed to move and it will escape while they fight.

# x = 1
# y = 3
# z = 2
# c1 = abs(x-z)
# c2 = abs(y-z)

# if c1<c2:
#     print("cat A")
# elif c1>c2:
#     print("cat B")
# else:
#     print("Mouse C")

# ==========================================================
#find the minimum cost to convert a matrix into magic matrix or square into magic square

# s = [
#     [5, 3, 4],
#     [1, 5, 8],
#     [6, 4, 2]
# ]

# magic_squares = [
#         [[8, 1, 6], [3, 5, 7], [4, 9, 2]],
#         [[6, 1, 8], [7, 5, 3], [2, 9, 4]],
#         [[4, 9, 2], [3, 5, 7], [8, 1, 6]],
#         [[2, 9, 4], [7, 5, 3], [6, 1, 8]],
#         [[8, 3, 4], [1, 5, 9], [6, 7, 2]],
#         [[4, 3, 8], [9, 5, 1], [2, 7, 6]],
#         [[6, 7, 2], [1, 5, 9], [8, 3, 4]],
#         [[2, 7, 6], [9, 5, 1], [4, 3, 8]]
# ]
# min_cost = float('inf')
# for mag in magic_squares:
#     # print(mag)
#     cost = 0
#     for i in range(3): # i is 0,1,2 ---> [8, 1, 6], [3, 5, 7], [4, 9, 2]
#         for j in range(3): # j is 0,1,2 ---> 8,1,6 
#         # print(mag) #or print(magic_squares[i])
#             # print(mag[i]) 
#             # print(mag[j])
#             # print(f"{s[i][j]}-{mag[i][j]} = {abs(s[i][j]-mag[i][j])}")
#             cost += abs(s[i][j] - mag[i][j])
#     min_cost = min(min_cost,cost)
#     # print('\n')
# print(min_cost)

# ============================================================================
# Given an array of integers, find the longest subarray where the absolute difference between any two elements is less than or equal to 1.
"""
APPROACH: first sort ---> count first element and count first+1 element ---> add them, this is the occurance of elements whose abs is 1. Since we sorted it already, so 1st element will always be smaller and when we add 1 in it, the element becomes one of the greater elements then 1st element. ---> store the occurance and find max from them 
"""

# a = [4,6,5,3,3,1]
# a = [1, 2, 2, 3, 1, 2]
# a.sort()
# occur = []
# for i in a:
#     count_i = a.count(i)
#     count_j = a.count(i+1)
#     occur.append((count_i+count_j))

#     # for j in range(i+1,len(a)):
#     #     if abs(a[i]-a[j])<=1:
#     #         count += 1
#     # occur.append(count)

# print(max(occur))

# =============================== INCOMPLETE =========================================
"""
The ranked players will have ranks 1, 2, 2, and 3, respectively. If the player's scores are 70, 80 and 105, their rankings after each game are 4th, 3rd and 1st. Return [4,3,1].

Function Description
"""
# new = {}
# player = [5,25,50,120]
# ranked = [100,100,50,40,40,20,10]
# uranked = list(set(ranked))
# uranked.sort(reverse=True)
# print(uranked)
# rank = 1
# new[rank] = ranked[0]
# for i in range(1,len(ranked)):
#     if ranked[i] < ranked[i-1]:
#         rank += 1
#         new[rank]=ranked[i]
#     elif ranked[i] == ranked[i-1]:
#         new[rank]=ranked[i]
# print(new)

# for i in player:
    # for k in new:
    # print(new[k])
        # if i > new[k]:
#             pass # insert before new[k]
#         elif i == new[k]:
#             pass 
#         else:
#             pass


# mykeys = ['Name', 'Age', 'Class']
# mydict = {'Name': 'Zara', 'Age': 7, 'Class': 'First'} # order doesn't matter

# k, v = 'Phone', '123-456-7890'

# mykeys.insert(mykeys.index('Name')+1, k)
# mydict[k] = v

# for k in mykeys:
#     print(f'{k} => {mydict[k]}')

# ======================================================================================

"""
A video player plays a game in which the character competes in a hurdle race. Hurdles are of varying heights, and the characters have a maximum height they can jump. There is a magic potion they can take that will increase their maximum jump height by 1 unit for each dose. How many doses of the potion must the character take to be able to jump all of the hurdles. If the character can already clear all of the hurdles, return 0.
"""

# k = 4
# height = [1,6,3,5,2]
# if k>=max(height):
#     return 0
# else:
#     final = max(height)-k
#     return final

# =======================================================================
""" 
When a contiguous block of text is selected in a PDF viewer, the selection is highlighted with a blue rectangle. In this PDF viewer, each word is highlighted independently. For example:
    yash par wal  [assume these highlighted]
There is a list of 26 character heights aligned by index to their letters. For example, 'a' is at index 0 and 'z' is at index 25. There will also be a string. Using the letter heights given, determine the area of the rectangle highlight in mm2 assuming all letters are 1mm wide.
z=5, a=1, b=2, a=1, so max is z=5 and zaba=4mm so area = 4mm x 1mm for word and then multiply by 5 (the max mm of a word in zaba which is z)

"""

# h = [1, 3, 1, 3, 1, 4, 1, 3, 2, 5, 5, 5, 5, 5, 5, 5, 5, 5, 5 ,5, 5, 5, 5, 5, 5, 5]
# word = "zaba"

# alpha = "abcdefghijklmnopqrstuvwxyz"
# heights = []
# for letter in word:
#     for i in range(len(alpha)):
#         if letter == alpha[i]:
#             heights.append(h[i])
# print(heights)
# area = len(word)*max(heights)
# print(area)

# for i in range(26):
#     print(alpha[i])

# ===================================================================================
""" 
The Utopian Tree goes through 2 cycles of growth every year. Each spring, it doubles in height. Each summer, its height increases by 1 meter.
A Utopian Tree sapling with a height of 1 meter is planted at the onset of spring. How tall will the tree be after n growth cycles?

Period  Height
0          1
1          2
2          3
3          6
4          7
5          14

"""
# # spring - x*2 --> Summer - (x*2)+1
# def tree():
#     t = 0
#     height = 1
#     if t==0:
#         return height
#     for i in range(t):
#         if i%2==0:
#             height = height * 2
#         else:
#             height = height + 1
#         print(height)    

# result = tree()
# print(result)

# ============================================================================

# def professor():
#     count = 0
#     # k = 3
#     # a = [-2,-1,0,1,2]
#     a = [-3,-1,4,2]
#     k = 3
#     for i in a:
#         if i<=0:
#             count += 1
#     if count >= k:
#         return 'YES'
#     else:
#         return 'NO'

# result = professor()
# print(result)

# ===========================================================================
"""
Lily likes to play games with integers. She has created a new game where she determines the difference between a number and its reverse. For instance, given the number 12, its reverse is 21. Their difference is 9. The number 120 reversed is 21, and their difference is 99.

She decides to apply her game to decision making. She will look at a numbered range of days and will only go to a movie on a beautiful day.
"""
# def beautifulDays(i, j, k):
#     count = 0
#     for x in range(i,j+1):
#         num = x-int(str(x)[::-1])
#         print("num",num)
#         if num%k==0:
#             count+=1
#         print("count",count)
#     return count

# i = 20
# j = 23
# k = 6
# result = beautifulDays(i,j,k)
# print(result)

# =======================================================================

""" 
#Strange Advertising


"""
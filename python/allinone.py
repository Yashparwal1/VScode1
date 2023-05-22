# numbers = []

# for i in range(5):
#     num = int(input(f"Enter number {i+1}: "))
#     numbers.append(num)

# largest = numbers[0]
# smallest = numbers[0]
# for num in numbers:
#     if num > largest:
#         largest = num

# for num in numbers:
#     if num < smallest:
#         smallest = num
        
# print(f"The largest number is {largest}")
# print(f"The smallest number is {smallest}")


# def numb():
#     for i in range(5):
#         n = int(input("Enter number: "))
#         print(n)

# numb()

# ==================================================================================
# QUESTION: Find the Looser - GfG

win = []
lose = []
n = 5
k = 2
steps = k
i = 1
for f in range(1,n+1): # 1,2,3
    if i >= n: # 7>5, 8>5
        i=(i-n)
        if i in win:
            for l in range(1,n+1):
                if l not in win:
                    lose.append(l)
            break
    ball = i # 1,3,2
    win.append(ball)
    k = steps*f  # 2,4,6
    i = i+k  # 3,7,8

# print(win)
print(lose)

# ball = 1
# ball = ball+k
# ball = ball+(k*2)

# ==================================================================================



# def func(*args):
#     sum = 0
#     for i in args:
#         if type(i) == int:
#             sum = sum+i
#     print(sum)


# func(1,2,"hello",True,3,"kid")

#a = 100
#def func():
#    a = 200
#    return
#    print("a = ",a)
#func()
#print("a = ",a)

# output??
#------------------------------------------------------------------------
# alpha = 0
# with open("dcs.txt", "w") as file:
#     file.write(input("Enter some lines: "))
# file.close()

# file = open("dcs.txt", "r")
# data = file.read()
# print(data)

# for i in data:
#     if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
#         alpha += 1
# print(f"Total no. of alphabets in the stentence are: {alpha}")
# for i in data:
#     if i >= 'a' and i <= 'z' or i >= 'A' and i <= 'Z':
#         data = data.replace(i,'')
# print(f"after removing all the alphabest, remaining chars are: {data}")

for i in range(0x41,0x5b):
    print(f"{chr(i )}",end="")
print()
for i in range(0x61,0x7b):
    print(f"{chr(i )}",end="")
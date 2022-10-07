# 56 + 9 = 77 , 45 * 3 = 555, 56/6 = 4 
print("choose your operator")
op = input()
print("enter greater number : ")
num1 = int(input())
print("enter smaller number : ")
num2 = int(input())

if op=='+' and num1==56 and num2==9:
        print(num1, '+', num2, '=', 77)
elif op=='-' and num1==100 and num2 == 50:
        print(num1, '-', num2, '=', 10 ) 
elif op=='*' and num1==45 and num2==3:
        print(num1, '*', num2, '=', 555)
elif op=='/' and num1==56 and num2==6:
        print(num1, '/', num2, '=', 4)
elif op=='+':
        print(num1 + num2)
elif op=='-':
        print(num1 - num2)
elif op=='*':
        print(num1 * num2)
elif op=='/':
        print(num1 / num2)


else:
        print("invalid entry")
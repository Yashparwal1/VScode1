# main script

code = """
print("Running inner script")
a = input()
b = input()
print("Result:", a + b)
print("Inner script finished")
"""

exec(code)

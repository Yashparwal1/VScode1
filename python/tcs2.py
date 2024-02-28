import re

def is_luhn_valid(number):
    digits = [int(digit) for digit in number[::-1]]
    checksum = sum(digits[0::2] + [sum(divmod(d * 2, 10)) for d in digits[1::2]])
    return checksum % 10 == 0

def extract_sensitive_data(text):
    # Regex here
    ssn_pattern = re.compile(r'\b[0-9]{3}-[0-9]{2}-[0-9]{4}\b')
    credit_card_pattern = re.compile(r'\b[0-9]{16}\b')
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    phone_number_pattern = re.compile(r'\(\d{3}\) [0-9]{3}-[0-9]{4}\b')
    # phone_number_pattern = re.compile(r'\b[0-9]{3}-[0-9]{4}\b')

    # Finding all matches in the text from file
    ssn_matches = ssn_pattern.findall(text)
    credit_card_matches = []
    for i in credit_card_pattern.finditer(text):
        credit_card_number = i.group()
        if is_luhn_valid(credit_card_number):
            credit_card_matches.append(credit_card_number)
    email_matches = email_pattern.findall(text)
    phone_number_matches = phone_number_pattern.findall(text)

    print(ssn_matches)
    print(credit_card_matches)
    print(email_matches)
    print(phone_number_matches)
    
    #combining all
    sensitive_data = ssn_matches + credit_card_matches + email_matches + phone_number_matches

    #last character of each sensitive data in their original order
    last_chars = []
    for data in sensitive_data:
        last_chars.append(data[-1])

    return last_chars

file_path = 'D:\\VScode\\python\\file.txt'
with open(file_path, 'r') as file:
    file_content = file.read()

result = extract_sensitive_data(file_content)
print(result)

str = " "
for i in result:
    str += i
print(str)

""" 
(234) 123-7890
(123) 543-5678
(876) 51-12 ----------x
(890) 123-4567
(543) 654-3210
(678) 9012345 ----------x
(987) 8769876 ----------x
(876) 88-44 ----------x
(22) 243-1139 ----------x
(980) 68-9587 ----------x
(876) 543-2109 
(444) 5556666 ----------x
(091) 453-67102 -----------x

HQ8{70013790134123307eanvkus08709}
 """
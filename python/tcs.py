from ast import Str
import re

def extract_sensitive_data(text):
    # regex here
    ssn_pattern = re.compile(r'\b\d{3}-\d{2}-\d{4}\b')
    credit_card_pattern = re.compile(r'\b\d{16}\b')
    email_pattern = re.compile(r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b')
    phone_number_pattern = re.compile(r'\b\(\d{3}\) \d{3}-\d{4}\b')

    # Finding all matches in the text from file
    ssn_matches = ssn_pattern.findall(text)
    credit_card_matches = credit_card_pattern.findall(text)
    email_matches = email_pattern.findall(text)
    phone_number_matches = phone_number_pattern.findall(text)

    print(ssn_matches)
    print(credit_card_matches)
    print(email_matches)
    print(phone_number_matches)

    # Combine all matches
    sensitive_data = ssn_matches + credit_card_matches + email_matches + phone_number_matches

    # Extract the last character of each sensitive data type in their original order
    last_chars = [data[-1] for data in sensitive_data]

    return last_chars

# Example usage
text_file_content = """

"""

result = extract_sensitive_data(text_file_content)
print("Last characters of sensitive data:", result)

str = " "
for i in result:
    str += i
print(str)
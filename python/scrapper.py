import re
import csv
import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin
from selenium import webdriver

def scrape_page(url):
    response = requests.get(url)
    if response.status_code == 200:
        return BeautifulSoup(response.text, 'html.parser')
    else:
        return None

# def scrape_page(url):
#     options = webdriver.ChromeOptions()
#     options.add_argument("--headless")  # Run Chrome in headless mode (no GUI)
#     driver = webdriver.Chrome(options=options)
#     driver.get(url)
#     page_source = driver.page_source
#     driver.quit()
#     return BeautifulSoup(page_source, 'html.parser')

def find_internal_links(soup, base_url):
    links = []
    for a in soup.find_all('a',href=True):
        link = urljoin(base_url, a['href'])
        if link.startswith(base_url):
            links.append(link)
    links = list(set(links))
    return links

def extract_emails_and_first_names(soup):
    email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
    paragraphs = soup.find_all(['td','p','div','span'])
    # print(paragraphs)
    paragraph_texts = ' '.join([p.get_text() for p in paragraphs])
    # print(paragraph_texts)
    emails = re.findall(email_pattern,paragraph_texts)
    # print(emails)
    first_name = [email.split('@')[0].split('.')[0] for email in emails]
    first_name = [email.split('@')[0] for email in emails]
    # print(first_name)
    return list(zip(first_name,emails))

def main():
    # base_url = "https://suryahospitals.com/"
    base_url = input("Enter the url: ")
    visited_links = set()
    links_to_visit = [base_url]
    with open('email_and_first_names.csv','w',newline='') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['First Name', 'Email'])

        while links_to_visit:
            link = links_to_visit.pop(0)
            if link not in visited_links:
                print(f"Scrapping {link}...")
                soup = scrape_page(link)
                print(soup) #for large source code, it doesnt scrape whole code 
                if soup:
                    visited_links.add(link)
                    # links_to_visit.extend(find_internal_links(soup, base_url))
                    # print(links_to_visit) #got uniques internal links from the source code
                    emails_and_first_names = extract_emails_and_first_names(soup)
                    # print(emails_and_first_names)
                    for first_name, email in emails_and_first_names:
                        # print(first_name,email)
                        writer.writerow([first_name,email])

if __name__ == "__main__":
    main()

# import re
# import csv
# import requests
# from bs4 import BeautifulSoup
# from urllib.parse import urljoin
# import sys
# from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QVBoxLayout, QWidget, QLabel, QFileDialog, QLineEdit

# class EmailScraperApp(QMainWindow):
#     def __init__(self):
#         super().__init__()
#         self.init_ui()

#     def init_ui(self):
#         self.setWindowTitle("Email Scraper")
#         self.setGeometry(100, 100, 800, 600)

#         self.url_input = QLineEdit()
#         self.text_edit = QTextEdit()
#         self.start_button = QPushButton("Start Scraping")
#         self.save_button = QPushButton("Save to CSV")

#         layout = QVBoxLayout()
#         layout.addWidget(QLabel("Enter URL:"))
#         layout.addWidget(self.url_input)
#         layout.addWidget(QLabel("Scraped Email Addresses:"))
#         layout.addWidget(self.text_edit)
#         layout.addWidget(self.start_button)
#         layout.addWidget(self.save_button)

#         container = QWidget()
#         container.setLayout(layout)

#         self.setCentralWidget(container)

#         self.start_button.clicked.connect(self.start_scraping)
#         self.save_button.clicked.connect(self.save_to_csv)

#         self.scraped_data = []

#     def scrape_page(self, url):
#         response = requests.get(url)
#         if response.status_code == 200:
#             return BeautifulSoup(response.text, 'html.parser')
#         else:
#             return None

#     def find_internal_links(self, soup, base_url):
#         links = []
#         for a in soup.find_all('a', href=True):
#             link = urljoin(base_url, a['href'])
#             if link.startswith(base_url):
#                 links.append(link)
#         links = list(set(links))
#         return links

#     def extract_emails_and_first_names(self, soup):
#         email_pattern = r'\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b'
#         paragraphs = soup.find_all(['td','p','div','span'])
#         paragraph_texts = ' '.join([p.get_text() for p in paragraphs])
#         emails = re.findall(email_pattern, paragraph_texts)
#         first_name = [email.split('@')[0] for email in emails]
#         self.scraped_data = list(zip(first_name, emails))
#         self.update_text_edit()

#     def update_text_edit(self):
#         text = '\n'.join([f"{first_name}: {email}" for first_name, email in self.scraped_data])
#         self.text_edit.setPlainText(text)

#     def start_scraping(self):
#         base_url = self.url_input.text()  # Get URL from the input field
#         if not base_url:
#             return

#         visited_links = set()
#         links_to_visit = [base_url]

#         while links_to_visit:
#             link = links_to_visit.pop(0)
#             if link not in visited_links:
#                 print(f"Scraping {link}...")
#                 soup = self.scrape_page(link)
#                 if soup:
#                     visited_links.add(link)
#                     links_to_visit.extend(self.find_internal_links(soup, base_url))
#                     self.extract_emails_and_first_names(soup)
#         print(links_to_visit)
#     def save_to_csv(self):
#         if not self.scraped_data:
#             return

#         options = QFileDialog.Options()
#         options |= QFileDialog.ReadOnly
#         file_name, _ = QFileDialog.getSaveFileName(self, "Save to CSV", "", "CSV Files (*.csv);;All Files (*)", options=options)

#         if file_name:
#             with open(file_name, 'w', newline='') as csvfile:
#                 writer = csv.writer(csvfile)
#                 writer.writerow(['First Name', 'Email'])
#                 for first_name, email in self.scraped_data:
#                     writer.writerow([first_name, email])

# def main():
#     app = QApplication(sys.argv)
#     window = EmailScraperApp()
#     window.show()
#     sys.exit(app.exec_())

# if __name__ == "__main__":
#     main()

# """ 
# https://tips.vidalhealthtpa.com/vidalhealth/HospNetwork.htm
# https://tips.vidalhealthtpa.com/vidalhealth/searchHospitalNew.htm?inseqId=20038&stateSeq=RJ&city=&hosp=&gipsappn=
# """
# import json
# import csv

# # Read data from the JSON file
# with open('scrape.txt', 'r') as json_file:
#     data = json.load(json_file)

# # Define the CSV file name
# csv_file = 'scraped_data.csv'

# # Define the field names based on the keys in the JSON data
# field_names = data[0].keys()

# # Write data to the CSV file
# with open(csv_file, 'w', newline='') as csvfile:
#     writer = csv.DictWriter(csvfile, fieldnames=field_names)
    
#     # Write the header row
#     writer.writeheader()
    
#     # Write the data rows
#     for row in data:
#         writer.writerow(row)

# print(f'Data has been successfully written to {csv_file}')

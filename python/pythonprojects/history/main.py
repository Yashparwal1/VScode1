import os, csv
import sqlite3
import operator
from collections import OrderedDict
import matplotlib.pyplot as plt
import datetime 

# def parse(url):
# 	try:
# 		parsed_url_components = url.split('//')
# 		sublevel_split = parsed_url_components[1].split('/', 1)
# 		domain = sublevel_split[0].replace("www.", "")
# 		return domain
# 	except IndexError:
# 		print("URL format error!")

# def analyze(results):

# 	prompt = input("[.] Type <c> to print or <p> to plot\n[>] ")

# 	if prompt == "c":
# 		for site, count in sites_count_sorted.items():
# 			print(site, count)
# 	elif prompt == "p":
# 		plt.bar(range(len(results)), results.values(), align='edge')
# 		plt.xticks(rotation=45)
# 		plt.xticks(range(len(results)), results.keys())
# 		plt.show()
# 	else:
# 		print ("[.] Uh?")
# 		quit()

# Define a function to parse URLs
def parse(url):
    try:
        parsed_url_components = url.split('//')
        sublevel_split = parsed_url_components[1].split('/', 1)
        domain = sublevel_split[0].replace("www.", "")
        return domain
    except IndexError:
        print("URL format error!")

# Path to the user's history database (Chrome)
data_path = os.path.expanduser('~') + "\\AppData\\Local\\Google\\Chrome\\User Data\\Profile 2"
history_db = os.path.join(data_path, 'history')

# Connect to the Chrome history database
db = sqlite3.connect(history_db)
cursor = db.cursor()

# Execute a query to retrieve the history data
cursor.execute("SELECT datetime(visits.visit_time/1000000-11644473600, 'unixepoch') as visit_time, urls.url, urls.title FROM visits, urls WHERE visits.url = urls.id;")

# Fetch all the results
results = cursor.fetchall()

# Define the filename for the CSV file
csv_filename = "chrome_history.csv"

# Open the CSV file in write mode
with open(csv_filename, "w", newline="", encoding="utf-8") as timeline_csv:
    # Create a CSV writer
    csv_writer = csv.writer(timeline_csv)

    # Write the CSV header
    csv_writer.writerow(["Visit Time", "Website visited (Chrome)", "Title"])

    # Iterate through the history data and write it to the CSV file
    for result in results:
        visit_time = result[0]
        visit_url = result[1]
        visit_title = result[2]
        visit_title = visit_title.replace(",", "") if visit_title else ""

        # Write the data to the CSV file
        csv_writer.writerow([visit_time, visit_url, visit_title])

print("Google Chrome browsing history gathered and saved to", csv_filename)

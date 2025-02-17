from main.tools import banner
import requests
from bs4 import BeautifulSoup
import os
def get_news(url="https://thehackernews.com/"):
    os.system("clear")
    banner.main()
    banner.attack("News")
    res = requests.get(url)
    soup = BeautifulSoup(res.text, "html.parser")

    titles = []
    discription_post=[]
    urls = []
    posts = soup.find("div", class_="blog-posts clear")
    for post in posts.find_all("h2"):
        title = post.text.strip()
        if title and '<img alt="external link"' not in str(post):
            titles.append(title)
            urls.append(post.find_parent('a')['href'])
    discriptions = soup.find_all("div", class_="home-desc")
    for discription in discriptions:
        discription=discription.text.strip()
        if title and '<img alt="external link"' not in str(discription):
            discription_post.append(discription)

    dates = []
    for date in soup.find_all("span", class_="h-datetime"):
        if '<img alt="external link"' not in str(date):
            dates.append(date.text.strip()[1:])

    for title, date, url,description in zip(titles, dates, urls,discription_post):
        print(f"\n\u001b[33mTitle: {title}\u001b[0m \n\u001b[32mdescription: {description}\u001b[0m  \nDate: {date} \n\u001b[34mURL: {url}\u001b[0m \n\n")
    input("\u001b[31mPress ENTER to go back\u001b[0m")
def main():
    os.system("clear")
    banner.main()
    banner.attack("News")
    ask=input("Do you want news Date wise?(y/n)".title())
    if ask.lower()=="y" or ask.lower()=="y":
        date_user=input("Enter Date:(YYYY-MM-DD)")
        get_news(f"https://thehackernews.com/search?updated-max={date_user}T17:23:00%2B05:30&max-results=10")
    else:
        get_news()
if __name__=="__main__":
    main()
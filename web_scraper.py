import requests
from bs4 import BeautifulSoup
from urllib.parse import urljoin

# Website we want to scrape
url = "https://www.python.org"

#  Try to fetch the webpage
try:
    response = requests.get(url, timeout=10)
    response.raise_for_status()  # Raise an error if the request failed
except requests.RequestException as e:
    print(f"⚠️ Oops! Something went wrong while connecting to the website:\n{e}")
    exit()

#  Parse the HTML content using BeautifulSoup
soup = BeautifulSoup(response.text, 'html.parser')

# Let's look for the section that contains the latest Python news/events
print("✨ Latest Happenings in the Python Community:\n")

try:
    # Locate the specific section containing news/events
    news_section = soup.find('div', class_='medium-widget event-widget last')
    news_list = news_section.find_all('li')

    # Loop through each news item and extract the details
    for news in news_list:
        title = news.find('a').text.strip()  # News headline
        link = urljoin(url, news.find('a')['href'])  # Full URL to the news
        date = news.find('time').text.strip()  # Date of the event/news
        print(f"📅 {date} - 📌 {title}\n🔗 {link}\n")
except AttributeError:
    print("⚠️ Couldn't find the news section. The website structure might have changed.")

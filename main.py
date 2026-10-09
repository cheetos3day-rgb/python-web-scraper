import csv
import requests
from bs4 import BeautifulSoup


def run_scraper():
    url = "https://quotes.toscrape.com/"
    headers = {"User-Agent": "Mozilla/5.0"}

    response = requests.get(url, headers=headers)

    if response.status_code == 200:
        soup = BeautifulSoup(response.text, "html.parser")
        quotes = soup.find_all("div", class_="quote")

        data = []
        for item in quotes:
            text = item.find("span", class_="text").text
            author = item.find("small", class_="author").text
            data.append([text, author])

        with open("data.csv", "w", newline="", encoding="utf-8") as f:
            writer = csv.writer(f)
            writer.writerow(["Quote", "Author"])
            writer.writerows(data)

        print("Data scraped and saved to data.csv successfully!")
    else:
        print("Failed to load page.")


if __name__ == "__main__":
    run_scraper()
  

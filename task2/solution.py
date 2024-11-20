import requests
from bs4 import BeautifulSoup
import csv

BASE_URL = "https://ru.wikipedia.org"
CATEGORY_URL = "/wiki/Категория:Животные_по_алфавиту"


def fetch_page(session, url):
    response = session.get(url)
    response.raise_for_status()
    return response.text


def get_animals_count():
    counts = {chr(i): 0 for i in range(ord('А'), ord('Я') + 1)}
    url = BASE_URL + CATEGORY_URL

    with requests.Session() as session:
        while url:
            html = fetch_page(session, url)
            soup = BeautifulSoup(html, "html.parser")

            for item in soup.select(".mw-category-group"):
                letter = item.find("h3").text.strip()
                if letter in counts:
                    counts[letter] += len(item.select("li"))

            next_page = soup.select_one("a:-soup-contains('Следующая страница')")
            url = BASE_URL + next_page["href"] if next_page else None

    counts = {letter: count for letter, count in counts.items() if count > 0}
    return counts


def save_to_csv(counts, filename="beasts.csv"):
    with open(filename, mode="w", encoding="utf-8") as file:
        writer = csv.writer(file)
        for letter, count in sorted(counts.items()):
            writer.writerow([letter, count])


def main():
    counts = get_animals_count()
    save_to_csv(counts)
    print("Данные сохранены в beasts.csv")


if __name__ == "__main__":
    main()

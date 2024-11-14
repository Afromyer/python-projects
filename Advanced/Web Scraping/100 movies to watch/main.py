import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
URL_ORIGINAL = "https://www.empireonline.com/movies/features/best-movies-2/"
# Write your code below this line 👇

response = requests.get(URL_ORIGINAL)
response.raise_for_status()
content = response.text

soup = BeautifulSoup(content, "html.parser")

data = soup.select(selector="div > h3")
ordered_titles = []
titles = [title.getText() for title in data]
movies = titles[::-1]
with open("movies.txt", mode="w", encoding="utf-8") as file:
    for movie in movies:
        file.write(f"{movie}\n")








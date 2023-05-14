import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

# Write your code below this line 👇

responses = requests.get(URL)
website_html = responses.text

soup = BeautifulSoup(website_html, "html.parser")

# list_of_movies = soup.select(".gallery .title").__reversed__()
list_of_movies = soup.select("h3").__reversed__()   # The above and this code output the same.

# [::-1] ====   .__reversed__()   # can also use[::-1] to reverse in a list.


# Using append
# for movie in list_of_movies:
#     with open(file="Movies", mode="a", encoding="utf-8") as file:
#         file.write(f"{movie.text}\n")

# Using write only both above and these codes work the same
with open(file="Movies", mode="w", encoding="utf-8") as file:
    for movie in list_of_movies:
        file.write(f"{movie.text}\n")


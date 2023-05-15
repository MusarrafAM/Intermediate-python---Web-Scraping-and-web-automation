from bs4 import BeautifulSoup
import requests
import time

responses = requests.get("https://news.ycombinator.com/")
yc_web_page = responses.text

soup = BeautifulSoup(yc_web_page, "html.parser")

# ###########To find the first thing on yc_web_page.

# article_tag = soup.select_one(".titleline a")     # can use find here then the paranthesis will change for it.
# article_text = article_tag.getText()
# article_link = article_tag.get("href")
# article_upvote = soup.select_one("span .score").getText()
#
# print(article_text)
# print(article_link)
# print(article_upvote)


#   ------------------------Mine------------------------------------    #
text_list = []
link_list = []
score_list = []

articles = soup.select(".titleline ")

# Get all text
for article in articles:
    text_list.append(article.select_one("a").getText())     # Can use print(article.find("a").getText())

    # Get all Link
    link_list.append(article.select_one("a").get("href"))


# Get all scores
scores_tag = soup.select("span .score")
for score in scores_tag:
    score_list.append(int(score.getText().split()[0]))


# print(text_list)
# print(link_list)
# print(score_list)

# -------------Get above 3 using list comprehension.
# text_list = [article.select_one("a").getText() for article in articles]
# link_list = [article.select_one("a").get("href") for article in articles]
# score_list = [int(score.getText().split()[0]) for score in scores_tag]

high_score = max(score_list)
index = score_list.index(high_score)
print(f"high score text: {text_list[index]}")
print(f"high score link: {link_list[index]}")

time.sleep(5)



# ----------------- Basic ------------------------
# with open("website.html", encoding="utf8") as file:
#     contents = file.read()


# soup = BeautifulSoup(contents, "html.parser")
# print(soup.title)
# print(soup.title.string)

# all_anchor_tags =soup.find_all(name="a")
# print(all_anchor_tags)

# for tag in all_anchor_tags:
#     print(tag.getText())


# Search by id
# heading = soup.find(name="h1", id="name")
# print(heading)

# Search by class
# section_heading = soup.find(name="h3", class_="heading")
# print(section_heading)

#
# company_url = soup.select_one(selector="p a")
# print(company_url)

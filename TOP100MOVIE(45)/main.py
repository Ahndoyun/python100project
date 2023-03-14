from bs4 import BeautifulSoup
import lxml

with open ("D:/안도윤/2. 3월/vscode/python100project/DAY45/website.html") as file:
    contents = file.read()

soup = BeautifulSoup(contents, "html.parser")

all_anchor_tags = soup.find_all(name="a")
print(all_anchor_tags)

for tag in all_anchor_tags:
   #print(tag.getText())
   print(tag.get("href"))

heading = soup.find(name="h1", id="name")
print(heading)

company_url = soup.select_one(selector = "p a")
print(company_url)


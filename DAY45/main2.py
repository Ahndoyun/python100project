from bs4 import BeautifulSoup
import lxml
import requests

response = requests.get('https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/')

web_page = response.text

soup = BeautifulSoup(web_page, 'html.parser')
print(soup.prettify())

#all movie titles
all_movies = soup.find_all(name="h3", class_="title")

#iterate through tags and put it in a list
movie_titles = [movie.getText() for movie in all_movies]
print(movie_titles)

#reverse the list to get 
for n in range(len(movie_titles) - 1, -1, -1):
    print(movie_titles[n])

#convert to text file
movies = movie_titles[::-1]

with open('movies.txt', mode="w") as file:
    for movie in movies:
        file.write(f"{movie}\n")


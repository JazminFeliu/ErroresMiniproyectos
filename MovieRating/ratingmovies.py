import requests
import json

url = "https://imdb-top-100-movies.p.rapidapi.com/"

headers = {
	"X-RapidAPI-Key": "tu API-KEY",
	"X-RapidAPI-Host": "imdb-top-100-movies.p.rapidapi.com"
}

response = (requests.get(url, headers=headers))
movies_list = response.json()

# Listado de las 100 pelis mejor rankeadas de IMDB
data = movies_list
print ("Top 100 Rating Movies IMDB:\n")
print ("Movie / Rating ")
for movie in data:
    print(movie['title'] + " / " + movie['rating']) 
    





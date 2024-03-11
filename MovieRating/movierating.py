import requests

imdb_id = "tt2934286"

url= f"https://moviesdatabase.p.rapidapi.com/titles/{imdb_id}/ratings"

url_title = f"https://moviesdatabase.p.rapidapi.com/titles/{imdb_id}"

url_top250 = "https://moviesdatabase.p.rapidapi.com/top_rated_250"

headers = {
	"X-RapidAPI-Key": "tu API-KEY",
	"X-RapidAPI-Host": "moviesdatabase.p.rapidapi.com"
}

response = requests.get(url, headers=headers)
results = response.json()

response_title = requests.get(url_title, headers=headers)
results_title = response_title.json()

# Detalle por movie
print("Movie name: ", results_title['results']['originalTitleText']['text'])
print("release year: ", results_title['results']['releaseYear']['year'])

day = results_title['results']['releaseDate']['day']
month = results_title['results']['releaseDate']['month']

print(f"release day is {day} th of Month {month}")

name = results_title['results']['originalTitleText']['text']
print(f"Average rating on this Movie - {name} : ", results['results']['averageRating'])
print("Number of votes :", results['results']['numVotes'])


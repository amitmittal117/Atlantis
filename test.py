import requests
import csv

BASE = 'http://127.0.0.1:5000/'
with open('data.csv') as csv_file:

    response = requests.post(BASE + 'atlantis/csv/', {"data": csv_file})
print(response.json())



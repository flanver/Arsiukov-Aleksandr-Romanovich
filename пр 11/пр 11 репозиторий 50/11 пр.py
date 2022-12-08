import requests
from pprint import pprint
# Имя пользователя github
username = "kubernetes"
# url для запроса
url = f"https://api.github.com/users/{username}"
# делаем запрос и возвращаем json
user_data = requests.get(url).json()
# довольно распечатать данные JSON
pprint(user_data)

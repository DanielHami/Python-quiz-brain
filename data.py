import requests

response_data = requests.get("https://opentdb.com/api.php?amount=10&category=11&difficulty=easy&type=boolean")
data = response_data.json()

question_data = data["results"]

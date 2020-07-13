import requests

BASE = "http://127.0.0.1:5000/"

data = [{'name': 'viral', 'views': 50, 'likes': 10},
        {'name': 'yesh', 'views': 0, 'likes': 100},
        {'name': 'mait', 'views': 5, 'likes': 1000}
        ]

for i in range(len(data)):
    response = requests.put(BASE + "video/" + str(i), data[i])
    print(response.json())

input()
response = requests.patch(BASE + "video/2", {})
print(response.json())

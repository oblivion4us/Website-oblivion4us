import requests

url = "https://jsonplaceholder.typicode.com/posts"
parameters = {
    "urlId" : 1
}

response = requests.get(url, params=parameters)

if response.status_code == 200:
    posts = response.json()

for post in posts:
        print(f"ID: {post['id']}, Title: {post['title']}")
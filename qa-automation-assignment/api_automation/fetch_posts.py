import requests
import json

URL = "https://jsonplaceholder.typicode.com/posts"

response = requests.get(URL)

assert response.status_code == 200, "Status code is not 200"

posts = response.json()

required_keys = {"userId", "id", "title", "body"}

for post in posts:
    assert required_keys.issubset(post.keys()), "Missing keys in response"

with open("api_automation/first_5_posts.json", "w") as f:
    json.dump(posts[:5], f, indent=4)

print("First 5 posts saved successfully.")
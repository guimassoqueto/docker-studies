from requests import get

r = get("https://jsonplaceholder.typicode.com/posts")

if not r.status_code == 200:
    raise ConnectionError("Fail on connecting to the website")

r = r.json()

for post in r:
    print(post['title'])